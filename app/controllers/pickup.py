from app import app
from flask import Response
import os
import json
import jsonpickle
from app.services import heb_service
from urllib.error import HTTPError

@app.route("/pickup/<zipcode>", methods = ['GET'])
def next_time_all_stores(zipcode):
   

    try:
        next_pickups = heb_service.get_next_pickups(zipcode)
    except AttributeError as ex:
       return Response(json.dumps({"error": str(ex)}),status=400, mimetype='application/json')
    except HTTPError as ex:
        return Response(json.dumps({"error": str(ex)}),status=400, mimetype='application/json')

    return Response(jsonpickle.encode(next_pickups, unpicklable=False), status = 200, mimetype='application/json')
    



