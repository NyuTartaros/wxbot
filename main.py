# encoding: utf-8

import json

from wxpy import *


if __name__ == '__main__':
    # init girl friend info
    gf_dict = json.load(open('specific_man.json', 'r', encoding='utf-8'))
    gf_name = gf_dict['name']
    gf_nickname = gf_dict['NickName']
    gf_sex = FEMALE if gf_dict['Sex'] == 'FEMALE' else MALE
    gf_city = gf_dict['city']

    # init Bot
    bot = Bot()
    gf = bot.friends().search(gf_name, NickName=gf_nickname, Sex=gf_sex, city=gf_city)[0]
    xiaoice = bot.mps().search('小冰', Signature='我是人工智能微软小冰~~')[0]

    @bot.register()
    def monitor_all(msg):
        print(msg)

    @bot.register(gf)
    def reply_gf(msg):
        print(msg)
        xiaoice.send(msg.text)

    @bot.register(xiaoice)
    def reply_xiaoice(msg):
        print(msg)
        gf.send(msg.sender.name + ": " + msg.text)

    embed()
