import requests
import csv
from sws_Login import tokens
f = open('client_userid.csv', 'w', encoding='utf-8', newline='')
writer = csv.DictWriter(f,fieldnames= ['userID'])
writer.writeheader()
cookies = {
    '_ga': 'GA1.1.516967780.1752903886',
    '_ga_VT7LK3LSPQ': 'GS2.1.s1753520345$o3$g1$t1753520599$j60$l0$h0',
    '__cf_bm': 'xzfUCkGaAS2FI.5wZZ2k4lz_IZaVln8FEWt5hOO6.ms-1754062315-1.0.1.1-x17jTQJVvrvZYGu8vzgPoM5WPqf8QcTvK.l1RU7tHKPebC8jnl9crtu1nxOO5SBYmkJfH7jnnWyE44i3BY4zHCr_2sYfBSmawEV7zEaUPu0',
    'swsToken': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJsZW93YW5nIiwiaWF0IjoxNzU0MDYyNjQ2LCJleHAiOjE3NTQwNjQ0NDZ9.OMGOFna-wMaUAWjm_l-L9TWZxwP5YMeaO65yU_KUxpFl6FOlF-14vA9dbMfNfY2UImSijiSQuw2bVZbwxSyHRA',
    'swsRefreshToken': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJsZW93YW5nIiwiaWF0IjoxNzU0MDYyNjQ2LCJleHAiOjE3NTQ2Njc0NDZ9.YCdiJWy9AEIcqRQtHUG0N-7UeI5FTiTrku13KwZMqbh8RojTPPeBU9NeTc3OTWRcHdnkFqSkbM3MjDagl2nLag',
    '_ga_HMZF9KNBFD': 'GS2.1.s1754062301$o5$g1$t1754062655$j45$l0$h0',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,zh-HK;q=0.8',
    'authorization': 'Bearer ' + tokens,
    'branchversion': 'release',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'language': 'en',
    'origin': 'https://sws-core-au.crm-alpha.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://sws-core-au.crm-alpha.com/clientsV2',
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
    # 'cookie': '_ga=GA1.1.516967780.1752903886; _ga_VT7LK3LSPQ=GS2.1.s1753520345$o3$g1$t1753520599$j60$l0$h0; __cf_bm=xzfUCkGaAS2FI.5wZZ2k4lz_IZaVln8FEWt5hOO6.ms-1754062315-1.0.1.1-x17jTQJVvrvZYGu8vzgPoM5WPqf8QcTvK.l1RU7tHKPebC8jnl9crtu1nxOO5SBYmkJfH7jnnWyE44i3BY4zHCr_2sYfBSmawEV7zEaUPu0; swsToken=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJsZW93YW5nIiwiaWF0IjoxNzU0MDYyNjQ2LCJleHAiOjE3NTQwNjQ0NDZ9.OMGOFna-wMaUAWjm_l-L9TWZxwP5YMeaO65yU_KUxpFl6FOlF-14vA9dbMfNfY2UImSijiSQuw2bVZbwxSyHRA; swsRefreshToken=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJsZW93YW5nIiwiaWF0IjoxNzU0MDYyNjQ2LCJleHAiOjE3NTQ2Njc0NDZ9.YCdiJWy9AEIcqRQtHUG0N-7UeI5FTiTrku13KwZMqbh8RojTPPeBU9NeTc3OTWRcHdnkFqSkbM3MjDagl2nLag; _ga_HMZF9KNBFD=GS2.1.s1754062301$o5$g1$t1754062655$j45$l0$h0',
}

json_data = {
    'dateTimeFrameEnd': '2025-08-01 23:59:59',
    'dateTimeFrameStart': '2025-08-01 00:00:00',
    'tableSettingList': [
        'userId',
        'name',
        'tradeActivityStatus',
        'depositActivityStatus',
        'resourcePool',
        'lastLoginTime',
        'regulatorId',
        'userTags',
        'isBlack',
        'sales',
        'accountOwner',
        'email',
        'mobile',
        'account',
        'country',
        'region',
        'language',
        'userType',
        'clientStatus',
        'walletStatus',
        'kycAuthenticationStr',
        'cpa',
        'cpaSales',
        'affId',
        'leadSource',
        'retailSource',
        'websiteId',
        'cxd',
        'registrationTime',
        'onboardingTestCount',
        'followUpNotesCount',
        'salesStatus',
        'clientTiers',
        'lastContactDate',
        'assignedTime',
    ],
    'pageNum': 1,
    'pageSize': 20,
    'search': True,
}

response = requests.post(
    'https://sws-core-au.crm-alpha.com/api/v2/users/management/clientList',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
# print(response.json())
for i in response.json()['data']:
    name = {
        'userID': i['userId']
    }
    writer.writerow(name)
