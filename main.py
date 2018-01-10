# encoding=utf8
import requests
from bs4 import BeautifulSoup
import json
import webbrowser
from wox import Wox


class Main(Wox):
    def query(self, query):
        results = []

        if not query:
            results.append({
                "Title": "使用帮助, 输入:" ,
                "SubTitle":"热映: 查看影院在播放的电影; 其他关键词:将根据电影名称/演员进行匹配",
                "IcoPath": "Images\\movies.png"
            })
            return results
        r = ""
        if query == "热映":
            r = requests.get('http://api.douban.com/v2/movie/in_theaters', params={'start': 0})
        else:
            r = requests.get('http://api.douban.com/v2/movie/search?q=' + query, params={'start': 0})


        r_json = r.json()
        
        for item in r_json['subjects']:
            res = {}
            title = item['title']
            original_title = item['original_title']

            if not title == original_title:
                title = title  +" "+ original_title

            collect_count = item['collect_count']
            score = item['rating']['average']
            year = item['year']
                        
            casts = []
            for cast in item["casts"]:
                casts.append(cast['name'])

            directors = []
            for director in item["directors"]:
                directors.append(director['name'])
            
            res["Title"] = title  + " (" + str(score) + "分, " + str(collect_count) + "人看过)"
            res["SubTitle"] =str(year) + "年" + ", 主演: " + " ".join(casts) + " 导演: " + " ".join(directors)
            res["IcoPath"] = "Images\\movies.png"
            res["JsonRPCAction"] = {"method": "openUrl", "parameters": [item['alt']]}
            results.append(res)
        return results

    def openUrl(self, url):
        webbrowser.open(url)


if __name__ == "__main__":
    Main()
