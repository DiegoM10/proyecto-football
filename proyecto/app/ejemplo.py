import http.client
import json


connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '6f89e625709d4b11af33273c70007ae9 ', 'X-Response-Control': 'minified' }
connection.request('GET', '/v1/competitions', None, headers )
#connection.request('GET', '/v1/teams/524', None, headers )
response = json.loads(connection.getresponse().read().decode())
#respuesta = json.loads(connection.getresponse().read().decode())
#print (response)
#print(respuesta)
for x in response:
    print(x["id"],x["caption"],x["league"],x["year"],x["currentMatchday"],x["numberOfMatchdays"],x["numberOfTeams"],
          x["numberOfGames"],x["lastUpdated"])












#import requests
import json
#from soccer import exceptions, leagueids, teamnames, writers
#if __name__ =='__main__':

#SOCCER_CLI_API_TOKEN= '6f89e625709d4b11af33273c70007ae9 '
#team =
#print(team)
 #url = 'http://api.football-data.org/v1/competitions/?season=2017'
# url= "http://api.football-data.org/v1/competitions/444/leagueTable"
#url = 'http://soccer.sportsopendata.net/v1/leagues/serie-a/seasons/15-16/teams'
#response = requests.get(url)

#print(response.url)
#if response.status_code == 200:
 #response_json = json.loads(response.text)
 #print(response_json)



#response_json = response.json()
    #origin = response_json
    #print(origin)



 #consulta = json.loads(response.text)
 #print(consulta )


#if response.status_code == 200:
 #response_json = response.json()
 #or.igin = response_json
 #print(origin)
