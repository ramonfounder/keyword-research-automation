from serpapi import GoogleSearch
import json

def fetch_keyword_data(api_key, keyword, location, language):
    params = {
        "engine": "google",
        "q": keyword,
        "api_key": api_key,
        "location": location,
        "hl": language
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results

def read_keywords_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def save_results_to_json(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

api_key = 'YOUR_SERPAPI_KEY'
keywords_file = 'keywords.txt'
output_file = 'serpapi_results.json'
location = "Dallas, TX, USA"
language = "en"

keywords = read_keywords_from_file(keywords_file)
results = {keyword: fetch_keyword_data(api_key, keyword, location, language) for keyword in keywords}
save_results_to_json(output_file, results)
