import requests
import re
from bs4 import BeautifulSoup

# find player's agent


def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


# target_url = 'https://hoopshype.com/salaries/players/'
# response = request(target_url)
#
# parsed_html = BeautifulSoup(response.content, features="html.parser")
#
#
# player_href = parsed_html.findAll(class_="name")
# print(player_href[1].contents[1]['href'])       # player's href





target_url = 'https://hoopshype.com/player/chris-paul/salary/'
response = request(target_url)

parsed_html = BeautifulSoup(response.content, features="html.parser")


agent_of_player = parsed_html.findAll(class_="player-fact")
print(agent_of_player)
# match = re.findall(r'His agent is <a.*>(.*)</a>', str(agent_of_player))
# print(match[0])


# target_url = 'https://hoopshype.com/player/stephen-curry/salary/'
# response = request(target_url)
#
# parsed_html = BeautifulSoup(response.content, features="html.parser")
#
#
# agent_of_player = parsed_html.findAll(class_="player-fact")
# match = re.findall(r'His agent is <a.*>(.*)</a>', str(agent_of_player))
# print(match[0])
