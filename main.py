# encoding: utf-8

import json

from wxpy import *


if __name__ == '__main__':
    # init girl friend info
    speci_man_dict = json.load(open('specific_man.json', 'r', encoding='utf-8'))
    speci_man_name = speci_man_dict['name']
    speci_man_nickname = speci_man_dict['NickName']
    speci_man_sex = FEMALE if speci_man_dict['Sex'] == 'FEMALE' else MALE
    speci_man_city = speci_man_dict['city']

    # init Bot
    bot = Bot()
    speci_man = bot.friends().search(speci_man_name, NickName=speci_man_nickname,
                              Sex=speci_man_sex, city=speci_man_city)[0]
    xiaoice = bot.mps().search('小冰', Signature='我是人工智能微软小冰~~')[0]

    @bot.register()
    def monitor_all(msg):
        print(msg)

    @bot.register(speci_man)
    def reply_speci_man(msg):
        print(msg)
        xiaoice.send(msg.text)

    @bot.register(xiaoice)
    def reply_xiaoice(msg):
        print(msg)
        speci_man.send(msg.text)

    embed()
