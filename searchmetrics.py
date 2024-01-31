import json

import requests
from urllib.parse import urlencode, urljoin

API_KEY = "xxxxx"
API_SECRET = "xxxxx"
BASE_URL = 'http://api.searchmetrics.com/v3/'

def get_access_token(api_key, api_secret):
    token_url = urljoin(BASE_URL, 'token')
    data = {'grant_type': 'client_credentials'}
    response = requests.post(token_url, data=data, auth=(api_key, api_secret)).json()
    return response.get('access_token')

def fetch_keyword_info(access_token, keyword, countrycode='us'):
    endpoint = 'ResearchKeywordsGetListKeywordinfo.json/'
    params = {'countrycode': countrycode, 'keyword': keyword, 'access_token': access_token}
    query_string = urlencode(params)
    request_url = urljoin(BASE_URL, endpoint) + "?" + query_string
    response = requests.get(request_url)
    return response.json()

def read_keywords_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def save_results_to_json(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage
keywords_file = 'keywords.txt'
output_file = 'keyword_data.json'
access_token = get_access_token(API_KEY, API_SECRET)

if access_token:
    keywords = read_keywords_from_file(keywords_file)
    all_keyword_data = {}
    for keyword in keywords:
        all_keyword_data[keyword] = fetch_keyword_info(access_token, keyword)
    save_results_to_json(output_file, all_keyword_data)
else:
    print("Failed to obtain access token.")
