import requests
import urllib3
import sqlite3
import json
import time


def get_eff(id):
    insert_url = "https://www.balldontlie.io/api/v1/season_averages?player_ids[]=" + str(id)
    r = requests.get(insert_url, verify=False)
    list_of_dicts = r.json()

    temp_min = list_of_dicts["data"][0]["min"]
    temp2_min = temp_min.split(":")
    ave_min = round(int(temp2_min[0]) + (int(temp2_min[1])/60), 2)

    temp_total = list_of_dicts["data"][0]["pts"] + list_of_dicts["data"][0]["reb"] + list_of_dicts["data"][0]["stl"] + list_of_dicts["data"][0]["ast"] + list_of_dicts["data"][0]["blk"] - (list_of_dicts["data"][0]["fga"] - list_of_dicts["data"][0]["fgm"]) - (list_of_dicts["data"][0]["fta"] - list_of_dicts["data"][0]["ftm"]) - list_of_dicts["data"][0]["turnover"]
    player_eff = temp_total * ave_min / list_of_dicts["data"][0]["games_played"]

    return player_eff


def players_get_api_id():
    urllib3.disable_warnings()
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()

    cur.execute('SELECT name FROM Players')
    results1 = cur.fetchall()

    for name in results1:
        time.sleep(1)
        insert_url = "https://www.balldontlie.io/api/v1/players?search=" + name[0]
        r = requests.get(insert_url, verify=False)
        try:
            list_of_dicts = r.json()
            time.sleep(1)
            print(get_eff(list_of_dicts["data"][0]["id"]))

        except json.decoder.JSONDecodeError:
            continue


players_get_api_id()

# print(type(r))
# print(list_of_dicts)

# for i in list_of_dicts["data"]:
#     print(i["id"])

# for a in list_of_dicts["meta"]:
#     print(i["id"])

# print(list_of_dicts["last_name"])
# print(list_of_dicts["first_name"])
# connect1 = str(list_of_dicts["first_name"]) + " " +str(list_of_dicts["last_name"])
# print(connect1)

# conn = sqlite3.connect('test.db')
# cur = conn.cursor()
#
# cur.execute('SELECT name FROM Players WHERE (name=?)', (connect1,))
#
# entry = cur.fetchone()
# if entry != None:
#     print(list_of_dicts["id"])