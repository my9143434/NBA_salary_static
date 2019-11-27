import requests
import urllib3
import sqlite3

urllib3.disable_warnings()
test2 = "anthony davis"
test1 = "https://www.balldontlie.io/api/v1/players?search=" + test2
r = requests.get(test1, verify=False)
list_of_dicts = r.json()
# print(type(r))
print(list_of_dicts)

for i in list_of_dicts["data"]:
    print(i["id"])
    print(i)
for a in list_of_dicts["meta"]:
    print(i["id"])
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