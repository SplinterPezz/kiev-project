import json
from bson import json_util
import pandas as pd
from collections import Counter

def prettify_text(text):
    text = '<pre style="word-wrap: break-word; white-space: pre-wrap;background-color: black;color: #1bff00;min-width: 500;">' + text + '</pre>'
    return text

def add_value_in_weighted_way_to_a_list(total_daily, difference, list_of_values):
    new_list = []
    for any in list_of_values:
        value_to_sum = (any / total_daily)*difference
        new_value = any + int(value_to_sum)
        new_list.append(new_value)
    return new_list

def date_to_day_and_month_str(date):
    return str(date.day) +"-"+ str(date.strftime("%B"))[0:3]
    #return str(date.month) +"/"+ str(date.day)

def data_to_json(data):
    return json.loads(json_util.dumps(data))

def set_zeros_in_datatime(dataToConvert):
    new_data = dataToConvert.replace(hour=0, minute=0, second=0)
    return new_data


def transform_list_of_dates_to_str(dates):
    list_dates_str = []
    for any in dates:
        this_date_str = date_to_day_and_month_str(any)
        list_dates_str.append(this_date_str)
    return list_dates_str

def calculate_from_next_in_series(this_serie):
    new_serie = [y - x for x, y in zip(this_serie, this_serie[1:])]
    new_serie_updated = [int(new_serie[0]/2)] + new_serie
    return new_serie_updated

def generate_data_frame_from_json(data, to_dict):
    if(to_dict):
        return pd.DataFrame.from_records([s.to_dict() for s in data])
    return pd.DataFrame.from_records(data)

def get_set_sorted_dates_between_two_object(list_one, list_two):
    dates_list_one = set(map(lambda x: x.date, list_one))
    dates_list_two = set(map(lambda x: x.date, list_two))

    if(len(dates_list_one) > len(dates_list_two)):
        return sorted(dates_list_two)
    else:
        return sorted(dates_list_one)

def explode_matrix_and_remove_stop_words(tags, stop_words):
    full_list = []
    for this_list in tags:
        for any in this_list:
            if(any not in stop_words):
                full_list.append(any)

    return full_list

def count_matrix(tags, tags_count, stop_words):
    full_list = explode_matrix_and_remove_stop_words(tags, stop_words)
    new_list = Counter(full_list)
    new_list_ordered = new_list.most_common()[0:tags_count]
    return new_list_ordered


def change_data_type_to_all_series(value_name, list):
    new_list = []

    for any in list:
        new_element = any.copy()
        data_transformed = date_to_day_and_month_str(
            any[value_name])
        new_element[value_name] = data_transformed
        new_list.append(new_element)

    return new_list