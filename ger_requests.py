import requests
import json
web = 'https://www.youtube.com/'
result = requests.get(web)
print(result)
print('Код ответа от сервера', result.status_code)
print('Тест опыта')

main_url = f'{web}ru/feed/'
result = requests.get(web)
data = result.json()
print(data)