import re
import threading

import requests

import module

PROXY_POOL = module.apis.proxies.ProxyPool('gold')
GOOGLEKEY = '6LdTY9MjAAAAAOPrsEq42QB0zIRujU7tM-hVqxki'
PAGEURL = 'https://dataforest.hurma.work/public-vacancies/12'


def get_index(session: requests.Session):
    headers = {
        'authority': 'dataforest.hurma.work',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    response = session.get('https://dataforest.hurma.work/public-vacancies/12', headers=headers)
    return response


def get_api(session, csrf_token: str = None):
    xsrf_token = session.cookies.get_dict().get('XSRF-TOKEN')
    headers = {
        'authority': 'dataforest.hurma.work',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'referer': 'https://dataforest.hurma.work/public-vacancies/12',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'x-csrf-token': csrf_token,
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': xsrf_token,
    }

    response = session.get('https://dataforest.hurma.work/api/v1/public-vacancies/12', headers=headers)
    return response


def post(session, captcha_answer: str, csrf_token: str | None = None):
    xsrf_token = session.cookies.get_dict().get('XSRF-TOKEN')
    headers = {
        'authority': 'dataforest.hurma.work',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryzAA70EnoU5pGuM3F',
        'origin': 'https://dataforest.hurma.work',
        'referer': 'https://dataforest.hurma.work/public-vacancies/12',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'x-csrf-token': csrf_token,
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': xsrf_token,
    }
    data = '------WebKitFormBoundaryzAA70EnoU5pGuM3F\r\nContent-Disposition: form-data; name="name"\r\n\r\ncontact me https://t.me/adw3r\r\n------WebKitFormBoundaryzAA70EnoU5pGuM3F\r\nContent-Disposition: form-data; name="emails[]"\r\n\r\nwezxasqw@gmail.com\r\n------WebKitFormBoundaryzAA70EnoU5pGuM3F\r\nContent-Disposition: form-data; name="phones[]"\r\n\r\n1231231234\r\n------WebKitFormBoundaryzAA70EnoU5pGuM3F\r\nContent-Disposition: form-data; name="additional_info"\r\n\r\nhttps://t.me/adw3r contact me\r\n------WebKitFormBoundaryzAA70EnoU5pGuM3F\r\nContent-Disposition: form-data; name="g_recaptcha_response"\r\n\r\ncap_field\r\n------WebKitFormBoundaryzAA70EnoU5pGuM3F--\r\n'
    data = data.replace('cap_field', captcha_answer)
    response = session.post('https://dataforest.hurma.work/api/v1/public-vacancies/12', headers=headers, data=data)
    return response


def main():
    session = requests.Session()
    proxy = PROXY_POOL.pop()
    session.proxies = {'http': proxy, 'https': proxy}
    get_index_response = get_index(session)
    csrf_token_pattern = re.compile(r'(?<=<meta name="_token" content=")\w+(?=">)')
    csrf_token = csrf_token_pattern.search(get_index_response.text)
    if not csrf_token:
        print('error')
        return False
    # get_api(session, csrf_token.group())
    cap = module.CapMonsterSolver.solve(GOOGLEKEY, PAGEURL, version='v3')
    if not cap:
        print('error with captcha occured')
        return False
    post_response = post(session, captcha_answer=cap, csrf_token=csrf_token.group())
    print(post_response.text)
    return True


def threaded_main():
    while True:
        threads = []
        for _ in range(100):
            t = threading.Thread(target=main)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()


if __name__ == '__main__':
    res = main()
    # if res:
    #     threaded_main()
