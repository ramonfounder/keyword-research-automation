import requests
import json


def get_keyword_suggestions(api_key, query, language):
    url = "https://api.keywordtool.io/v2/search/keywords"
    params = {
        "apikey": api_key,
        "keyword": query,
        "country": "AE",  # Country code for the United Arab Emirates (Dubai)
        "language": language  # Language code, e.g., "en" for English
    }

    response = requests.get(url, params=params)
    return response.json()


def read_keywords_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


# Example usage
api_key = "YOUR_API_KEY"
language = "en"
file_path = 'keywords.txt'

keywords = read_keywords_from_file(file_path)
all_suggestions = []

for keyword in keywords:
    response = get_keyword_suggestions(api_key, keyword, language)
    all_suggestions.append({keyword: response})

# Save the results to a JSON file
with open('all_keyword_suggestions.json', 'w') as json_file:
    json.dump(all_suggestions, json_file, indent=4)
