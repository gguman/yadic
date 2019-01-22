#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json, platform, os, re


def translate(eng_text, direction):
    try:
        with open('.token', 'r') as t: token = t.read()
    
        requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
        _url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        _options = {'key':token, 'lang':direction, 'text':eng_text}
        _req = requests.get(_url, params=_options, verify=False)
        _result = json.loads(_req.content)
        if _result.get('code') == 200:
            return _result.get('text')[0]
        else:
            print(f"\nError. Find the reference for code { _result.get('code')} here:\nhttps://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/") 
    
    except FileNotFoundError:
        print('''\tYou need to get a token from Yandex: https://translate.yandex.ru/developers/keys\n\tand put it to .token file''')
        with open('.token', 'w') as f: f.write('#replace this line with your token')
    
    
def grab_text():
    '''
    To get token follow the link: https://translate.yandex.ru/developers/keys
    To get stats: https://translate.yandex.ru/developers/stat
    '''

    print('\nWellcome to our online dictionary!\nref: input (t)ext. catch (r)esult. eeasy')
    _cl = 'clear' if platform.system() == 'Linux' else 'cls'
    _direct = 'en-ru'
    _cnt = 1
    while True:
        _text = input(f'\n[{_cnt}] t: ' )
        if re.search('\w', _text):
            if re.search('^!', _text):
                if re.search('exit', _text): exit()
                if re.search('clear', _text): _clear = lambda: os.system(_cl); _clear(); _cnt -= 1
                if re.search('direct', _text): _direct = input('Input new direction (format \'en-ru\'): ')
                if re.search('help', _text): print(grab_text.__doc__); _cnt -= 1
            else:
                _result = translate(_text, _direct)
                if _result:
                    print(f"[{_cnt}] r: {_result}")
                    _cnt += 1
    time.sleep(1)
    
if __name__ == '__main__':
    grab_text()
