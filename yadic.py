#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json, platform, os

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

if __name__ == '__main__':
    print('\nWellcome to our online dictionary!\nref: input (t)ext. catch (r)esult. eeasy')
    _cl = 'clear' if platform.system() == 'Linux' else 'cls'
    _cnt = 1
    while True:
        _text = input(f'\n[{_cnt}] t: ' )
        if len(_text) > 0:
            if _text == 'exit()':
                exit()
            elif _text == 'clear()':
                _clear = lambda: os.system(_cl)
                _clear()
                _cnt -= 1
            else:
                _result = translate(_text)
                print(f"[{_cnt}] r: {_result}")
            _cnt += 1
