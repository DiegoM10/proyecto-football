from flask import Flask, render_template,redirect, request
from flask_api import FlaskAPI
import http.client
import json


#print(response)
app = Flask('__name__')

@app.route('/',methods =['GET','POST'])
def init():
    return
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': '6f89e625709d4b11af33273c70007ae9 ', 'X-Response-Control': 'minified'}
    connection.request('GET', '/v1/competitions', None, headers)
    response = json.loads(connection.getresponse().read().decode())
    #print(response)
    for x in response:
        id = x['id']
        copa = x['caption']
        liga = x['league']

        print(id,'', copa,'',liga)
        print('id',x["id"],'copa',x["caption"],'liga',x["league"],'año',x["year"],'dia_actual',x["currentMatchday"],'jornadas',x["numberOfMatchdays"],
            'cantidad de equipos',  x["numberOfTeams"],
          'numero de partidos',x["numberOfGames"],'actualizacion', x["lastUpdated"])

    return render_template('init.html',id=id, copa=copa, liga=liga)

        #return render_template('inicio.html')

#@app.route('/goleadores',methods=['POST'])
#def goleadores():
 #   return render_template('goleadores.html')

if __name__=='__main__':
    app.run()
