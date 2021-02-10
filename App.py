import geocoder
import requests

g = geocoder.ip('me')

# Parametrização dos dados da API
key = '8755ec76bdf154510fd657da7d6f2999'
url = 'http://api.openweathermap.org/data/2.5/weather?'
params = {
  'lat': str(g.lat),
  'lon': str(g.lng),
  'appid': key,
  'lang': 'pt',
  'units':"metric"
}

# Utilizando o metodo requests.GET da biblioteca para consumir a API
response = requests.get(url=url, params = params)
response_data = response.json()


# Exibindo os resultados
cidade = response_data['name']
tempAtual = response_data['main']['temp']
tempMax = response_data['main']['temp_max']
tempMin = response_data['main']['temp_min']
sensacaoTermica = response_data['main']['feels_like']
descricaoClima = response_data['weather'][0]['description']



print("Agora em {} fazem {}cº".format(cidade, tempAtual))
print("Maxima de {}cº e Minima de {}cº".format(tempMax, tempMin))
print("Sensação Térmica de {}cº".format(sensacaoTermica))
print(descricaoClima)


