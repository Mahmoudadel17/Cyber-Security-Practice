import requests
import json

# base url 
url = "https://fakestoreapi.com/auth/login"


# request body
data = {
 'username': "mor_2314",
 'password': "83r5^_"
}


response = requests.post(url = url, json = data)

if response.status_code == 200:
    print(json.dumps(response.json(),indent = 4))
   

