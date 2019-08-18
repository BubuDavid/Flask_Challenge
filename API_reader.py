import requests
from pprint import pprint
import json

def get_prediction(url, filename, LS, AS, LP, AP):
    """
    Download JSON response url for prediction.
    """

    # Set metadata:
    headers = {'Content-type': 'application/json'}
    input_values = {
        'sepal_length': LS,
        'sepal_width': AS,
        'petal_length': LP,
        'petal_width': AP
    }

    # Get response:
    response = requests.post(url, headers = headers, json = input_values)

    # If response's status is 200:
    if response.status_code == requests.codes.ok:
        # Pretty print response:
        pprint(response.json())
        
    return response.json()