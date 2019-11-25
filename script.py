import requests
import sqlite3
from bs4 import BeautifulSoup


def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


target_url = 'https://hoopshype.com/reps/'
response = request(target_url)

parsed_html = BeautifulSoup(response.content, features="html.parser")

print(parsed_html)
# agent = parsed_html.findAll(class_="name")

    # n = 1
    # temp_list = []
    # while n < len(stephen):
    #     temp = str(stephen[n].contents[1].contents[0]).strip()
    #     temp2 = int(str(curry[n].contents[0]).strip().replace("$", "").replace(",", ""))
    #
    #     temp_list.append([temp, temp2])
    #     n += 1
    # return temp_list