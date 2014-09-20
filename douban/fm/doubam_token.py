#-*- encoding: UTF-8 -*-
#---------------------------------import------------------------------------
import requests
#---------------------------------------------------------------------------
login_data = {
        'app_name': 'radio_desktop_win',
        'version': '100',
        'email': '',
        'password': ''
        }
s = requests.post('http://www.douban.com/j/app/login', login_data)
print s.text
############################################################################
