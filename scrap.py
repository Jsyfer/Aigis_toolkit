import re
from bs4 import BeautifulSoup
from common_class import *
from src.dao import * 

PATH = "/Users/jsyfer/Downloads/black.html"
RARE = "sapphire"

def __gen_unit_info_by_rare(path, rare):
    # 取得网页数据
    with open(path, 'r') as f:
        contents = f.read()
        # start scrap
        unit_container = BeautifulSoup(contents, "lxml").findAll('div', {'class': 'splitinclude-included-page-container'})
        aigis_unit_list = []
        for unit in unit_container:
            aigis_unit = AigisUnit()
            regex = re.compile('background-color:.*text-align:center;')
            unit_info = unit.find('td', {'style': regex})
            if unit_info is not None:
                aigis_unit.unit_name = unit_info.find('a')['title']
                aigis_unit.info_url = unit_info.find('a')['href']
                aigis_unit.icon = unit_info.find('img')['src']
                aigis_unit.rare = rare
                aigis_unit_list.append(aigis_unit)
    return aigis_unit_list


def main():
    aigis_unit_list = __gen_unit_info_by_rare(PATH, RARE)
    insert(aigis_unit_list)


if __name__ == '__main__':
    main()
