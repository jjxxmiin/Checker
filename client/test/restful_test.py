import datetime
import requests

URL = 'http://210.115.229.133:5170/user'

now = datetime.datetime.now()
now_timestamp = now.timestamp()

param = {'timestamp': now_timestamp,'code': "M195220", 'location': 1}

response = requests.get(URL, param)

print(response.text)
