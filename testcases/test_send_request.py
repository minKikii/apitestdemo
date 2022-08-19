import json
import re

import requests

class TestProductApi:

    access_token = ""
    session = requests.session() #通过session去关联，session默认情况下会自动关联cookie

    def test_get_token(self):
         print("获取token鉴权码")
         urls = "https://api.weixin.qq.com/cgi-bin/token"
         datas = {
              "grant_type":"client_credential",
              "appid":"wx8e8b67ced3c4b884",
              "secret":"27c524bd9ca932e31e229be30b0a805b"
         }
         res = TestProductApi.session.request("get",url=urls,params=datas)
         TestProductApi.access_token = res.json()['access_token']#截取返回的json中的access_token
         print(TestProductApi.access_token)

#创建实例gettoken
gettoken=TestProductApi()
#调用test_get_token方法
gettoken.test_get_token()

#自己写，获取到一个网站的token

class getToken:
    # 设置成全局变量，在其他方法中也能获取到，通过类名访问
    token=""

    def testLogin(self):
        url="https://xxxx.com/dev/xxxx-workpoint/api/admin/form-login"
        data={
            "password":'xxxx',
            "username":"xxx"
        }
        headers={
            "content-type":"application/json"
        }
        res=requests.post(url=url,json=data,headers=headers)
        getToken.token=res.text
        print(getToken.token)

token=getToken()
token.testLogin()