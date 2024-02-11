import requests
import json

web = 'https://www.youtube.com/'
result = requests.get(web)
print(result)
print('Код ответа от сервера', result.status_code)


main_url = f'{web}page_id/'
result = requests.post(main_url,data={'name':'Musia','breed':'silan','age':'20'})
print(result)