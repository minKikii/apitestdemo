import json
import re

import pytest
import requests
from common.yaml_util import YamlUtil

@pytest.fixture(scope="function")
def conn_database():
    print("连接数据库")
    yield
    print('关闭数据库')

class TestProductApi:

    access_token = ""
    session = requests.session() #通过session去关联，session默认情况下会自动关联cookie

    def test_get_token(self):
         print("获取token鉴权码")
         urls = "https://api.weixin.qq.com/cgi-bin/token"
         datas = {
              "grant_type":"client_credential",
              "appid":"wx8e8b67ced3c4b884",
              "secret":"xxxx"
         }
         res = TestProductApi.session.request("get",url=urls,params=datas)
         TestProductApi.access_token = res.json()['access_token']#截取返回的json中的access_token
         print(TestProductApi.access_token)

# #创建实例gettoken
# gettoken=TestProductApi()
# #调用test_get_token方法
# gettoken.test_get_token()

#自己写，获取到一个网站的token

class Login:
    # 设置成全局变量，在其他方法中也能获取到，通过类名访问
    token=""

    def testGetToken(self):
        url="https://xxxx.com/dev/xxxx-workpoint/api/admin/form-login"
        data={
            "password":'xxxx',
            "username":"xxx"
        }
        headers={
            "content-type":"application/json;charset=utf-8"
        }
        res=requests.post(url=url,json=data,headers=headers).text
        # json.loads用于解码 JSON数据。该函数返回Python字段的数据类型
        # res=json.loads(res)
        # print(res)
        Login.token=res
        return Login.token
        # print(token)
        YamlUtil().write_extract_yaml(Login.token)

    def testVillages(self):
        # token=YamlUtil.read_extract_yaml()
        token=Login.token
        url='https://xxx.com/xxx/xxxxx-workpoint/api/admin/xxxx'
        headers={
            "Content-type":'application/json;charset=utf-8',
            "Authorization":token
        }
        result=json.loads(requests.get(url=url,headers=headers).text)
        print(result)
        return result


token=Login()
token.testGetToken()
token.testVillages()


