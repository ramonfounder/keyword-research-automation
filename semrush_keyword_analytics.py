import requests
import json

def fetch_semrush_keyword_analytics(api_key, keyword):
    url = "https://api.semrush.com"
    params = {
        "type": "phrase_this",
        "key": api_key,
        "phrase": keyword,
        "database": "us",
        "export_columns": "Ph,Nq,Cp,Co",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()  # Assuming JSON response; adjust as necessary
    else:
        print(f"Error fetching data for {keyword}: {response.status_code}")
        return None

def read_keywords_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def save_results_to_json(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

api_key = "YOUR_SEMRUSH_API_KEY"
keywords_file = "keywords.txt"
output_file = "semrush_keyword_analytics.json"

keywords = read_keywords_from_file(keywords_file)
analytics_results = []

for keyword in keywords:
    analytics = fetch_semrush_keyword_analytics(api_key, keyword)
    if analytics:
        analytics_results.append({keyword: analytics})

save_results_to_json(output_file, analytics_results)
