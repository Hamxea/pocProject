import pandas as pd
from loguru import logger
import matplotlib

from consigli.modules.data_prep_processing import replace_newlines
from consigli.modules.keywords_stopwords import MAITENANCE_KEYWORDS
from operator import itemgetter


def get_list_content(content: pd.DataFrame)->list:
    """

    :param content:
    :return:
    """
    contents = list(content.values.tolist())
    return [replace_newlines(list(map(str, l))) for l in contents]


def check(sentences, words):
    """

    :param sentences:
    :param words:
    :return:
    """
    res = list(map(lambda x: all(map(lambda y: y.lower() in x.lower().split(),
                                     words)), sentences))
    return [sentences[i] for i in range(0, len(res)) if res[i]]


def search_builder(contents, words):
    """

    :param contents:
    :param words:
    :return:
    """
    return [check(list(map(itemgetter(2), contents)), [w, words[1]]) for w in MAITENANCE_KEYWORDS] \
        if words[0].casefold().__eq__('vedlikehold'.casefold()) \
        else check(list(map(itemgetter(2), contents)), words)


def text_search(contents, words):
    """

    :param contents:
    :param words:
    :return:
    """
    sentences = list(matplotlib.cbook.flatten(
        search_builder(contents=contents, words=words)))

    logger.info(f"Total number of sentences that discuss {words[0]} and {words[1]} are: {len(sentences)} \n")

    for i in range(0, len(sentences)):
        logger.info(f"{i+1}:{sentences[i]} \n")
