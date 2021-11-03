import requests
import json


class RunMain:
    def __init__(self, url, method, data=None):
        res = self.run_main(url, method, data)

    def send_get(self, url, data):
        res = requests.get(url=url, data=data).text
        return json.dumps(res, indent=2, sort_keys=True)
        # return res

    def send_post(self, url, data):
        res = requests.post(url=url, data=data).text
        return json.dumps(res, indent=2, sort_keys=True)
        # return res

    def run_main(self, url, method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res
if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    data = {
            'text': 'number one',
            'text2': 'number two'
        }
    run = RunMain(url, 'POST', data)
# data ={
#     'text':'number one',
#     'text2':'number two'
# }
# res = requests.post(url='http://localhost:8080/success',data=data)
# print(res.text)
