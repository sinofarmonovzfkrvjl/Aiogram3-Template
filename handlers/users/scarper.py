
import requests

def detect_alphabet(text):
    latin_alphabet = set("qertyuiopasdfghjklzxcvbnmo'g'chsho‘g‘")
    cyrillic_alphabet = set("қертюиопасдфгҳжклзcвбнмўғчшнг")

    text_lower = text.lower()

    contains_latin = any(char in latin_alphabet for char in text_lower)
    contains_cyrillic = any(char in cyrillic_alphabet for char in text_lower)

    if contains_latin and contains_cyrillic:
        return "Lotin va Krill"
    elif contains_latin:
        return "Lotin"
    elif contains_cyrillic:
        return "Krill"
    else:
        return "Mix"



def translate_text(mod,text):
    url = 'https://lotin.uz/api/translate'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uz;q=0.6',
        'Content-Type': 'application/json',
        'Cookie': 'XSRF-TOKEN=eyJpdiI6IlZ6V0RTSGtLbmN2QmdNUm1DeHIwWnc9PSIsInZhbHVlIjoiUjZNbUdtZFZ2c29Fa1hocVYzUk5IRXBudWVKSUVnVHlzSDNRdyt3OElBNXR0dnc3MzVXZjg1aWtVV2xlRXNJbTdRR3ZTTm1qRFFwdko2TzUwNVN1MW9XSlI4dTRLeVZxR0x1WWdCbnZsY1AxSWxhMU1HV3ZKeEJFdllMZkpQZ0giLCJtYWMiOiJlYzBmY2QyNDRjMWY1MmMzYjJkNmE5NDA5MDdiYmRjNTgzYjk1YWMyMWM2ZTg4NzNlNGEwYjczZGNiYmFkNWYzIiwidGFnIjoiIn0%3D; lotinuz_session=eyJpdiI6IkdRVGRJTnp3NGdNY2F2dnBkcEF1Z3c9PSIsInZhbHVlIjoiQXVEZklyQldoa3U1aDQrWDltS1NjM3krYmJ4UEZNa0xTNTRsTU1QK09VU0FRY3NqUm4reUo4Z1ZSOHc4b1NsQXhrdFZYb3IxMUw4VGVjM3gwODZEczFuOUpKYTRuZVJEeFZSWERwUlpzRXhRWEhNYVJxb1FtZ0pFME9rL25ZV3YiLCJtYWMiOiIyMGViNDY2NWVkY2QwMWVmOTVjOTczZmU0MzhkZjljMjVhNjBiNjY2ZmQ4YmNiNTE5ZGNiZmFlMzhhNGIyNTkxIiwidGFnIjoiIn0%3D; _gid=GA1.2.1218229874.1690621112; _ym_uid=1690621112421339497; _ym_d=1690621112; _ym_isad=2; _ga_ZPE569JKST=GS1.1.1690621112.1.0.1690621112.0.0.0; _ga=GA1.1.839919468.1690621112; _ym_visorc=w; lotin_promo_expiration=1; lotin_promo=8',
        'Origin': 'https://lotin.uz',
        'Referer': 'https://lotin.uz/',
        'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'X-Csrf-Token': 'laTWDvk9z8IX3vAcU9Eo1nj8Mo2rfmrY8yriqEee',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Xsrf-Token': 'eyJpdiI6IlZ6V0RTSGtLbmN2QmdNUm1DeHIwWnc9PSIsInZhbHVlIjoiUjZNbUdtZFZ2c29Fa1hocVYzUk5IRXBudWVKSUVnVHlzSDNRdyt3OElBNXR0dnc3MzVXZjg1aWtVV2xlRXNJbTdRR3ZTTm1qRFFwdko2TzUwNVN1MW9XSlI4dTRLeVZxR0x1WWdCbnZsY1AxSWxhMU1HV3ZKeEJFdllMZkpQZ0giLCJtYWMiOiJlYzBmY2QyNDRjMWY1MmMzYjJkNmE5NDA5MDdiYmRjNTgzYjk1YWMyMWM2ZTg4NzNlNGEwYjczZGNiYmFkNWYzIiwidGFnIjoiIn0='
    }

#cyrtolat
    data = {
        'mod': mod,
        'text': text,
        'ignoreHtml': True
    }
    resposne = requests.post(url, headers=headers, json=data)
    print(resposne.json())
    if resposne.status_code == 200:
        return resposne.json()
    else:
        print(f"Xato yuz berdi! Status kodi: {resposne.status_code}")
        return None


