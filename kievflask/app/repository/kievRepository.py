from app import app
from flask_pymongo import PyMongo
from app.models.OnuDataModels import OnuDataModel, OnuDataDeathModel
from app.models.KievArticleModels import KievArticleTagModel, KievArticleModel, KievArticleDeathModel
from app.models.KaggleEquipmentModels import EquipmentDataModel, EquipmentData
from app.models.FirePowerModels import FirePowerModel
from app.models.RefugeeModels import RefugeeAggregatedDataModel, RefugeeAggregatedModel, RefugeeDailyDataModel, refugeeDailyModel
from app.utils import utility_operations

mongo = PyMongo(app)

kiev_indipendent_collection = mongo.db.articles
onu_data_collection = mongo.db.onuData
kaggle_equipment_collection = mongo.db.equipment
refugee_daily_collection = mongo.db.refugeeDaily
refugee_aggregated_collection = mongo.db.refugeeAggregated
firepower_collection = mongo.db.firePower

def get_total_refugees_aggregated():
    aggregate = [
        {
            '$group': {
                '_id': '',
                'value': { '$sum': '$value' }
            }
        }, 
        {
            '$project': {
                '_id': 0,
                'value': '$value'
        }
    }]
    
    value = refugee_aggregated_collection.aggregate(aggregate)
    value_agg = 0

    for any in value:
        value_agg = any['value']
    return value_agg

def get_onu_data_filtered_by_death_values():
    data = onu_data_collection.find({"death.total": {"$ne": None}})
    articles = []
    for any in data:
        onu_data_model = OnuDataModel(**any)
        onu_data_death_model = OnuDataDeathModel(onu_data_model.date, onu_data_model.death, onu_data_model.injuried)
        articles.append(onu_data_death_model)

    sorted_list = sorted(articles, key=lambda t: t.date)
    return sorted_list


def get_kaggle_equiment():
    data = kaggle_equipment_collection.find()
    data_list = []
    for any in data:
        kaggle_data = EquipmentDataModel(**any)
        kaggle_data_model = EquipmentData(kaggle_data.date, kaggle_data.aircraft, kaggle_data.helicopter, kaggle_data.tank, kaggle_data.apc, kaggle_data.artillery,
                                          kaggle_data.mrl, kaggle_data.auto, kaggle_data.fuel_tank, kaggle_data.drone, kaggle_data.naval_ship, kaggle_data.anti_aircraft)
        data_list.append(kaggle_data_model)

    sorted_list = sorted(data_list, key=lambda t: t.date)
    return sorted_list


def get_kiev_data_filtered_by_tag_V2():
    data = kiev_indipendent_collection.find({"tag": {"$ne": None}})
    articles = []
    for any in data:
        kiev_model = KievArticleModel(**any)
        data_converted = utility_operations.set_zeros_in_datatime(kiev_model.date)
        kiev_tag_model = KievArticleTagModel(
            data_converted, kiev_model.tag)
        articles.append(kiev_tag_model)

    sorted_list = sorted(articles, key=lambda t: t.date)
    return sorted_list


def get_kiev_data_death_filtered():
    data = kiev_indipendent_collection.find({'deaths': {"$exists": True}})
    articles = []
    for any in data:
        kiev_model = KievArticleModel(**any)
        data_converted = utility_operations.set_zeros_in_datatime(kiev_model.date)
        kiev_death_model = KievArticleDeathModel(
            data_converted, kiev_model.deaths)
        articles.append(kiev_death_model)

    sorted_list = sorted(articles, key=lambda t: t.date)
    return sorted_list


def get_fire_power_data():
    fire_power_data = firepower_collection.find({})
    fire_power_list = []
    for any in fire_power_data:
        fire_power_model = FirePowerModel(**any)
        fire_power_list.append(fire_power_model)

    return fire_power_list


def get_kiev_data_death():
    data = kiev_indipendent_collection.find({})
    articles = []
    for any in data:
        kiev_model = KievArticleModel(**any)
        data_converted = utility_operations.set_zeros_in_datatime(kiev_model.date)
        kiev_death_model = KievArticleDeathModel(data_converted, kiev_model.deaths)
        articles.append(kiev_death_model)

    sorted_list = sorted(articles, key=lambda t: t.date)
    return sorted_list

def get_refugee_daily_data():
    data = refugee_daily_collection.find({})
    refugees = []
    for any in data:
        refugee__model = refugeeDailyModel(**any)
        refugee_data_model = RefugeeDailyDataModel(refugee__model.date, refugee__model.value)
        refugees.append(refugee_data_model)
    
    sorted_list = sorted(refugees, key=lambda t: t.date)
    return sorted_list

def get_refugee_aggregated_data():
    data = refugee_aggregated_collection.find({})
    refugees = []
    for any in data:
        refugee__model = RefugeeAggregatedModel(**any)
        refugee_data_model = RefugeeAggregatedDataModel(refugee__model.value, refugee__model.nation)
        refugees.append(refugee_data_model)

    return refugees
    