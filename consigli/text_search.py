import pandas as pd
from loguru import logger
from modules.textsearch import textsearch


def replace_newlines(obj):
    if isinstance(obj, list):
        return[" ".join(item.split())for item in obj]


def read_data(url: str)->pd.DataFrame:
    return pd.read_json(url).head(5)


def get_list_content(content: pd.DataFrame)->list:
    contents = list(content.values.tolist())
    return [replace_newlines(list(map(str, l))) for l in contents]


df = read_data('/Users/hamzaharunamohammed/Desktop/Etiya/others/poc_pojects/consigli/dataset/data.json')

contents = get_list_content(df)

# t = textsearch(contents, histogram=False)


import sys
sys.dont_write_bytecode = True
import os
import ast
import json


# loads
def load_test():
    y = []
    for a in open('//consigli/dataset/test_data.txt', 'rb'):
        y.append(a)
    y = y[0]
    return ast.literal_eval(y)


# tests
def test_search():
    test_data = load_test()
    t = textsearch(test_data, True)
    return t


t = test_search()

logger.info('The data...'.format(df))
