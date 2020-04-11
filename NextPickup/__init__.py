import logging
from . import app
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    route_path = req.route_params.get('route')
    with app.test_client() as app_router:
        doAction = {
            "GET": app_router.get(route_path).data,
            "POST": app_router.post(route_path).data
        }
        resp = doAction.get(req.method).decode()
        
    if route_path:
        return func.HttpResponse(resp)
    else:
        return func.HttpResponse(
             "Unknown route path",
             status_code=400
        )
