# encoding=utf8
import requests
from bs4 import BeautifulSoup
import json
import webbrowser
from wox import Wox


class Main(Wox):
    def query(self, query):
        if not query:
            return ""

        r = requests.get('http://api.douban.com/v2/movie/search?q=' + query, params={'start': 0})
        r_json = r.json()
        results = []
        for item in r_json['subjects']:
            res = {}
            title = item['title']
            score = item['rating']['average']
            res["Title"] = title
            year = item['year']
            res["SubTitle"] = "Year: " + str(year) + "   Score: " + str(score)
            res["IcoPath"] = "Images\\movies.png"
            res["JsonRPCAction"] = {"method": "openUrl", "parameters": [item['alt']]}
            results.append(res)
        return results

    def openUrl(self, url):
        webbrowser.open(url)


if __name__ == "__main__":
    Main()
