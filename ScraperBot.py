#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 18:58:49 2019

@author: r17935avinash
"""

import urllib
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
from random import randint
from pymongo import MongoClient

def match_classes(targets):
    targets = targets.split()
    def do_match(tag):
        try:
            classes = dict(tag.attrs)["class"]
        except KeyError:
            classes = ""
        return all(c in classes for c in targets)
    return do_match

def extract_entities(link):
    with urllib.request.urlopen(link) as url:
        s = url.read()
    
    #Extract Name
    soup = BeautifulSoup(s, 'html.parser')
    movie_name = soup.h2.string

    #Extract Image Link
    link = soup.find_all('img')
    img_src =link[1].get('src')

    #Extract Overview
    para = soup.find_all(match_classes("overview"))
    para = str(para)
    para = para.split('>')
    para = para[2].split('<')
    overview = para[0]
    return movie_name,img_src,overview

 
if __name__=="__main__":
    data = pd.read_csv("imdbid.csv")
    client = MongoClient("mongodb://avi123:123itrocks@movierecommend-shard-00-00-tgqzh.mongodb.net:27017,movierecommend-shard-00-01-tgqzh.mongodb.net:27017,movierecommend-shard-00-02-tgqzh.mongodb.net:27017/test?ssl=true&replicaSet=MovieRecommend-shard-0&authSource=admin&retryWrites=true")
    print("Connection Established")
    for i in range(300):
        link_id = int(data["tmdbId"][i])
        generate_link = "https://www.themoviedb.org/movie/" + str(link_id)
        movie_name,img_link,overview = extract_entities(generate_link)
        db=client.movies
        movie_details = {
                'Name' : movie_name,
                'Overview' : overview,
                'Image Link' : img_link
                }
        result=db.movie_details.insert_one(movie_details)
        print('Created {0} of 300'.format(i+1))



