from flask import Flask, render_template,redirect, request
import http.client
import json,requests

app = Flask('__name__')

#
# connection = http.client.HTTPConnection('api.football-data.org')
# headers = { 'X-Auth-Token': '6f89e625709d4b11af33273c70007ae9','X-Response-Control': 'minified' }
# connection.request('GET', '/v1/competitions/455/fixtures', None, headers )
#
# response= json.loads(connection.getresponse().read().decode())
#
# print(response['fixtures'])
#
# for x in response['fixtures']:
#     print(x)
#     # h = x['result']['goalsHomeTeam']
#     # v = x['result']['goalsAwayTeam']
#     # if h and v is not None:
#     #     print('goles en casa', h ,'Goles equipo Visitante',v)
# #for x in response['fixtures']:
#  #   h = x['result']['goalsHomeTeam']
#   #  v = x['result']['goalsAwayTeam']
#    # if h and v is not None:
#     #    print('goles en casa', h ,'Goles equipo Visitante',v)
#
# for x  in response['fixtures']:
#     b = x['homeTeamName']
#     c = x['awayTeamName']
#     h = x['result']['goalsHomeTeam']
#     a = x['result']['goalsAwayTeam']
#     if h and a is not None:
#         print(b, h,'VS',c,a)
#
#
@app.route('/',methods = ['GET'])
def init():

 connection = http.client.HTTPConnection('api.football-data.org')
 headers = {'X-Auth-Token': '6f89e625709d4b11af33273c70007ae9','X-Response-Control': 'minified'}
 connection.request('GET', '/v1/competitions/464/teams', None, headers)
 response = json.loads(connection.getresponse().read().decode())
 if request.method == 'GET':
  try:
 #print(response)
  #for x in response['teams']:
    return render_template('ejemplo.html', response=response['teams'])
   # for x in response['players']:
    #    print(x['name'],x['position'],x['jerseyNumber'],x['dateOfBirth'],x['nationality'],x['nationality'],
#          x['contractUntil'],x['marketValue'])
    # return render_template('loq.html', response=response['fixtures'])
  except Exception as e:
    print(e)
 return render_template('ejemplo.html')
if __name__ == '__main__':
    app.run()


