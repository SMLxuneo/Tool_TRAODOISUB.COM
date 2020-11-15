import requests
from time import sleep
import random
from configparser import ConfigParser
import os
cccc = open('nguyenhoa.txt', 'r', encoding='utf-8').readlines()
list_x = []
for x in cccc:
    b = x.find('wd=')
    if b < 0:
        x = x + ';wd=1366x657'
    list_x.append(x.replace('\n', ''))

listnv = []
print('\n+---------------------------------------------+\n        TOOL CAY XU VIP TRAODOISUB.COM BY NGUYENHOA\n-----------------------------------------------\n      Copyright © 2020 By NGUYENHOADEV.COM\n┌─────────────────────────────────────────────┐\n│                 Versoin: 3.2                │\n├─────────────────────────────────────────────┤\n│     Download Tool: https://github.com/SMLxuneo/Tool_TRAODOISUB.COM   │\n└─────────────────────────────────────────────┘\n')
config = ConfigParser()
config.read('cauhinh.ini')
user = config.get('main', 'user')
pwd = config.get('main', 'pwd')
vonglap = int(config.get('main', 'vonglap'))
delayvong = int(config.get('main', 'delayvong'))
nhiemvuvong = int(config.get('main', 'nhiemvuvong'))
delaycx = int(config.get('main', 'delaycx'))
delaycmt = int(config.get('main', 'delaycmt'))
delaysub = int(config.get('main', 'delaysub'))
delaypage = int(config.get('main', 'delaypage'))
delaylike = int(config.get('main', 'delaylike'))
like = config.get('main', 'like')
page = config.get('main', 'page')
sub = config.get('main', 'sub')
cmt = config.get('main', 'cmt')
camxuc = config.get('main', 'camxuc')
if like == 'on':
    listnv.append('like')
    if delaylike < 5:
        print('Error: Delay like min 5s!')
        sleep(2)
        exit()
if page == 'on':
    listnv.append('page')
    if delaypage < 10:
        print('Error: Delay page min 10s!')
        sleep(2)
        exit()
if sub == 'on':
    listnv.append('sub')
    if delaysub < 5:
        print('Error: Delay sub min 5s!')
        sleep(2)
        exit()
if cmt == 'on':
    listnv.append('cmt')
    if delaycmt < 5:
        print('Error: Delay comment min 5s!')
        sleep(2)
        exit()
if camxuc == 'on':
    listnv.append('camxuc')
    if delaycx < 5:
        print('Error: Delay reaction min 5s!')
        sleep(2)
        exit()
else:

    def camxuc():
        global xu
        dem = 0
        response = requests.get(f"https://traodoisub.com/scr/api_job.php?chucnang=camxuc&user={user}")
        try:
            data = response.json()
            so_nv = len(data)
            if so_nv > 0:
                print(f"[+] {user}-> {idfb} da tim thay {so_nv} nhiem vu!")
            else:
                print(f"[+] {user}-> {idfb} het nhiem vu cam xuc! Chuyen ID khac")
        except:
            print(f"[+] {user}-> Sever dang gap su co, se chay lại sau: 30s!")
            sleep(30)
            camxuc()
        else:
            headersfb = {'authority':'mbasic.facebook.com', 
             'cache-control':'max-age=0', 
             'upgrade-insecure-requests':'1', 
             'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Mobile Safari/537.36', 
             'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
             'sec-fetch-site':'none', 
             'sec-fetch-mode':'navigate', 
             'sec-fetch-user':'?1', 
             'sec-fetch-dest':'document', 
             'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5', 
             'cookie':cookie_fbs}
            for xxx in data:
                if dem < nhiemvuvong:
                    uid = xxx['id']
                    loai = xxx['type']
                    check = uid.find('_')
                    if check > 0:
                        s = uid.split('_')
                        uid2 = f"story.php?story_fbid={s[1]}&id={s[0]}"
                        rr = requests.get(f"https://mbasic.facebook.com/{uid2}", headers=headersfb, timeout=10)
                        response = requests.get((rr.url), headers=headersfb, timeout=10)
                        try:
                            uid2 = response.text.split('amp;ft_id=')[1].split('&amp;origin_uri=')[0]
                        except:
                            pass

                    else:
                        uid2 = uid
                    url2 = f"https://mbasic.facebook.com/reactions/picker/?is_permalink=1&ft_id={uid2}"
                    h = requests.get(url2, headers=headersfb, timeout=10)
                    haha = h.text.split('<a href="')
                    try:
                        if loai == 'LOVE':
                            haha2 = haha[2].split('" style="display:block"')[0].replace('amp;', '')
                        else:
                            if loai == 'WOW':
                                haha2 = haha[5].split('" style="display:block"')[0].replace('amp;', '')
                            else:
                                if loai == 'HAHA':
                                    haha2 = haha[4].split('" style="display:block"')[0].replace('amp;', '')
                                else:
                                    if loai == 'SAD':
                                        haha2 = haha[6].split('" style="display:block"')[0].replace('amp;', '')
                                    else:
                                        haha2 = haha[7].split('" style="display:block"')[0].replace('amp;', '')
                        a = requests.get(f"https://mbasic.facebook.com{haha2}", headers=headersfb, timeout=10)
                    except:
                        pass

                    h = {'id':uid, 
                     'loaicx':loai}
                    nhantien = requests.post('https://traodoisub.com/scr/nhantiencx.php', cookies=cookies, data=h, timeout=10)
                    if nhantien.text == '2':
                        xu += 400
                        print(f"[+] {user}-> [{loai}]-> Success ID {uid} -> +400 xu -> {xu} xu")
                    else:
                        print(f"[+] {user}-> [{loai}]-> Fail ID {uid}")
                    dem += 1
                    sleep(delaycx)
                else:
                    break


    def page():
        global xu
        dem = 0
        response = requests.get(f"https://traodoisub.com/scr/api_job.php?chucnang=likepage&user={user}")
        try:
            data = response.json()
            so_nv = len(data)
            if so_nv > 0:
                print(f"[+] {user}-> {idfb} da tim thay {so_nv} nhiem vu!")
            else:
                print(f"[+] {user}-> {idfb} het nhiem vu page! Chuyen sang ID khac")
        except:
            print(f"[+] {user}-> Sever dang gap su co, se chay lai sau 30s!!")
            sleep(30)
            page()
        else:
            for uid in data:
                if dem < nhiemvuvong:
                    headersfb = {'authority':'mbasic.facebook.com',  'cache-control':'max-age=0', 
                     'upgrade-insecure-requests':'1', 
                     'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Mobile Safari/537.36', 
                     'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
                     'sec-fetch-site':'none', 
                     'sec-fetch-mode':'navigate', 
                     'sec-fetch-user':'?1', 
                     'sec-fetch-dest':'document', 
                     'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5', 
                     'cookie':cookie_fbs}
                    rr = requests.get(f"https://mbasic.facebook.com/{uid}", headers=headersfb, timeout=10)
                    url = rr.url
                    response = requests.get(url, headers=headersfb, timeout=10)
                    check_login = response.text.find('https://mbasic.facebook.com/login.php')
                    if check_login > 0:
                        print(f"[+] {user}-> {idfb} cookie die!")
                        break
                    else:
                        try:
                            get = response.text.split('pageSuggestionsOnLiking=1&amp;gfid=')[1].split('&amp;refid=')[0]
                        except:
                            get = ''

                        requests.get(f"https://mbasic.facebook.com/a/profile.php?fan&id={uid}&origin=page_profile&pageSuggestionsOnLiking=1&gfid={get}&refid=17", headers=headersfb, timeout=15)
                        x = requests.get(url, headers=headersfb, timeout=10)
                        check_block = x.text.find('/a/profile.php?unfan')
                        check_die = x.text.find('{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}')
                        if check_block < 0:
                            if check_die < 0:
                                print(f"[+] {user}-> {idfb} bị block!")
                                break
                        else:
                            data = {'id': uid}
                            nhantien = requests.post('https://traodoisub.com/scr/nhantienpage.php', cookies=cookies, data=data, timeout=10)
                            if nhantien.text == '2':
                                xu += 600
                                print(f"[+] {user}-> [PAGE]-> Success ID {uid} -> +600 xu -> {xu} xu")
                            else:
                                print(f"[+] {user}-> [PAGE]-> Fail ID {uid}")
                        dem += 1
                        sleep(delaypage)
                else:
                    break


    def cmt():
        global xu
        dem = 0
        response = requests.get(f"https://traodoisub.com/scr/api_job.php?chucnang=cmt&user={user}")
        try:
            data = response.json()
            so_nv = len(data)
            if so_nv > 0:
                print(f"[+] {user}-> {idfb} da tim thay {so_nv} nhiem vu!")
            else:
                print(f"[+] {user}-> {idfb} het nhiem vu comment! Chuyen sang ID khac")
        except:
            print(f"[+] {user}-> Sever dang gap su co, se chay lai sau 30s!!")
            sleep(30)
            cmt()
        else:
            for xxx in data:
                if dem < nhiemvuvong:
                    uid = xxx['id']
                    msg = xxx['nd']
                    r = requests.post(f"https://graph.facebook.com/{uid}/comments", data={'access_token':access_token,  'message':msg})
                    if 'id' in r.json():
                        data = {'id': uid}
                        nhantien = requests.post('https://traodoisub.com/scr/nhantiencmt.php', cookies=cookies, data=data, timeout=10)
                        if nhantien.text == '2':
                            xu += 800
                            print(f"[+] {user}-> [CMT]-> Success ID {uid} -> +800 xu -> {xu} xu")
                    else:
                        try:
                            if r.json()['error']['code'] == 368:
                                print(f"ID {idfb} da bi block chuyen ID khac")
                                break
                        except:
                            requests.post('https://traodoisub.com/scr/nhantiencmt.php', cookies=cookies, data={'id': uid})
                            print(f"[+] {user}-> [CMT]-> Comment Fail ID {uid}")

                    dem += 1
                    sleep(delaycmt)
                else:
                    break


    def follow():
        global xu
        dem = 0
        response = requests.get(f"https://traodoisub.com/scr/api_job.php?chucnang=follow&user={user}")
        try:
            data = response.json()
            so_nv = len(data)
            if so_nv > 0:
                print(f"[+] {user}-> {idfb} da tim thay {so_nv} nhiem vu!")
            else:
                print(f"[+] {user}-> {idfb} het nhiem vu follow! Chuyen sang ID khac")
        except:
            print(f"[+] {user}-> Sever dang gap su co, se chay lai sau 30s!!")
            sleep(30)
            follow()
        else:
            for uid in data:
                if dem < nhiemvuvong:
                    r = requests.post(f"https://graph.facebook.com/{uid}/subscribers", data={'access_token': access_token})
                    if r.text == 'true':
                        nhantien = requests.post('https://traodoisub.com/scr/nhantiensub.php', cookies=cookies, data={'id': uid}, timeout=10)
                        if nhantien.text == '2':
                            xu += 600
                            print(f"[+] {user}-> [FOLLOW]-> Success ID {uid} -> +600 xu -> {xu} xu")
                    else:
                        try:
                            if r.json()['error']['code'] == 368:
                                print(f"[+] {user}-> ID {idfb} da bi block chuyen ID khac")
                                break
                        except:
                            print(f"[+] {user}-> [FOLLOW]-> Fail ID {uid}")
                            requests.post('https://traodoisub.com/scr/nhantiensub.php', cookies=cookies, data={'id': uid})

                    dem += 1
                    sleep(delaysub)
                else:
                    break


    def like():
        global xu
        dem = 0
        response = requests.get(f"https://traodoisub.com/scr/api_job.php?chucnang=like&user={user}")
        try:
            data = response.json()
            so_nv = len(data)
            if so_nv == 0:
                print(f"[+] {user}-> {idfb} het nhiem vu like! Chuyen sang ID khac")
            else:
                print(f"[+] {user}-> {idfb} da tim thay {so_nv} nhiem vu!")
        except:
            print(f"[+] {user}-> Sever dang gap su co, se chay lai sau 30s!!")
            sleep(30)
            like()
        else:
            for uid in data:
                if dem < nhiemvuvong:
                    r = requests.post(f"https://graph.facebook.com/{uid}/likes", data={'access_token': access_token})
                    if r.text == 'true':
                        nhantien = requests.post('https://traodoisub.com/scr/nhantienlike.php', cookies=cookies, data={'id': uid}, timeout=10)
                        if nhantien.text == '2':
                            xu += 300
                            print(f"[+] {user}-> [LIKE]-> Success ID {uid} -> +300 xu -> {xu} xu")
                    else:
                        try:
                            if r.json()['error']['code'] == 368:
                                print(f"[+] {user}-> ID: {idfb} da bi block chuyen ID khac")
                                break
                        except:
                            print(f"[+] {user}-> [LIKE]-> Fail ID {uid}")
                            requests.post('https://traodoisub.com/scr/nhantienlike.php', cookies=cookies, data={'id': uid})

                    dem += 1
                    sleep(delaylike)
                else:
                    break


    def get_token(cookie_fb):
        global access_token
        global cookie_fbs
        global idfb
        cookie_fbs = cookie_fb
        headers = {'authority':'m.facebook.com', 
         'cache-control':'max-age=0', 
         'upgrade-insecure-requests':'1', 
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36', 
         'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
         'accept-language':'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5', 
         'cookie':cookie_fbs}
        response = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed', headers=headers)
        a = response.text.find('accessToken\\":\\"')
        if a > 0:
            access_token = response.text.split('accessToken\\":\\"')[1].split('\\",\\"useLocalFilePreview')[0]
            data = {'access_token': access_token}
            r = requests.get('https://graph.facebook.com/me/', params=data)
            if 'id' in r.json():
                idfb = r.json()['id']
                setad = requests.get(f"https://traodoisub.com/scr/api_dat.php?user={user}&idfb={idfb}")
                if setad.text == '1':
                    mod = random.choice(listnv)
                    if mod == 'like':
                        like()
                    else:
                        if mod == 'page':
                            page()
                        else:
                            if mod == 'cmt':
                                cmt()
                            else:
                                if mod == 'camxuc':
                                    camxuc()
                                else:
                                    follow()
                else:
                    print(f"[+] {user}-> Cau hinh that bai ID {idfb}, chuyen nick!")
            else:
                print(f"[+] {user}-> Loi khong xac dinh!, chuyen nick")
        else:
            print(f"[+] {user}-> Cookie die, chuyen nick!")


    def login():
        global cookies
        global xu
        data = {'username':user, 
         'password':pwd}
        print(f"[+] {user}-> Dang nhap traodoisub ...")
        session = requests.session()
        login = session.post('https://traodoisub.com/scr/login.php', data=data)
        if login.status_code == 200:
            if login.json() != 1 and login.json() != '':
                cookies = session.cookies
                check_live = requests.post('https://traodoisub.com/', cookies=cookies)
                if len(check_live.text.split('<strong id="soduchinh">')) == 2:
                    xu = int(check_live.text.split('<strong id="soduchinh">')[1].split('</strong> xu</span>')[0])
                    print(f"[+] {user}-> Dang nhap thanh cong - Xu hien tai la: {xu} xu")
                    for x in range(1, vonglap + 1):
                        for fb in list_x:
                            get_token(fb)

                        if x == vonglap:
                            break
                        print(f"[+] {user}-> Bat dau vong tiep theo sau: {delayvong} giây!")
                        sleep(delayvong)

                    print(f"[+] {user}-> Done!")
            else:
                print(f"[+] {user}-> Dang nhap that bai vui long kiem tra lai tai khoan traodoisub!")
                sleep(2)
        else:
            print(f"[+] {user}-> Web dang gap su co, vui long doi tron 1 phut tool tu chay lai!")
            sleep(60)
            login()


    if len(listnv) == 0:
        print('Chua chon nhiem vu nao, vui long xoa file cauhinh.ini va cai lai!')
        sleep(2)
        exit()
    else:
        if len(list_x) == 0:
            print('Vui long them cookie!')
            sleep(2)
            exit()
        else:
            login()