import requests, json;

url = 'https://www.balldontlie.io/api/v1/teams';
r = requests.get(url);
print(r.text);
print(r.status_code)
print(r.json)
