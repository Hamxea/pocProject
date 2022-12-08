from consigli.config import data_path_source
from consigli.modules.data_prep_processing import read_data
from consigli.text_search import get_list_content, text_search
from loguru import logger
import sys


def text_search_(url, keyword_one, keyword_two):

    df, mem_history_1 = read_data(url)
    contents = get_list_content(df)
    text_search(contents=contents, words=[keyword_one, keyword_two])

    logger.info('Done.!')


if __name__ == '__main__':
    data_path = data_path_source
    if len(sys.argv) <= 2:
        logger.info('Please specify the information to search...')
        exit(1)

    text_search_(url=data_path, keyword_one=sys.argv[1], keyword_two=sys.argv[2])
