from flask import jsonify
from app.utils import utility_operations, constants, chart_utility
from app.repository import kievRepository
from app.services import mapAndUtilsKiev
import pandas as pd

STOP_WORDS_ARTICLES = constants.STOP_WORDS
TAGS_COUNT = constants.TAGS_COUNT_MAX

def get_refugees_daily(days_request):
    refugee_daily = kievRepository.get_refugee_daily_data()
    total_refugee_aggregated = kievRepository.get_total_refugees_aggregated()
    
    daily_series, xaxis_daily = mapAndUtilsKiev.get_refugees_daily_series(refugee_daily, days_request, total_refugee_aggregated)
    linearChartDaily = chart_utility.create_basic_chart(daily_series, xaxis_daily)
    return jsonify(linearChartDaily)

def get_refugees_aggregated():
    refugee_aggregated = kievRepository.get_refugee_aggregated_data()
    aggregated_series, xaxis_aggregated = mapAndUtilsKiev.get_refugees_aggregated_series(refugee_aggregated)
    linearChartAggregated = chart_utility.create_basic_chart(aggregated_series, xaxis_aggregated)
    return jsonify(linearChartAggregated)


def get_fire_power():
    fire_power_data = kievRepository.get_fire_power_data()
    fire_power_data_aggregate = mapAndUtilsKiev.aggregate_fire_power_data(fire_power_data)
    fire_power_panda = utility_operations.generate_data_frame_from_json(fire_power_data_aggregate, False)
    xaxis, seriesPower, seriesOther = mapAndUtilsKiev.get_dataframes_list_from_firepower_data(fire_power_panda)
    linearChartPower = chart_utility.create_basic_chart(seriesPower, xaxis)
    linearChartOther = chart_utility.create_basic_chart(seriesOther, xaxis)

    return jsonify({"power": linearChartPower, "resources": linearChartOther})


def get_total_deaths(type, days_request, sum_type):
    onu_articles = kievRepository.get_onu_data_filtered_by_death_values()
    onu_articles_panda, list_of_dates_str, prefix = mapAndUtilsKiev.get_death_pandas_dates_and_prefix(sum_type, onu_articles)

    if(type == "total"):
        death_total, enjur_total = mapAndUtilsKiev.generate_death_enjured_from_data_erame(
            onu_articles_panda, sum_type)
        xaxis, series = mapAndUtilsKiev.get_death_xaxis_and_series_from_days_total(days_request, list_of_dates_str, death_total, enjur_total, prefix)
    else:
        xaxis, series = mapAndUtilsKiev.generate_splitted_from_data_frame(onu_articles_panda, 'death', sum_type, days_request, list_of_dates_str, prefix + " Dead")

    linearChart = chart_utility.create_basic_chart(series, xaxis)
    return jsonify(linearChart)

def get_total_equipment(days, sum_type):
    kaggle_data = kievRepository.get_kaggle_equiment()
    kaggle_pandas = utility_operations.generate_data_frame_from_json(
        kaggle_data, True)
    xaxis, series = mapAndUtilsKiev.getDataFramesListFromKaggleData(
        kaggle_pandas, sum_type, days)

    chart = chart_utility.create_basic_chart(series, xaxis)
    return jsonify(chart)

def get_total_deaths_splitted(type, days_request):
    onu_articles = kievRepository.get_onu_data_filtered_by_death_values()
    onu_articles_panda = utility_operations.generate_data_frame_from_json(
        onu_articles, True)
    list_of_dates = onu_articles_panda['date']
    list_of_dates_str = utility_operations.transform_list_of_dates_to_str(
        list_of_dates)
    xaxis, series = mapAndUtilsKiev.generate_splitted_from_data_frame(onu_articles_panda, type, "sub", days_request, list_of_dates_str, "Daily " + type.capitalize())
    chart = chart_utility.create_basic_chart(series, xaxis)

    return chart


def get_tree_tag_total(days_request):
    kiev_articles = kievRepository.get_kiev_data_filtered_by_tag_V2()

    values = set(map(lambda x: x.date, kiev_articles))
    newlist = [[y.tags for y in kiev_articles if y.date == x] for x in values]

    all_series = []
    counter = 0
    for data in values:
        old_tags = newlist[counter]
        new_tags = utility_operations.count_matrix(
            old_tags, TAGS_COUNT, STOP_WORDS_ARTICLES)
        data_list = chart_utility.transform_tags_to_chart_XY(new_tags)
        this_serie = chart_utility.create_serie(data, data_list)
        all_series.append(this_serie)
        counter += 1

    sorted_list = sorted(all_series, key=lambda t: t['name'])

    updated_list = utility_operations.change_data_type_to_all_series(
        'name', sorted_list)

    if(days_request > len(updated_list)):
        return jsonify(updated_list)

    return jsonify(updated_list[-days_request:])

def get_death_article(days_request):
    kiev_death_articles = kievRepository.get_kiev_data_death()
    dates = set(map(lambda x: x.date, kiev_death_articles))
    sorted_dates = sorted(dates)
    no_death_list, death_list, dates_list = mapAndUtilsKiev.count_articles_and_death_articles(
        kiev_death_articles, sorted_dates)
    chart = mapAndUtilsKiev.get_chart_of_these_days(
        death_list, no_death_list, days_request, dates_list, "Articles About Death", "Articles Not About Death")

    return jsonify(chart)

def get_articles_and_totals_death(days_request):
    kiev_death_articles = kievRepository.get_kiev_data_death()
    onu_articles = kievRepository.get_onu_data_filtered_by_death_values()
    sorted_dates = utility_operations.get_set_sorted_dates_between_two_object(
        kiev_death_articles, onu_articles)
    death_total, list_of_dates, list_articles_count = mapAndUtilsKiev.count_articles_and_deaths(
        kiev_death_articles, onu_articles, sorted_dates)
    new_death_total_updated = utility_operations.calculate_from_next_in_series(
        death_total)
    chart = mapAndUtilsKiev.get_chart_of_these_days(
        new_death_total_updated, list_articles_count, days_request, list_of_dates, "New Deaths", "New Articles")
    return jsonify(chart)


def get_death_and_equipment(days):
    kaggle_data = kievRepository.get_kaggle_equiment()
    kaggle_pandas = utility_operations.generate_data_frame_from_json(
        kaggle_data, True)
    onu_articles = kievRepository.get_onu_data_filtered_by_death_values()
    onu_articles_panda = utility_operations.generate_data_frame_from_json(
        onu_articles, True)
    onu_articles_panda_dropped = onu_articles_panda.drop("injuried", axis=1)
    pd_merged = pd.merge(kaggle_pandas, onu_articles_panda_dropped, on="date")
    xaxis, seriesEquipment, seriesHumans = mapAndUtilsKiev.generate_equipment_series_and_humans(
        days, pd_merged, onu_articles_panda)
    chartEquipment = chart_utility.create_basic_chart(seriesEquipment, xaxis)
    chartHumans = chart_utility.create_basic_chart(seriesHumans, xaxis)
    return jsonify({"human": chartHumans, "equipment": chartEquipment})
