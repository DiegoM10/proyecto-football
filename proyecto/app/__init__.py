from flask import Flask, render_template,redirect, request
import http.client
import json,requests

app = Flask('__name__')

@app.route('/',methods =['GET'])
def init():
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': '6f89e625709d4b11af33273c70007ae9', 'X-Response-Control': 'minified'}
    connection.request('GET', '/v1/competitions', None, headers)
    response = json.loads(connection.getresponse().read().decode())
    connection.request('GET', '/v1/competitions/445/leagueTable', None, headers)
    premier = json.loads(connection.getresponse().read().decode())
    connection.request('GET', '/v1/competitions/455/leagueTable', None, headers)
    bbva = json.loads(connection.getresponse().read().decode())
    connection.request('GET', '/v1/competitions/452/leagueTable', None, headers)
    bundes = json.loads(connection.getresponse().read().decode())
    connection.request('GET', '/v1/competitions/456/leagueTable', None, headers)
    serieA = json.loads(connection.getresponse().read().decode())
    connection.request('GET', '/v1/competitions/450/leagueTable', None, headers)
    ligue = json.loads(connection.getresponse().read().decode())
    #Es un poco importante detallas que tipo de llamado haces si es GET o POST asi le dices al servidor que camino escojer.
    if request.method == 'GET':
        #La excepcion es por si da el caso que revienta el codigo no te tire esa corretiada de cosas rojas
        #si no que te lo resume en una linea el error.
        try:
            #Metodo 1
            #En este estas mandado todo el json al html para despues recorerlo en el mismo html
            #es mas facil y conveniente hacerlo asi ya que imprimes todos los valos de un tiro
            #y no tienes que hacer un segundo llamado para imprimir otro valor.
            return render_template('init.html',response = response, premier = premier['standing'],bbva = bbva['standing'],
                                   bundes = bundes['standing'], serieA = serieA['standing'],ligue = ligue['standing'])
            #Metodo 2
            #De esta forma estas mandando valor por valor cada ves que recargas la pagina imagina
            #que tengas 50 datos en el json tienes que recargar 50 veces para que aparescan no es malo
            #pero es muy lento...


        except Exception as e:
            print(e)
    #Cuando estas utilizando un if por regla van dos return el que cumple la condicion de if y el que no
    #El que la cumple es el que le mandas los resultados para enviarselos al html como el de arriva
    #El que no los dejas vasio como el de abajo
    return render_template('init.html')




@app.route('/log')
def log():
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': '6f89e625709d4b11af33273c70007ae9', 'X-Response-Control': 'minified'}
    connection.request('GET', '/v1/competitions/455/fixtures', None, headers)

    response = json.loads(connection.getresponse().read().decode())
    if request.method == 'GET':
       try:

           return render_template('loq.html',response=response['fixtures'])
       except Exception as e:
           print(e)

    return  render_template('loq.html')

if __name__ == '__main__':
    app.run()
