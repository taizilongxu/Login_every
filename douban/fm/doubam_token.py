#-*- encoding: UTF-8 -*-
#---------------------------------import------------------------------------
import requests
import urllib
#---------------------------------------------------------------------------
class Doubanfm(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self):
        '登陆douban.fm获取token'
        login_data = {
                'app_name': 'radio_desktop_win',
                'version': '100',
                'email': self.email,
                'password': self.password
                }
        s = requests.post('http://www.douban.com/j/app/login', login_data)
        dic = eval(s.text)
        if dic['r'] == '1':
            print dic['err']
        else:
            print dic
            self.token = dic['token']
            self.user_name = dic['user_name']
            self.user_id = dic['user_id']
            self.expire = dic['expire']
            self.login_data = {
                'app_name' : 'radio_desktop_win',
                'version' : '100',
                'user_id' : self.user_id,
                'expire' : self.expire,
                'token' : self.token
                    }

    def get_channel(self):
        '获取channel'
        r = requests.get('http://www.douban.com/j/app/radio/channels')
        self.channel = r.text

    def select_channel(self,num):
        self.channel_num = num

    def get_playlist(sefl):
        '获取播放列表'
        self.login_data['channel'] = self.channel
        post_data = self.login_data.copy()
        post_data['type'] = 'n'

        s = requests.get('http://www.douban.com/j/app/radio/people?' + urllib.urlencode(post_data))
        self.playlist = eval(s.text)
        print s.text

    def play_next(self):
        post_data = self.login_data.copy()

    def rate_music(self):
        post_data = self.login_data.copy()
        post_data['type'] = 'r'
        post_data['sid'] = self.sid
        s = requests.get('http://www.douban.com/j/app/radio/people?' + urllib.urlencode(post_data))

    def unrate_music(self):
        post_data = self.login_data.copy()
        post_data['type'] = 'u'
        post_data['sid'] = self.sid
        s = requests.get('http://www.douban.com/j/app/radio/people?' + urllib.urlencode(post_data))

# user_id, user_name, expire, token = login()
# get_channel()
# channel = 1
# get_playlist(channel,user_id, expire, token)


############################################################################
