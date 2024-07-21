import re
from bs4 import BeautifulSoup
from src.common_class import *
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
                aigis_unit.owned = False
                aigis_unit.is_awakening = False
                aigis_unit.has_extra_story = False
                aigis_unit.complete_extra_story = False
                aigis_unit.all_complete = False
                aigis_unit_list.append(aigis_unit)
    return aigis_unit_list


def __gen_extra_story():
    with open("scrap_input/extra_story.txt", 'r') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        update_extra_story(lines)


def __gen_group():
    UPDATE_FIELD = "property_belong"
    GROUP = "白の帝国"
    with open("scrap_input/group.txt", 'r') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        update_group(lines, UPDATE_FIELD, GROUP )


def main():
    __gen_group()


if __name__ == '__main__':
    main()
