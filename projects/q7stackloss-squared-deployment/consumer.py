"""
A python application that post data to the Stackloss model API endpoint at http://0.0.0.0:8000/predict
""" 
import requests
import json
import os

def post_to_api(data: dict):
    # url is stored in an environment variable
    url = os.environ.get('API_URL', 'http://0.0.0.0:8000/predict')
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

if __name__ == "__main__":
    x = [
        [2, 3, 4, 9, 16],
        [4, 5, 6, 25, 36],
        [62, 22, 87, 484, 7569]
    ]    
    for record in x:
        # split into individual lists
        # Create the request body in the format the API expects
        data = {"X": record}
        print(f"Sending data: {data}")

        response = post_to_api(data)
        print(response)