import requests
import json

# Extract dataset names and wikipedia ID (if available) from the input text
def extractFromSentence(text):
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        }

    url = 'http://localhost:8060/service/annotateDatasetSentence'
    payload = f'text={text}'

    response = requests.post(url, headers=headers, data=payload)
    
    json_data = json.loads(response.text)

    if len(json_data['mentions']) > 0:
    
        for key,value in json_data["mentions"][0].items():
            if(key == "rawForm"):
                print(f"\nThe raw value of the dataset name extracted is: {value}")
            if(key == "dataset-name"):
                print(f"Normalized dataset name: {value['normalizedForm']}")
                if('wikidataId' in value.keys() and 'wikipediaExternalRef' in value.keys()):
                    print(f"Wikidata ID: {value['wikidataId']}\nWikiExternal Reference: {value['wikipediaExternalRef']}")
            if(key == "context"):
                print(f'The context from which the dataset name was extracted: {value}\n')
    else:
        print('No dataset name was found in the sentence.')
    return response