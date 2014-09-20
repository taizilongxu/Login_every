#-*- encoding: UTF-8 -*-
#---------------------------------import------------------------------------
import requests
#---------------------------------------------------------------------------
class Renren(object):
    def __init__(self, email, password):
        self.login_data = {
        'email':email,
        'password':password,
        }

    def login(self):
        url = 'http://www.renren.com/PLogin.do'
        s = requests.Session()

        s.post(url, self.login_data)
        r = s.get('http://www.renren.com')
        print r.text

def main():
    renren = Renren('', '')
    renren.login()

if __name__ == '__main__':
    main()
############################################################################
