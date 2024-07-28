import re
import time
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


def __scrap_unit_awakening_material(url):
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
    else:
        print(f"status code:{response.status_code}")
        time.sleep(60)


def __gen_unit_awakening_material():
    aigis_unit_list = select_all()
    for aigis_unit in aigis_unit_list:
        print(aigis_unit.id)
        awakening_material  = None
        while awakening_material is None:
            awakening_material = __scrap_unit_awakening_material('https://wikiwiki.jp' + aigis_unit.info_url)
        data = {
            'update_key': aigis_unit.id,
            'update_field': 'awakening_material',
            'update_value': awakening_material
        }
        update_field_by_id(data)


def __gen_extra_story():
    with open("scrap_input/extra_story.txt", 'r') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        update_extra_story(lines)


def resolve_property_response(response, identifier, identify_id, update_field, group=''):
    raw_content = BeautifulSoup(response.text, "html.parser").find(identifier, {'id':identify_id}).findNext('div').find('tbody').findAll('tr')
    for row in raw_content:
        first_column_value = row.find('td').text
        first_column_th = row.find('th')
        if first_column_value == '属性':
            group = row.findAll('td')[1].find('strong').text
        elif first_column_th is not None and first_column_th.text in ['近', '遠', '遠近']:
            property_distance = first_column_th.text
            unit_name_list = []
            for td in row.findAll('td'):
                td_value = td.get_text(',')
                if td_value is not None:
                    if td_value in ['', '編集', '\u3000']:
                        continue
                    else:
                        unit_names = re.sub(r"([★■☆◇◆]),", '\g<1>', td_value)
                        unit_name_list = unit_names.split(',')
                        if '\u3000' in unit_name_list:
                            unit_name_list.remove('\u3000')
                        update_group(unit_name_list, update_field, group )
                        # 遠近距離更新
                        update_group(unit_name_list, 'property_distance', property_distance )

def __gen_group():
    URL="https://wikiwiki.jp/aigiszuki/%E3%83%A6%E3%83%8B%E3%83%83%E3%83%88%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97"
    # 取得网页数据
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    session.mount('https://', adapter)
    response = session.get(url=URL, headers=headers)
    # 检查请求是否成功
    if response.status_code == 200:
        # 属性-所属
        resolve_property_response(response, 'h3', 'h3_content_2_0', 'property_belong')
        # 属性-種族
        resolve_property_response(response, 'h3', 'h3_content_2_1', 'property_race')
        # 属性-特性
        resolve_property_response(response, 'h3', 'h3_content_2_2', 'property_speciality')
        # 属性-季節
        resolve_property_response(response, 'h3', 'h3_content_2_3', 'property_season')
        # 男性
        resolve_property_response(response, 'h4', 'h4_content_2_5', 'property_sex', '男')
        # 特定能力
        resolve_property_response(response, 'h4', 'h4_content_2_6', 'property_qualification')
        # コラボ
        raw_content = BeautifulSoup(response.text, "html.parser").find('h3', {'id':'h3_content_1_5'}).findNext('div').find('tbody').findAll('tr')
        for row in raw_content:
            if row.find('td') is None:
                continue
            first_column_value = row.find('td').text
            group = first_column_value
            unit_name_list = []
            for td in row.findAll('td')[1:]:
                td_value = td.get_text(',')
                if td_value is not None:
                    if td_value in ['', '\u3000']:
                        continue
                    else:
                        unit_names = re.sub(r"([★■☆◇◆]),", '\g<1>', td_value)
                        unit_name_list = unit_names.split(',')
                        if '\u3000' in unit_name_list:
                            unit_name_list.remove('\u3000')
                        update_group(unit_name_list, 'property_collaboration', group )

    else:
        print(f"status code:{response.status_code}")





def main():
    __gen_group()


if __name__ == '__main__':
    main()
