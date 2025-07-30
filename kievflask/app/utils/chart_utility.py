def transform_tags_to_chart_XY(new_tags):
    list_data = []
    for any in new_tags:
        data = create_data_XY(any[0], any[1])
        list_data.append(data)
    return list_data

def create_serie(serieName, data):
    return {
        "name": serieName,
        "data": data
    }


def create_data_XY(x, y):
    return {
        "x": x,
        "y": y
    }


def create_xaxis(categories):
    return {
        "categories": categories
    }


def create_basic_chart(series, xaxis):
    return {
        "series": series,
        "xaxis": xaxis
    }