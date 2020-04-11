import logging
import azure.functions as func
from ..core.services import heb_service
import json
import jsonpickle
import aiohttp

async def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    zipcode = req.route_params.get('zipcode')
    try: 
        next_pickups = await heb_service.get_next_pickups(zipcode, 5)
    except AttributeError as ex:
        return func.HttpResponse(body = json.dumps({"error": str(ex)}), status_code=400, mimetype='application/json')
    except aiohttp.ClientError as ex:
        return func.HttpResponse(body = json.dumps({"error": str(ex)}),status_code =400, mimetype='application/json')
    return func.HttpResponse(body = jsonpickle.encode(next_pickups, unpicklable=False), status_code = 200, mimetype='application/json')