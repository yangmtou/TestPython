import requests
import re

url = 'http://www.zzjdkj.cn/book/8/8121/'
respons = requests.get(url)
respons.encoding = 'gbk'
html = respons.text

pattern = re.compile(r'<meta property="og:novel:book_name" content="(.*?)"/>')
title = pattern.findall(html)[0]

fb = open('%s.txt'%title,'w',encoding='gbk')

content = re.findall(r'<div class="jcdf_box">(.*?)</div>',html,re.S)[0]

chaper_content_list = re.findall(r'<a href="(.*?)">(.*?)</a>',content,re.S)

for chaper_content in chaper_content_list:
    chaper_url, chaper_title = chaper_content

    chaper_html_url = f'{url}{chaper_url}'

    chaper_respons = requests.get(chaper_html_url)
    chaper_respons.encoding = 'gbk'
    chaper_html = chaper_respons.text
    chaper_html_content = re.findall(r'<div id="content">(.*?)</div>',chaper_html,re.S)[0]

    chaper_html_content = chaper_html_content.replace('&nbsp;','')

    fb.write(chaper_title)
    fb.write('\n')
    fb.write(chaper_html_content)
    fb.write('\n')
    fb.flush()
    #print(chaper_title)
    #print(chaper_html_content)
    print(chaper_html_url)

fb.close()
