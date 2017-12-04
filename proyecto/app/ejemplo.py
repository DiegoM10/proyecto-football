import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '6f89e625709d4b11af33273c70007ae9','X-Response-Control': 'minified' }
connection.request('GET', '/v1/competitions/455/fixtures', None, headers )

response= json.loads(connection.getresponse().read().decode())

print(response['fixtures'])

for x in response['fixtures']:
    print(x)
    # h = x['result']['goalsHomeTeam']
    # v = x['result']['goalsAwayTeam']
    # if h and v is not None:
    #     print('goles en casa', h ,'Goles equipo Visitante',v)
