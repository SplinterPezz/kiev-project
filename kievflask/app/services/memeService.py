from flask import jsonify
from datetime import datetime
from app.models.memeModels import memeModel
from app.repository import memeRepository
from app.utils import utility_operations
import requests
import random
from bs4 import BeautifulSoup

REDDIT = "reddit"
MAX_PAGE = 50
TWITCH_QUOTES = "twitchquotes"
COPYPASTA_LOCK = "show copypasta [NSFW]"
NO_MEMES = "No Memes :("

def get_random_meme():
    all_memes = memeRepository.get_all()
    mainPage = "https://www.twitchquotes.com/copypastas/ascii-art?page="+str(random.randint(1, MAX_PAGE))
    fresh_memes = getFreshMemesFromTwitchQuotes(all_memes, mainPage)
    ascii = get_random_memeFromList(fresh_memes)
    if(ascii == NO_MEMES):
        ascii = get_random_memeFromList(all_memes)
    return utility_operations.prettify_text(ascii)

def getFreshMemesFromTwitchQuotes(all_memes, mainPage):
    pageRequestMeme = requests.request("GET", mainPage, headers={}, data={})
    soupFirstPage = BeautifulSoup(pageRequestMeme.text, 'html5lib')

    memes = soupFirstPage.findAll('div',{"class":"custom-scroll"})
    dates = soupFirstPage.findAll('a',{"class":"-date"})
    titles = soupFirstPage.findAll('h3',{"class":"-title-inner-parent"})
    
    memes_list_to_save = []
    count = 0
    for any in titles:
        if(COPYPASTA_LOCK not in memes[count].text):
            title = any.text.strip()
            date = dates[count].text.strip()
            meme = memes[count].text
            meme_model = memeModel(date, title, meme, TWITCH_QUOTES)
            memes_list_to_save.append(meme_model)
        count+=1
    
    fresh_memes = memeRepository.save_all_memes(memes_list_to_save, all_memes)
    return fresh_memes

def get_random_memeFromList(all_memes):
    if(len(all_memes)>0):
        random_number = random.randint(1, len(all_memes))
        
        return all_memes[random_number-1].text
    else:
        return NO_MEMES

def checkIfMemeIsPresent(all_memes, url):
    for any in all_memes:
        if(any.url == url):
            return True
    return False