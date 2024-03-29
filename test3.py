import requests
import urllib3
import sqlite3
import json
import time


def get_eff(id):
    insert_url = "https://www.balldontlie.io/api/v1/season_averages?player_ids[]=" + str(id)
    r = requests.get(insert_url, verify=False)
    list_of_dicts = r.json()

    try:
        temp_min = list_of_dicts["data"][0]["min"]
        temp2_min = temp_min.split(":")
        ave_min = round(int(temp2_min[0]) + (int(temp2_min[1])/60), 2)

        temp_total = list_of_dicts["data"][0]["pts"] + list_of_dicts["data"][0]["reb"] + list_of_dicts["data"][0]["stl"] + list_of_dicts["data"][0]["ast"] + list_of_dicts["data"][0]["blk"] - (list_of_dicts["data"][0]["fga"] - list_of_dicts["data"][0]["fgm"]) - (list_of_dicts["data"][0]["fta"] - list_of_dicts["data"][0]["ftm"]) - list_of_dicts["data"][0]["turnover"]
        player_eff = temp_total * ave_min / list_of_dicts["data"][0]["games_played"]
        temp_return = [player_eff, list_of_dicts["data"][0]["pts"]]
    except IndexError:
        player_eff = None
        temp_return = None

    return temp_return


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
            # time.sleep(1)
            temp_return = (get_eff(list_of_dicts["data"][0]["id"]))
            temp_name = str(name)[2:-3]
            print(temp_name)

            cur.execute('''UPDATE Players SET efficiency = ?, points = ?, api_id = ?, team = ? WHERE name = (?) ''', (temp_return[0], temp_return[1], int(list_of_dicts["data"][0]['id']), str(list_of_dicts["data"][0]['team']['full_name']), temp_name))

        except json.decoder.JSONDecodeError:
            continue
        except IndexError:
            continue
    conn.commit()


def add_column():
    try:
        add_column = "ALTER TABLE Players ADD COLUMN efficiency"
        cur.execute(add_column)
        add_column = "ALTER TABLE Players ADD COLUMN api_id INTEGER"
        cur.execute(add_column)
        add_column = "ALTER TABLE Players ADD COLUMN team TEXT"
        cur.execute(add_column)
        add_column = "ALTER TABLE Players ADD COLUMN points INTEGER"
        cur.execute(add_column)
    except sqlite3.OperationalError:
        pass


conn = sqlite3.connect('test.db')
cur = conn.cursor()
add_column()
players_get_api_id()

