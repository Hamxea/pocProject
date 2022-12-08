import pandas as pd

import os
import pickle
import re
from string import punctuation
import dask.dataframe as dd

from consigli.modules.keywords_stopwords import NORWEGIAN_STOPWORDS
from consigli.modules.track_memory import track_memory_use

emoji_map_path = os.path.join("/Users/hamzaharunamohammed/Desktop/Etiya/pocProject/consigli/modules/emoji_dict.pkl")
with open(emoji_map_path, "rb") as f:
    emoji_map = pickle.load(f)


# using a function so we can track memory usage
@track_memory_use(close=False, return_history=True)
def read_data(url: str)->pd.DataFrame:
    """

    :param url:
    :return:
    """
    return pd.read_json(url)  # .head(50)


# using a function so we can track memory usage
@track_memory_use(plot=False)
def dask_read(url, blocksize):
    """

    :param url:
    :param blocksize:
    :return:
    """
    # reading train data
    # df = dd.read_csv('./train.csv')
    return dd.read_csv(url, blocksize=blocksize)


def replace_newlines(obj):
    """

    :param obj:
    :return:
    """
    if isinstance(obj, list):
        return[" ".join(item.split()) for item in obj]
    elif isinstance(obj, str):
        return " ".join(obj.split())


def apply_preprocessing(item: str) -> str:

    item = '\n'.join(filter(None, item.split('\n')))
    item = replace_newlines(item)  # remove new lines \n
    item = lowercase(item)
    item = remove_after_apostrophe(item)
    item = remove_numbers(item)
    item = remove_stopwords(item, NORWEGIAN_STOPWORDS)
    item = replace_email(item)
    item = item.replace('\\', ' ')
    item = re.sub("[^a-zA-Z]", " ", item)
    item = ''.join(filter(lambda x: not x.isdigit(), item))
    item = remove_extra_space(item)
    item = remove_repeated_chars(item)
    item = remove_single_char_word(item)
    item = remove_stopwords(item, NORWEGIAN_STOPWORDS)
    item = item.replace("ø", "oo")
    item = item.replace("æ", "ae")
    # item = replace_emojis(item)
    # item = replace_url(item)

    return item


def contraction_look_up(s: str, contractions_dict: dict) -> str:
    """ şanzuman -> şanzuman """
    words = s.split()
    new_text = []

    for word_s in words:
        if word_s in contractions_dict:
            new_text.append(contractions_dict[word_s])
        else:
            new_text.append(word_s)
    return " ".join(new_text)


def lowercase(s: str) -> str:
    """
    Selamlar -> selamlar
    note: "İ".lower() != "i"
    """
    return s.lower()


def remove_after_apostrophe(tokens: str) -> str:
    """
    for chars --> ",’,‘,´,‛,❛,❜
    Ankara"da -> Ankara
    """
    regex_pattern = re.compile(r"(['|’|‘|´|‛|❛|❜][\w]+)")
    tokens = [re.sub(regex_pattern, '', token) for token in tokens.split() if len(re.sub(regex_pattern, '', token)) > 0]
    return " ".join(tokens)


def remove_extra_space(s: str) -> str:
    """ selamlar    nasılsınız -> selamlar nasılsınız """
    return " ".join(s.strip().split())


def remove_numbers(s: str) -> str:
    """ text2speech 12 123 -> text2speech     """
    # Remove numbers not in words
    return re.sub(r"\b\d+\b", " ", s)


def remove_punct_and_isolate(s: str, ALLOWED_PUNC: list = ["!", "?"]) -> str:
    """ selamlar nasılınız? -> selamlar nasılınız ?"""
    s = re.sub(r"([.\(\)\!\?\-\\\/\,])", r" \1 ", s)
    return s.translate(str.maketrans(dict.fromkeys("".join([p for p in punctuation if p not in ALLOWED_PUNC]))))


def remove_repeated_chars(tokens: str) -> str:
    """ selllaaaam -> sellaam """
    regex_pattern = re.compile(r"(.)\1+")
    tokens = [regex_pattern.sub(r"\1\1", token) for token in tokens.split()
              if len(regex_pattern.sub(r"\1\1", token)) > 0]
    return " ".join(tokens)


def remove_single_char_word(tokens: str) -> str:
    """ selamlar n n -> selamlar """
    tokens = [token for token in tokens.split() if len(token) > 1]
    return " ".join(tokens)


def remove_stopwords(s: str, stop_words_list: list) -> str:
    """ güzel ama ingiliççe -> güzel ingiliççe """
    return " ".join([word for word in s.split() if word not in (stop_words_list)])


def replace_email(s: str, replace_text: str = " ") -> str:
    """ example@gmail.com -> """
    return re.sub(r"\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b",
                  " " + replace_text + " ", s, flags=re.MULTILINE).strip()


def replace_emojis(s: str) -> str:
    """ 🐀 -> emoji_id """
    return s.replace(s.compile("|".join(emoji_map.keys())).sub(lambda x: " " + emoji_map[x.group()] + " ", s))


def replace_url(s: str, replace_text: str = " ") -> str:
    """ https://www.google.com -> """
    URL_REGEX = re.compile(
        r"""(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:"".,<>?«»“”‘’]))"""
    )
    return re.sub(URL_REGEX, " " + replace_text + " ", s).strip()


def slang_look_up(s: str, slangs_dict: dict) -> str:
    """ sg -> siktir git """
    words = s.split()
    new_text = []

    for word_s in words:
        if word_s in slangs_dict:
            new_text.append(slangs_dict[word_s])
        else:
            new_text.append(word_s)
    return " ".join(new_text)


def remove_stopwords(s: str, stop_words_list: list) -> str:
    """ güzel ama ingiliççe -> güzel ingiliççe """
    return " ".join([word for word in s.split() if word not in (stop_words_list)])