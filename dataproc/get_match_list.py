import json
import time
import requests
from envs.pserver.Lib.http.client import responses

API_KEY = "RGAPI-ea519fa2-ea18-4b9a-81ac-7d6d4f801e73"

HEADERS = {"X-Riot-Token": API_KEY}

STARTTIME = "1736294400"
TYPE = "ranked"
COUNT = 100

with open("puuids_over_MASTER_tier.json","r",encoding="utf-8") as f:
    puuid_data=json.load(f)

sample_puuid = puuid_data[0]['CHALLENGER'][0]
print(f'첫 번째 챌린저의 puuid : {sample_puuid}')


def get_match_list_single_100(puuid):
    base_url = "https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/"
    url = f'{base_url}{puuid}/ids?startTime={STARTTIME}&type={TYPE}&start=0&count={COUNT}'
    responses = requests.get(url,headers=HEADERS)

    if responses.status_code == 200:
        match_list = responses.json()
        return match_list
    else:
        raise Exception(f'Error : {responses.status_code}')

match_list = get_match_list_single_100(sample_puuid)
print(match_list)
print(len(match_list))

def get_match_list_from_puuid(puuid):
    base_url = "https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/"
    match_ids = []
    start_idx = 0

    while True:
        url = f'{base_url}{puuid}/ids?startTime={STARTTIME}&type={TYPE}&start=0&count={COUNT}'
        responses = requests.get(url, headers=HEADERS)

        if responses.status_code == 200:
            match_list = responses.json()
            if not match_list:
                print(f'수집이 종료되었습니다. 현재까지 수집한 match id의 수는 {len(match_ids)}입니다.')
                break
            match_ids.extend(match_list)
            start_idx += COUNT
            print(f'현재까지 {len(match_ids)}개의 match id 수집 완료')
        elif responses.status_code == 429:
            print('사용 한도를 넘어섰습니다. 10초간 대기합니다.')
            time.sleep(10)
        else:
            print(f'요청 실패 : {responses.status_code}')
            break
        time.sleep(0.1)
    return match_ids
match_ids= get_match_list_from_puuid(sample_puuid)
print(match_ids,len(match_ids))
