import re
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
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


def __gen_unit_awakening_material(url):
    # 取得网页数据
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    session.mount('https://', adapter)
    response = session.get(url=url, headers=headers)
    # 检查请求是否成功
    if response.status_code == 200:
        # 番剧标题
        raw_content = BeautifulSoup(response.text, "html.parser").findAll('li')
        counter = 0
        awakening_material = ''
        for li_content in raw_content:
            if '/☆4金' in li_content.text:
                counter = counter + 1
                if counter <= 3:
                    awakening_material = awakening_material + li_content.text.split('/')[1].replace('☆4金','')
                    if counter <= 2:
                        awakening_material = awakening_material + '、'
        return awakening_material


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
    aigis_unit_list = select_all()
    for aigis_unit in aigis_unit_list:
        print(aigis_unit.id)
        awakening_material = __gen_unit_awakening_material('https://wikiwiki.jp' + aigis_unit.info_url)
        data = {
            'update_key': aigis_unit.id,
            'update_field': 'awakening_material',
            'update_value': awakening_material
        }
        update_field_by_id(data)


if __name__ == '__main__':
    main()
