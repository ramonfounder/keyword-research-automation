import requests
import json

def google_search(api_key, cse_id, query, language, location, page, size):
    url = "https://www.googleapis.com/customsearch/v1"
    start_index = (page - 1) * size + 1

    params = {
        "key": api_key,
        "cx": cse_id,
        "q": query,
        "lr": "lang_" + language,
        "gl": location,
        "start": start_index,
        "num": size
    }

    response = requests.get(url, params=params)
    return response.json()

def read_keywords_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Example usage
api_key = "YOUR_API_KEY"
cse_id = "YOUR_CUSTOM_SEARCH_ENGINE_ID"
language = "en"
location = "AE"  # UAE country code
page = 1
size = 10
file_path = 'keywords.txt'

keywords = read_keywords_from_file(file_path)
all_search_results = []

for keyword in keywords:
    search_results = google_search(api_key, cse_id, keyword, language, location, page, size)
    all_search_results.append({keyword: search_results})

# Save all results to a JSON file
with open('all_search_results.json', 'w') as json_file:
    json.dump(all_search_results, json_file, indent=4)
