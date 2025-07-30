from app.utils import utility_operations, chart_utility
from app.models.firePowerModels import firePowerData

def get_death_xaxis_and_series_from_days_total(days_request, list_of_dates, death_total, enjur_total, serie_name):
    if(days_request > len(list_of_dates)):
        enjur_series = chart_utility.create_serie(serie_name + " Injuried", enjur_total)
        death_series = chart_utility.create_serie(serie_name + " Deaths", death_total)
        xaxis = chart_utility.create_xaxis(list_of_dates)
    else:
        enjur_series = chart_utility.create_serie(
            serie_name + " Injuried", enjur_total[-days_request:])
        death_series = chart_utility.create_serie(
            serie_name + " Deaths", death_total[-days_request:])
        xaxis = chart_utility.create_xaxis(list_of_dates[-days_request:])
    series = [death_series, enjur_series]
    return xaxis, series

def get_series_and_xaxis_of_these_days_one(serie, days_request, sorted_dates, series_name):
    if(days_request > len(sorted_dates)):
        series = chart_utility.create_serie(series_name, serie)
        xaxis = chart_utility.create_xaxis(sorted_dates)
    else:
        series = chart_utility.create_serie(series_name, serie[-days_request:])
        xaxis = chart_utility.create_xaxis(sorted_dates[-days_request:])
    return series, xaxis

def get_chart_of_these_days(serie_one, serie_two, days_request, sorted_dates, series_one_name, series_two_name):
    if(days_request > len(sorted_dates)):
        death_series = chart_utility.create_serie(series_one_name, serie_one)
        no_death_series = chart_utility.create_serie(series_two_name, serie_two)
        xaxis = chart_utility.create_xaxis(sorted_dates)
    else:
        death_series = chart_utility.create_serie(series_one_name, serie_one[-days_request:])
        no_death_series = chart_utility.create_serie(
            series_two_name, serie_two[-days_request:])
        xaxis = chart_utility.create_xaxis(sorted_dates[-days_request:])
    series = [death_series, no_death_series]
    chart = chart_utility.create_basic_chart(series, xaxis)
    return chart

def get_dataframes_list_from_kaggle_data(kaggle_df, sum_type, days):
    dates = kaggle_df['date']
    dates_str = utility_operations.transform_list_of_dates_to_str(dates)

    equipment_fields = [
        'aircraft', 'helicopter', 'tank', 'apc', 'artillery',
        'mrl', 'auto', 'fuel_tank', 'drone', 'naval_ship', 'anti_aircraft'
    ]

    equipment_data = {field: kaggle_df[field].tolist() for field in equipment_fields}

    prefix = "Daily " if sum_type == "sub" else "Summed "

    if sum_type == "sub":
        for field in equipment_data:
            equipment_data[field] = utility_operations.calculate_from_next_in_series(equipment_data[field])

    if days > len(dates):
        selected_dates = dates_str
        selected_data = {field: data for field, data in equipment_data.items()}
    else:
        selected_dates = dates_str[-days:]
        selected_data = {field: data[-days:] for field, data in equipment_data.items()}

    series = [
        chart_utility.create_serie(f"Destroyed {prefix}{label.replace('_', ' ').title()}", data)
        for label, data in selected_data.items()
    ]

    x_axis = chart_utility.create_xaxis(selected_dates)
    return x_axis, series

def get_dataframes_list_from_firepower_data(firepower_df):
    nations = firepower_df['name'].tolist()

    categories = {
        'ManPower Score': firepower_df['manpower'].tolist(),
        'Financial Score': firepower_df['financials'].tolist(),
        'AirPower Score': firepower_df['airpower'].tolist(),
        'LandPower Score': firepower_df['landPower'].tolist(),
        'NavalPower Score': firepower_df['navalPower'].tolist(),
        'Logistics Score': firepower_df['logistics'].tolist(),
        'Resources Score': firepower_df['resources'].tolist(),
        'Geography Score': firepower_df['geography'].tolist(),
    }

    power_series = []
    other_series = []

    for label, data in categories.items():
        series = chart_utility.create_serie(label, data)
        if 'Power' in label:
            power_series.append(series)
        else:
            other_series.append(series)

    x_axis = chart_utility.create_xaxis(nations)
    return x_axis, power_series, other_series
def generate_splitted_from_dataframe(onu_articles_df, data_type, sum_type, days, dates_list, prefix):
    df = utility_operations.generate_data_frame_from_json(onu_articles_df[data_type], False)

    categories = ['men', 'women', 'girls', 'boys', 'children']
    data_series = {}

    for category in categories:
        data = df[category].to_numpy().tolist()
        if sum_type == "sub":
            data = utility_operations.calculate_from_next_in_series(data)
        data_series[category] = data

    if days > len(dates_list):
        selected_dates = dates_list
    else:
        selected_dates = dates_list[-days:]

    x_axis = chart_utility.create_xaxis(selected_dates)

    series = [
        chart_utility.create_serie(f"{prefix} {category.capitalize()}", data[-days:] if days <= len(data) else data)
        for category, data in data_series.items()
    ]

    return x_axis, series

def generate_death_enjured_from_data_erame(onu_articles_panda, sum_type):
    death_total = utility_operations.generate_data_frame_from_json(onu_articles_panda['death'], False)[
        'total'].to_numpy().tolist()
    enjur_total = utility_operations.generate_data_frame_from_json(onu_articles_panda['injuried'], False)[
        'total'].to_numpy().tolist()
    if(sum_type == "sub"):
        enjur_series = utility_operations.calculate_from_next_in_series(enjur_total)
        death_series = utility_operations.calculate_from_next_in_series(death_total)
        return enjur_series, death_series
    return death_total, enjur_total

def aggregate_fire_power_data(fire_power_data):
    aggregated_list = []

    for nation in fire_power_data:
        name = nation.name

        def total_from_dict(data_dict, subtract_keys=None):
            total = 0
            for key, value in data_dict.items():
                if subtract_keys and key in subtract_keys:
                    total -= value
                else:
                    total += value
            return total

        manpower_total = total_from_dict(nation.manpower) / 100_000
        financials_total = total_from_dict(nation.financials, subtract_keys=["externalDebt"]) / 10_000_000_000
        airpower_total = total_from_dict(nation.airpower) / 10
        landpower_total = total_from_dict(nation.landPower) / 10
        navalpower_total = total_from_dict(nation.navalPower)
        logistics_total = total_from_dict(nation.logistics) / 1_000_000
        resources_total = total_from_dict(nation.resources) / 1_000_000_000
        geography_total = total_from_dict(nation.geography) / 100_000

        model = firePowerData(
            name,
            manpower_total,
            financials_total,
            airpower_total,
            landpower_total,
            navalpower_total,
            logistics_total,
            resources_total,
            geography_total
        )

        aggregated_list.append(model.to_dict())

    return aggregated_list


def get_prefix_for_death_data(sum_type):
    prefix = ""
    if(sum_type == "sum"):
        prefix = "Summed"
    else:
        prefix = "Daily"
    return prefix

def generate_equipment_series_and_humans(days, pd_merged, onu_articles_panda):
    list_of_dates = onu_articles_panda['date']
    list_of_dates_str = utility_operations.transform_list_of_dates_to_str(list_of_dates)
    prefix = get_prefix_for_death_data("sub")
    xaxis, seriesDeath = generate_splitted_from_data_frame(pd_merged, 'death', "sub", days, list_of_dates_str, prefix + " Dead")
    xaxis, seriesEquipment = getDataFramesListFromKaggleData(pd_merged, "sub", days)   
    return xaxis,seriesEquipment,seriesDeath

def count_articles_and_deaths(kiev_death_articles, onu_articles, sorted_dates):
    death_totals = []
    formatted_dates = []
    article_counts = []

    for date in sorted_dates:
        date_str = utility_operations.date_to_day_and_month_str(date)
        formatted_dates.append(date_str)

        # Trova il numero di morti (ONU)
        death_value = next(
            (art.death['total'] for art in onu_articles if art.date == date),
            0
        )
        death_totals.append(death_value)

        # Conta gli articoli (Kiev)
        count = sum(1 for art in kiev_death_articles if art.date == date)
        article_counts.append(count)

    return death_totals, formatted_dates, article_counts

def count_articles_and_death_articles(kiev_death_articles, sorted_dates):
    no_death_counts = []
    death_counts = []
    formatted_dates = []

    for date in sorted_dates:
        no_death = 0
        with_death = 0
        date_str = utility_operations.date_to_day_and_month_str(date)

        for article in kiev_death_articles:
            if article.date == date:
                if article.death and len(article.death) > 0:
                    with_death += 1
                else:
                    no_death += 1

        formatted_dates.append(date_str)
        no_death_counts.append(no_death)
        death_counts.append(with_death)

    return no_death_counts, death_counts, formatted_dates

def get_death_pandas_dates_and_prefix(sum_type, onu_articles):
    onu_articles_panda = utility_operations.generate_data_frame_from_json(onu_articles, True)
    list_of_dates = onu_articles_panda['date']
    list_of_dates_str = utility_operations.transform_list_of_dates_to_str(list_of_dates)
    prefix = get_prefix_for_death_data(sum_type)
    return onu_articles_panda, list_of_dates_str, prefix

def get_refugees_aggregated_series(refugee_aggregated):
    refugee_aggregated_panda = utility_operations.generate_data_frame_from_json(refugee_aggregated, True)
    list_of_nations = refugee_aggregated_panda['nation'].tolist()
    list_of_values = refugee_aggregated_panda['value'].tolist()
    values_series = chart_utility.create_serie("Refugees location", list_of_values)
    xaxis = chart_utility.create_xaxis(list_of_nations)
    return [values_series], xaxis

def get_refugees_daily_series(refugee_daily, days_request, total_aggregated):
    refugee_daily_panda = utility_operations.generate_data_frame_from_json(refugee_daily, True)
    list_of_dates = refugee_daily_panda['date']
    list_of_dates_str = utility_operations.transform_list_of_dates_to_str(list_of_dates)
    list_of_values = refugee_daily_panda['value'].tolist()
    total_daily = sum(list_of_values)
    difference = total_aggregated - total_daily
    if(total_aggregated > total_daily):
        list_of_values = utility_operations.add_value_in_weighted_way_to_a_list(total_daily, difference, list_of_values)
    series, xaxis = get_series_and_xaxis_of_these_days_one(list_of_values, days_request, list_of_dates_str, "Refugees daily")
    return [series], xaxis