import requests

#url = 'http://ES_search_demo.com/document/record/_search?pretty=true'
#data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'
#response = requests.get(url, data=data)

api_key = 'a2e355d69eaf597d26769c083d777d99'
url = 'http://api.openweathermap.org/data/2.5/forecast/city?id=524901&APPID=' + api_key
r = requests.get(url)
print(r.status_code)
print(r.headers['content-type'])
print(r.text)

#http://api.openweathermap.org/data/2.5/forecast/city?id=524901&APPID=a2e355d69eaf597d26769c083d777d99










'''
import pyowm

api_key = pyowm.OWM('a2e355d69eaf597d26769c083d777d99')



obervation = owm.weather_at_place("Cambridge, uk")

w = observation.get_weather()

wind = w.get_wind()

print(w)
print(wind)
'''

