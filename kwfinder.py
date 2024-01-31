import requests
import json

def get_related_keywords(api_key, query, location_id, language_id):
    url = 'https://api.mangools.com/v3/kwfinder/related-keywords'
    headers = {'X-access-Token': api_key}
    params = {'kw': query, 'location_id': location_id, 'language_id': language_id}

    response = requests.get(url, headers=headers, params=params)
    return response.json()

def read_keywords_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Example usage
api_key = 'YOUR_API_KEY'
location_id = 0  # Adjust as per your requirement
language_id = 0  # Adjust as per your requirement
file_path = 'keywords.txt'

keywords = read_keywords_from_file(file_path)
all_related_keywords = []

for keyword in keywords:
    response = get_related_keywords(api_key, keyword, location_id, language_id)
    all_related_keywords.append({keyword: response})

# Save the results to a JSON file
with open('all_related_keywords.json', 'w') as json_file:
    json.dump(all_related_keywords, json_file, indent=4)
