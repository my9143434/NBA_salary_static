import requests
import sqlite3
import re
from bs4 import BeautifulSoup


def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


def get_player_salary(response):
    parsed_html = BeautifulSoup(response.content, features="html.parser")

    stephen = parsed_html.findAll(class_="name")
    curry = parsed_html.findAll(class_="hh-salaries-sorted")

    n = 1
    temp_list = []
    while n < len(stephen):
        temp = str(stephen[n].contents[1].contents[0]).strip()
        temp2 = int(str(curry[n].contents[0]).strip().replace("$", "").replace(",", ""))
        temp_href = stephen[n].contents[1]['href']

        temp_response = request(temp_href)
        temp_parsed_html = BeautifulSoup(temp_response.content, features="html.parser")
        agent_of_player = temp_parsed_html.findAll(class_="player-fact")
        try:
            match = re.findall(r'His agent is <a.*>(.*)</a>', str(agent_of_player))[0]
        except IndexError:
            match = 'NULL'
        print(match)

        temp_list.append([temp, temp2, match])
        n += 1
    return temp_list


def insert_salary_players(player_salary_list):
    conn = sqlite3.connect('nba.db')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Players')
    cur.execute('CREATE TABLE Players (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, salary INTEGER, agent_id TEXT)')
    for a in player_salary_list:
        cur.execute('SELECT * FROM Players WHERE (name=? AND salary=? AND agent_id=?)', (a[0], a[1], a[2]))
        entry = cur.fetchone()
        if entry == None:
            cur.execute('''INSERT INTO Players (name, salary, agent_id) VALUES (?, ?, ?)''', (a[0], a[1], a[2]))

    conn.commit()

# https://hoopshype.com/reps/
# https://www.balldontlie.io/


target_url = 'https://hoopshype.com/salaries/players/'
response = request(target_url)
player_salary_list = get_player_salary(response)
insert_salary_players(player_salary_list)


