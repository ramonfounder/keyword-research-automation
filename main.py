# AIzaSyCU9Moka_iwFD7e4CmgxkckGUJ4twNvo-c
# 51d0cfd99085549ab

import json
from googleapiclient.discovery import build


def custom_search(query, api_key, cse_id, location, language, page, size):
    service = build("customsearch", "v1", developerKey=api_key)
    start_index = (page - 1) * size + 1  # Calculate the start index for the given page

    res = service.cse().list(
        q=query,
        cx=cse_id,
        gl=location,
        lr='lang_' + language,
        start=start_index,
        num=size
    ).execute()

    return res


def main():
    api_key = "AIzaSyCU9Moka_iwFD7e4CmgxkckGUJ4twNvo-c"
    cse_id = "51d0cfd99085549ab"
    query = "coffee"
    location = "AE"  # UAE country code
    language = "en"  # English language
    page = 1
    size = 10

    results = custom_search(query, api_key, cse_id, location, language, page, size)

    # Save the response to a JSON file
    with open('search_results.json', 'w') as json_file:
        json.dump(results, json_file, indent=4)


if __name__ == "__main__":
    main()
