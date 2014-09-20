#coding:utf-8

#这是一个用于登陆百度的脚本

import urllib2,requests,time,re

def login_baidu(name,password):
    #访问主页，获取cookie
    s.get('http://pan.baidu.com')
    s.get('https://passport.baidu.com/v2/api/?login')
    #获取token 值
    cook = s.get("https://passport.baidu.com/v2/api/?getapi&class=login&tpl=mn&tangram=true")
    data = cook.text
    token = re.findall(r"bdPass.api.params.login_token='(.*?)'",data)[0]

    #构造包的头部
    headers = {
    'Host': 'passport.baidu.com',
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0",
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://pan.baidu.com/',
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    s.get("https://passport.baidu.com/v2/api/?login",headers=headers)

    #第一次post数据
    payload={
     'staticpage':'http://pan.baidu.com/res/static/thirdparty/pass_v3_jump.html',
            'charset':'utf-8',
            'token':token,
            'tpl':'netdisk',
            'apiver':'v3',
            'tt': '1392637410384',
            'codestring' : '',
            'safeflg' : '0',
            'u' :'http://pan.baidu.com/',
            'isPhone' : 'false',
            'quick_user'  : '0',
            'loginmerge': 'true',
            'logintype' : 'basicLogin',
            'username': name,
            'password': password,
            'verifycode':'',
            'mem_pass':'on',
            'ppui_logintime' : '49586',
            'callback':'parent.bd__pcbs__hksq59'
    }
    #第一次post，获取验证码地址
    login = s.post("https://passport.baidu.com/v2/api/?login", data=payload,headers=headers,verify=True)
    get_code = re.findall(r'codeString=(.*?)&userName',login.text)[0]
    print get_code

    #获取验证码
    code = s.get("https://passport.baidu.com/cgi-bin/genimage",params=get_code,stream=True)
    path = "code"  #请自行修改路径
    if code.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in code.iter_content():
                f.write(chunk)

    #输入验证码
    verifycode = ''
    while not verifycode:
        verifycode = raw_input("请输入验证码:")
        print verifycode

    #构造post数据
    payload={
            'staticpage' : 'http://pan.baidu.com/res/static/thirdparty/pass_v3_jump.html',
            'charset' : 'utf-8',
            'token' : token,
            'tpl':'netdisk',
            'apiver':'v3',
            'tt': '1392637410384',
            'codestring' : get_code,
            'safeflg' : '0',
            'u' :'http://pan.baidu.com/',
            'isPhone' : 'false',
            'quick_user'  : '0',
            'loginmerge': 'true',
            'logintype' : 'basicLogin',
            'username': name,
            'password': password,
            'verifycode':verifycode,
            #'mem_pass':'on',
            'ppui_logintime' : '49586',
            'callback':'parent.bd__pcbs__hksq59'
        }

    login2 = s.post("https://passport.baidu.com/v2/api/?login", data=payload,headers=headers,verify=True)

    #判断是否登录成功,判断cookie中是否含有'BDUSS'
    if 'BDUSS' in s.cookies:
        print " 登录成功"
    else:
        print "登录失败"

if __name__ == '__main__':

    #构造一个会话，用来跨请求保存cookie
    s = requests.Session()
    name = '你的账户'
    password = '你的密码'
    login_baidu(name,password)
