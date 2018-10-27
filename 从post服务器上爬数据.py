import requests
import json
import random
import socket
import struct


def creat_ip():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
#raw string 格式
def get_sanjiaoshou(data):
    url = r"http://triotest.sanjiaoshou.net/nlp/segmentation"
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'X-Requested-With': 'XMLHttpRequest',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Cache-Control': 'no-cache',
               "Content-Type": "application/json"}
    headers.update({'X-Forwarded-For': creat_ip()})
    try:
        respons = requests.post(url, headers=headers, data=data)
    except Exception as e:
        print(data)
        print(respons.status_code)
        print(respons.text)
        print(e)
        return None
    return respons.text
def get_baidu_suggestions(keyword):
    url = "http://m.baidu.com/su?wd=" + keyword + "&action=opensearch&ie=utf-8"
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 4.0.3; U9200 Build/vivo Nex)'}
    headers.update({'X-Forwarded-For': creat_ip()})
    try:
        respons = requests.get(url, headers=headers)
        res = json.loads(respons.text)[1]
    except Exception as e:
        print(keyword)
        print(respons.status_code)
        print(respons.text)
        print(e)
        return None
    return res

def download():
    query_file = "query_cleaned.csv"
    result_file = "sanjiaoshou_result_02.csv"

    userId = "10001"
    latitude = "22.57052"
    longitude = "114.055554"

    with open(result_file, 'w', encoding='utf-8') as rf:
        with open(query_file, 'r', encoding='utf-8') as f:
            i = 1
            while True:
                line = f.readline()
                if i >= 99988:
                    break
                try:
                    data = {"userId": userId, "latitude": latitude, "longitude":longitude, "query": line}
                    data = json.dumps(data)
                    res = get_sanjiaoshou(data)
                    rf.write("{}\t{}".format(line, res))
                    i += 1
                    if i % 100 == 0:
                        print(i)
                except Exception as e:
                    print("{}\t{}\t{}".format(i, line, e))
                    continue
        print(i)
    print("Done!")

if __name__ == '__main__':
    download()