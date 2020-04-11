from app import app
from quart import Response
import os
import json
import jsonpickle
from app.services import heb_service
import aiohttp 
import asyncio

@app.route("/pickup/<zipcode>", methods = ['GET'])
async def next_time_all_stores(zipcode):
    try:
        next_pickups = await heb_service.get_next_pickups(zipcode, 5)
    except AttributeError as ex:
       return Response(json.dumps({"error": str(ex)}),status=400, mimetype='application/json')
    except aiohttp.ClientResponseError as ex:
        return Response(json.dumps({"error": str(ex)}),status=400, mimetype='application/json')

    return Response(jsonpickle.encode(next_pickups, unpicklable=False), status = 200, mimetype='application/json')