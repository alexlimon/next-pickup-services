import logging
import jsonpickle
import azure.functions as func
from ..core.services import manage_recipient_service
import json
async def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    response = None
    try:
        name = None
        zipcode = None
        phone_number = None

        if req.method == "GET":

            name = req.params["name"]
            zipcode = req.params["zipcode"]
            phone_number = req.params["phoneNumber"]
    
        else:
            parameter_body = req.get_json()

            name = parameter_body["name"]
            zipcode = parameter_body["zipcode"]
            phone_number = parameter_body["phoneNumber"]
        
        response =  await manage_recipient_service.manage_recipient(phone_number = phone_number, name = name, zipcode = zipcode, http_method= req.method)
        
    except AttributeError as ex:
        return func.HttpResponse(body = json.dumps({"Attribute Error" : str(ex)}),status_code =400, mimetype='application/json')
    except RuntimeError as ex:
        return func.HttpResponse(body = json.dumps({"Runtime Error": str(ex)}),status_code =400, mimetype='application/json')

    return func.HttpResponse(body = jsonpickle.encode(response, unpicklable = False), status_code = 200, mimetype='application/json')

