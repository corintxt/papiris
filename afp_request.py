import requests
import json
import time

from config import call_id, headercode, f_url, e_url

def generate_transaction_id(id):
    timestamp = time.strftime("%Y%m%d%H%M%S")
    return f"{id}-{timestamp}"

def retrieve_filter_definition(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve the filter definition.")
        print("Status code:", response.status_code)
        print("Response content:", response.text)
        return None

def execute_filter(url, params, body, headers):
    response = requests.post(url, params=params, json=body, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to execute the filter.")
        print("Status code:", response.status_code)
        print("Response content:", response.text)
        return None

def call_iris():    
    # Create the unique transaction ID
    transaction_id = generate_transaction_id(call_id)
    
    # Set the headers with the transaction ID
    headers = {
        headercode: transaction_id
    }
    
    # Step 1: Retrieve the filter definition
    filter_url = f_url
    filter_definition = retrieve_filter_definition(filter_url, headers)
    
    if filter_definition is not None:
        print("Filter definition retrieved successfully.")
        
        # Step 2: Execute the filter
        execution_url = e_url
        params = {
            "max": 100,
            "start": 0
        }
        body = filter_definition
        
        filter_results = execute_filter(execution_url, params, body, headers)
        
        if filter_results is not None:
            print("Filter executed successfully.")
            # print("Results:", filter_results)
            return filter_results

if __name__ == "__main__":
    call_iris()