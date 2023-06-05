#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2/23/23 10:20 PM
# @Author  : diablo427
# @Email   :  zcx1345478@163.com
# @File    : 爬取酷狗音乐.py
# @Software : PyCharm
import requests
import json


def get_music():
    # 伪装自己
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    # 音乐列表信息
    music_list = 'https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1677167357396&mid=bb7c1eeeaa03faba986a651b53744fbd&uuid=bb7c1eeeaa03faba986a651b53744fbd&dfid=3exmz74J2dJS44sGf93xNPDh&keyword=一路顺风&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=1f5bc96d85db28edfa5c636c00615479'
    music_list_resquest = requests.get(music_list, headers=headers)
    # print(music_list_resquest.text[12:-2])
    music_list_resquest_json = music_list_resquest.text[12:-2]
    # print(json.loads(music_list_resquest_json)['data']['lists'])
    song_list = json.loads(music_list_resquest_json)['data']['lists']
    # print(song_list)

    # for song in song_list:
    #     print(f"{song['OriSongName']} \t {song['SingerName']} \t {song['EMixSongID']}")
    for i, s in enumerate(song_list):
        print(f'{i + 1}---{s.get("OriSongName")}---{s.get("SingerName")}-----{s.get("EMixSongID")}')
    num = input("请输入要下载第几首音乐：")

    # 音乐信息url
    headers2 = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'cookie': 'kg_mid=bb7c1eeeaa03faba986a651b53744fbd; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1677162057; kg_dfid=3exmz74J2dJS44sGf93xNPDh'
    }
    # 'cookie':'kg_mid=bb7c1eeeaa03faba986a651b53744fbd; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1677162057; kg_dfid=3exmz74J2dJS44sGf93xNPDh'
    music_info_url = f'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&encode_album_audio_id={song_list[int(num) - 1].get("EMixSongID")}'
    info_resp = requests.get(music_info_url, headers=headers2)
    # 音乐地址
    music_url = info_resp.json()["data"]['play_url']
    audio_name = info_resp.json()["data"]['audio_name']
    # 发送请求到服务器，获取音乐资源
    music_requests = requests.get(music_url, headers=headers)
    # 服务器回应的数据--保存数据
    with open(f'{audio_name}.mp3', 'wb') as f:
        f.write(music_requests.content)


'''
    # 音乐信息url
    music_info_url = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&encode_album_audio_id=j2uxkf4'
    music_url = 'https://webfs.ali.kugou.com/202302232221/384bcf8fafd3439def441f07a0329fb4/part/0/2448060/KGTX/CLTX001/clip_7b45cc6d324d9a831f8f2340729d85c0.mp3'

    # 发送请求到服务器，获取音乐资源
    music_requests = requests.get(music_url, headers=headers)
    # 服务器回应的数据--保存数据
    with open('zzz.mp3', 'wb') as f:
        f.write(music_requests.content)
        
'''

'''
服务器响应的数据结果
.text 代表访问的数据是文字
.content 代表访问的数据是多媒体文件(图片、音乐、视频、文件等)
.json() 访问的文字是json类型
'''

if __name__ == '__main__':
    get_music()
