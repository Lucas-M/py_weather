import requests
import ast

#45, -86
api_key = 'a2e355d69eaf597d26769c083d777d99'

# this is a good example using zipcode
#url = 'http://api.openweathermap.org/data/2.5/weather?zip=49684,us&APPID=' + api_key

# this is good example using city id
#url = 'http://api.openweathermap.org/data/2.5/weather?id=5012495&APPID=' + api_key

# using forcast for city
#url = 'http://api.openweathermap.org/data/2.5/forecast/city?id=5012495`&APPID=' + api_key

url = 'http://api.openweathermap.org/data/2.5/forecast/city?id=5012495`&APPID=' + api_key


r = requests.get(url)
#print(r.status_code)
#print(r.headers['content-type'])
#print(r.text)

cc = ast.literal_eval(r.text)

print('\n\n\nThe weather forcast for: ' + cc['city']['name'])
#print('\nConditions will be: ' + cc['list'][0]['weather']['description'])
print('\nConditions will be: ' + str(cc['list'][0]['weather'][0]['description']))



