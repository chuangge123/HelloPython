from urllib import request
url='http://httpbin.org/ip'
# resp=request.urlopen(url)
# # # # print(resp.read())
# # # # 上面是本机地址
handler=request.ProxyHandler({"http":"221.182.101.213:8123"})
opener=request.build_opener(handler)
resp=opener.open(url)
print(resp.read())