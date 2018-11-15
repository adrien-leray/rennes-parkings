# -*- coding: utf-8 -*-
import requests
import json
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

headers = {
}


@app.route("/")
def hello():
    res = requests.get(
        'http://data.citedia.com/r1/parks?crs=EPSG:4326', headers=headers)

    parkings = []
    features = []

    data = res.json()

    for value in data['parks']:
        if value is not None:
            parkings.append({
                "name": value['parkInformation']['name'],
                "status": value['parkInformation']['status'],
                "max": value['parkInformation']['max'],
                "free": value['parkInformation']['free']
            })

    for value in data['features']['features']:
        if value is not None:
            features.append({
                "id": value['id'],
                "y": value['geometry']['coordinates'][0],
                "x": value['geometry']['coordinates'][1]
            })

    return render_template('hello.html', parkings=parkings, features=features)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
