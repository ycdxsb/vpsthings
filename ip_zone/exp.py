import requests
import os
import chardet
import json
from lxml import etree
from tqdm import tqdm
def mkpath(p):
    if not os.path.exists(p):
        os.makedirs(p)

def response_charchange(response):
    html_byte = response.content
    charset = chardet.detect(html_byte)['encoding'] 
    if (charset.lower() == "gb2312" or charset.lower() == "gbk"):
        response.encoding = 'gbk'
    else:
        response.encoding = 'utf-8'
    return response

ROOT_DIR = os.path.abspath('.')
RESULT_DIR = os.path.join(ROOT_DIR,'results')

mkpath(RESULT_DIR)
base_url = "http://ip.yqie.com/%d/%d/"
for i in tqdm(range(0,256)):
    mkpath(os.path.join(RESULT_DIR,"%d"%i))
    for j in tqdm(range(0,256)):
        filename = "%d.%d.json"%(i,j)
        p = os.path.join(RESULT_DIR,"%d"%i,filename)
        if os.path.exists(p):
            continue
        url = base_url % (i,j)
        #print(url)
        response = requests.get(url,timeout=10)
        response = response_charchange(response)
        text = response.text
        html = etree.HTML(text)
        ipstart = html.xpath('//dd[@class="ipstart"]/text()')
        #print(ipstart)
        ipend = html.xpath('//dd[@class="ipend"]/text()')
        #print(ipend)
        ipaddress = html.xpath('//dd[@class="address"]/text()')
        #print(ipaddress)
        #print(len(ipstart)==len(ipend),len(ipaddress)==len(ipstart))
        if len(ipstart)!=len(ipend) or len(ipaddress)!=len(ipstart):
            print(i,j)
        result = []
        for k in range(len(ipstart)):
            result.append([ipstart[k],ipend[k],ipaddress[k]])
        #print(result)
        with open(p,'w') as f:
            json.dump(result,f)