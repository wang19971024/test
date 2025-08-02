import requests

cookies = {
    '_ga': 'GA1.1.516967780.1752903886',
    '_ga_VT7LK3LSPQ': 'GS2.1.s1753520345$o3$g1$t1753520599$j60$l0$h0',
    '__cf_bm': 'xzfUCkGaAS2FI.5wZZ2k4lz_IZaVln8FEWt5hOO6.ms-1754062315-1.0.1.1-x17jTQJVvrvZYGu8vzgPoM5WPqf8QcTvK.l1RU7tHKPebC8jnl9crtu1nxOO5SBYmkJfH7jnnWyE44i3BY4zHCr_2sYfBSmawEV7zEaUPu0',
    'swsToken': 'null',
    'swsRefreshToken': 'null',
    '_ga_HMZF9KNBFD': 'GS2.1.s1754062301$o5$g1$t1754062319$j42$l0$h0',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8',
    'authorization': '',
    'branchversion': 'release',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'language': 'en',
    'origin': 'https://sws-core-au.crm-alpha.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://sws-core-au.crm-alpha.com/login',
    'regulator': 'vfsc2',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'tag': 'AU',
    'timezone': '8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': '_ga=GA1.1.516967780.1752903886; _ga_VT7LK3LSPQ=GS2.1.s1753520345$o3$g1$t1753520599$j60$l0$h0; __cf_bm=xzfUCkGaAS2FI.5wZZ2k4lz_IZaVln8FEWt5hOO6.ms-1754062315-1.0.1.1-x17jTQJVvrvZYGu8vzgPoM5WPqf8QcTvK.l1RU7tHKPebC8jnl9crtu1nxOO5SBYmkJfH7jnnWyE44i3BY4zHCr_2sYfBSmawEV7zEaUPu0; swsToken=null; swsRefreshToken=null; _ga_HMZF9KNBFD=GS2.1.s1754062301$o5$g1$t1754062319$j42$l0$h0',
}

json_data = {
    'userName': 'b4fea510752790e09f0ac5c621d6f134de653eb4b729ffcd1b4cba6d1bf566adf2bb3a4d3da7af139a6133b80f5c9beead7ac87291defacd0420d584bb87e8a0493b1319db64b2efaafa4d03f84e40f4b51949dfbe39458d90ae0a2e9ad3d13ff5fe718d31e279be740823d532a1b7ec0cdb7c5456fe243cb6ecee9d4ac9d27e',
    'passWord': 'a24ec0e1ba9b9073574872c6b76674e2',
}

response = requests.post(
    'https://sws-core-au.crm-alpha.com/api/v1/auth/session/login',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
tokens = response.json()['data']['accessToken']['token']
if __name__ == '__main__':

    print(tokens)