from requests import post
from csv_parser import CSV_Parser


def server(url):
    p = CSV_Parser('./viewedHistory.csv')
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    post(url, json=p.parse(), headers=headers)
