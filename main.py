from urllib import request,parse
url='https://www.lagou.com/jobs/list_python?labelWords=sug&fromSearch=true&suginput=py'
url2='https://www.lagou.com/jobs/list_python?labelWords=sug&fromSearch=true&suginput=py'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=sug&fromSearch=true&suginput=py',
    'Cookie':'JSESSIONID=ABAAABAAAGGABCBB353C92BE1F0980857A864647A5B9A93; WEBTJ-ID=20190823140649-16cbd15aa4541a-0cacfb868ad911-7373e61-2073600-16cbd15aa46836; X_HTTP_TOKEN=42daf4b72327b2816040456651bf5e71415983ed09; index_location_city=%E5%85%A8%E5%9B%BD; _ga=GA1.2.335537730.1566540414; _gid=GA1.2.582416069.1566540414; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1566540415; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1566540415; user_trace_token=20190823140652-337599b3-c56c-11e9-8b98-525400f775ce; LGSID=20190823140652-33759ad1-c56c-11e9-8b98-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20190823140652-33759c9e-c56c-11e9-8b98-525400f775ce; LGUID=20190823140652-33759d08-c56c-11e9-8b98-525400f775ce; SEARCH_ID=15b64ee16a4d4c099b350e0d8e094bf6',

}
data={
    'first':'true',
    'pn':1,
    'kd':'python'
}
req=request.Request(url2,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
resp=request.urlopen(req)
print(resp.read().decode('utf-8'))
