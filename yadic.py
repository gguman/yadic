#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json, platform, os, re
'''
    yep
'''


# Получить токен можно по этой ссылке: https://translate.yandex.ru/developers/keys
# Проверить количество переведенных символов в Статистике: https://translate.yandex.ru/developers/stat

with open('token.txt', 'r') as t: token = t.read()

def translate(eng_text):
    
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    _url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    _options = {'key':token, 'lang':'en-ru', 'text':eng_text}
    _req = requests.get(_url, params=_options, verify=False)
    _result = json.loads(_req.content)
    if _result.get('code') == 200:
        return _result.get('text')[0]
    else:
        print(f"\nError. Find the reference for code { _result.get('code')} here:\nhttps://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/") 

def grab_text():
    '''
    documentation must be 
        here in the future...
    '''

    print('\nWellcome to our online dictionary!\nref: input (t)ext. catch (r)esult. eeasy')
    _cl = 'clear' if platform.system() == 'Linux' else 'cls'
    _cnt = 1
    while True:
        _text = input(f'\n[{_cnt}] t: ' )
        if re.search('\w', _text):
            if re.search('^!', _text):
                if re.search('exit', _text): exit()
                if re.search('clear', _text): _clear = lambda: os.system(_cl); _clear(); _cnt -= 1
                if re.search('help', _text): print(grab_text.__doc__); _cnt -= 1
            else:
                _result = translate(_text)
                print(f"[{_cnt}] r: {_result}")
                
            _cnt += 1


if __name__ == '__main__':
    grab_text()
