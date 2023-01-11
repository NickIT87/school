import requests
import json


api_response = requests.get('https://jsonplaceholder.typicode.com/todos')

print(api_response.status_code)

data = api_response.text
parse_json = json.loads(data)

print(type(parse_json))
print(type(parse_json[0]))