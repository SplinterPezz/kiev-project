from app import app
from flask_pymongo import PyMongo
from app.models.MemeModels import MemeMongoModel, MemeModel
from bs4 import BeautifulSoup

mongo = PyMongo(app)

memes_collection = mongo.db.memes

def save_meme(meme):
    memes_collection.insert_one(meme)

def save_all_memes(memes_to_save, memes_in_db):
    saved_memes = []
    memes_to_insert = []

    existing = {(meme.name, meme.date) for meme in memes_in_db}

    for meme in memes_to_save:
        if (meme.name, meme.date) not in existing:
            memes_to_insert.append(meme.to_dict())
            saved_memes.append(meme)

    if memes_to_insert:
        memes_collection.insert_many(memes_to_insert)

    return saved_memes

def get_all():
    data = memes_collection.find({})

    data_list = []
    for any in data:
        meme_data = MemeMongoModel(**any)
        meme_data_model = MemeModel(meme_data.date, meme_data.name, meme_data.text, meme_data.source)
        data_list.append(meme_data_model)


    return data_list