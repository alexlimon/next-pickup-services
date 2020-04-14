import logging
import os
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    params = req.url.split("/")
    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    if params[len(params) - 1] == "lcWR5UdlbaRCjndYFuligiUossQrHrigh4Wt4VoO-C4":
        file_to_return = "lcWR5UdlbaRCjndYFuligiUossQrHrigh4Wt4VoO-C4.VLUFO0a_R5GNplkNhGqEaM1J9fJZNA6GyxkvZ2JIMrs"
    if params[len(params) - 1] == "LtiXh_dI7JS7bBEX8BqBieOcr89COBGCvwNSplK6dfE":
        file_to_return = "LtiXh_dI7JS7bBEX8BqBieOcr89COBGCvwNSplK6dfE.VLUFO0a_R5GNplkNhGqEaM1J9fJZNA6GyxkvZ2JIMrs"

    #file_to_return = open(ROOT_DIR+ "/" + params[len(params) - 1])

    return func.HttpResponse(body = file_to_return, mimetype="text/plain")
