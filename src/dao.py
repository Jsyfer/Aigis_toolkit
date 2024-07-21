import re
import sqlite3
from src.common_class import *

DATABASE = "aigis_toolkit.db"

def create_connection(db_file):
    """ 创建数据库连接 """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
    return conn


def initialize():
    # 创建数据库连接
    conn = create_connection(DATABASE)

    # 创建表
    if conn is not None:
        try:
            c = conn.cursor()
            c.execute("""
                CREATE TABLE IF NOT EXISTS UNIT 
                (
                    id integer PRIMARY KEY,
                    icon text,
                    unit_name text NOT NULL,
                    info_url text,
                    rare text,
                    base_class text,
                    property_belong text,
                    property_race text,
                    property_speciality text,
                    property_season text,
                    property_qualification text,
                    property_collaboration text,
                    obtain_method text,
                    owned boolean,
                    is_awakening boolean,
                    has_extra_story boolean,
                    complete_extra_story boolean,
                    all_complete boolean
                );""")
            conn.commit()
        except Exception as e:
            print(e)
    else:
        print("Error! cannot create the database connection.")


def insert(aigis_unit_list):
    # 创建数据库连接
    conn = create_connection(DATABASE)
    # 插入新数据
    if conn is not None:
        try:
            cursor = conn.cursor()
            for aigis_unit in aigis_unit_list:
                cursor.execute("""INSERT INTO UNIT (icon, unit_name, info_url, rare) VALUES(?,?,?,?);""",
                    (aigis_unit.icon, aigis_unit.unit_name, aigis_unit.info_url, aigis_unit.rare,))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)


def update_extra_story(unit_name_list):
    # 创建数据库连接
    conn = create_connection(DATABASE)
    # 插入新数据
    if conn is not None:
        try:
            cursor = conn.cursor()
            for unit_name in unit_name_list:
                update_sql = f"UPDATE UNIT SET has_extra_story = True WHERE unit_name = '{unit_name}';"
                cursor.execute(update_sql)
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)


def update_group(unit_name_list, update_field, group):
    # 创建数据库连接
    conn = create_connection(DATABASE)
    # 插入新数据
    if conn is not None:
        try:
            cursor = conn.cursor()
            for unit_name in unit_name_list:
                obtain_method = '0'
                if re.match(r'^[★■☆◇◆].*', unit_name):
                    obtain_method = unit_name[0]
                    unit_name = unit_name[1:]
                update_sql = f"UPDATE UNIT SET {update_field} = '{group}', obtain_method = '{obtain_method}' WHERE unit_name = '{unit_name}';"
                cursor.execute(update_sql)
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)


def update_field_by_id(data):
    # 创建数据库连接
    conn = create_connection(DATABASE)
    result = []
    # 插入新数据
    if conn is not None:
        try:
            cursor = conn.cursor()
            update_key = data['update_key']
            update_field = data['update_field']
            update_value = data['update_value']
            update_sql = f"UPDATE UNIT SET {update_field} = {update_value} WHERE id = '{update_key}';"
            result.append(update_sql)
            cursor.execute(update_sql)
            conn.commit()
            conn.close()
            result.append("update success!")
        except Exception as e:
            result.append(e)
            print(e)
    return result

def select_all():
    # 创建数据库连接
    conn = create_connection(DATABASE)
    # 插入新数据
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM UNIT;""")
            rows = cursor.fetchall()
            aigis_unit_list = [AigisUnit(*row) for row in rows]
            conn.close()
            return aigis_unit_list
        except Exception as e:
            print(e)

