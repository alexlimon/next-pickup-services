import logging
import os
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    params = req.url.split("/")
    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    #file_to_return = open(ROOT_DIR+ "/" + params[len(params) - 1])

    return func.HttpResponse(body = ROOT_DIR, mimetype="text/plain")
