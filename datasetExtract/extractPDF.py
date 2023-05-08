import requests
import json

# Makes the API call to extract json data from the given PDF file
def makeRequest(pdf_name, pdf_path):
    headers = {}
    url = "http://localhost:8060/service/annotateDatasetPDF"
    payload = {'disambiguate': '1'}

    files=[
    ('input',(pdf_name,open(pdf_path,'rb'),'application/pdf'))
    ]

    response = requests.post(url, headers=headers, data=payload, files=files)
    json_data = json.loads(response.text)
    
    return json_data

# Extracts only the names of dataset found in the given PDF file
def extractNamesFromPDF(pdf_name, pdf_path): 
    
    json_data = makeRequest(pdf_name, pdf_path)
    
    if len(json_data['mentions']) > 0:
        print('The dataset names extracted from the PDF are: \n')
        dataset_names = []
        for data in json_data['mentions']:
            for key,value in data.items():
                if key=="rawForm" and value not in dataset_names: # Removing duplicate dataset names
                    if(key == "rawForm"):
                        print(value)
                        dataset_names.append(value)
    else:
        print('No dataset name was found in the PDF.')
        

# Extracts the datase name, the normalized name and the dataset context from PDF
def extractNameAndContextFromPDF(pdf_name, pdf_path):
    
    json_data = makeRequest(pdf_name, pdf_path)
    
    if len(json_data['mentions']) > 0:
        print('The dataset names and their context extracted from the PDF are: \n')
        for data in json_data['mentions']:
            for key,value in data.items():
                if(key == "rawForm"):
                    print(f"Raw dataset name: {value}")
                if(key == "dataset-name"):
                    print(f"Normalized dataset name: {value['normalizedForm']}")
                if(key == "context"):
                    print(f'The context from which the dataset name was extracted: {value}\n')
    else:
        print('No dataset name was found in the PDF.')