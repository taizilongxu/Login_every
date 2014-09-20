#-*- encoding: UTF-8 -*-
#---------------------------------import------------------------------------
import requests
#---------------------------------------------------------------------------
class Zhihu(object):
    def __init__(self, email, password):
        self.login_data = {
        'email':email,
        'password':password,
        }

    def login(self):
        url = 'http://www.zhihu.com/login'
        s = requests.Session()

        s.post(url, self.login_data)
        r = s.get('http://www.zhihu.com')
        print r.text

def main():
    zhihu = Zhihu('', '')
    zhihu.login()

if __name__ == '__main__':
    main()
############################################################################
