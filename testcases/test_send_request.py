import requests

class TestSendRequest:
    url='https://azalea-tech.com/dev/qiaotou-workpoint/api/admin/form-login'
    data={
        'password':'123',
        'username':'developer'
    }
    headers={
        'Content-Type': 'application/json',
    }
    #疑问：为什么传参传的是json而不是data
    # 使用data，传的是Content-Type 字段的值被设置为 application/x-www-form-urlencoded
    # 使用json，传的Content-Type 字段的值被设置为 application/json
    rep=requests.post(url=url,json=data,headers=headers)
    print(rep.status_code)
    print(rep.text)


# 使用pytest框架，
# py文件必须是以test_开头或者_test结尾；类名必须以Test开头；测试用例必须以tets_开头
