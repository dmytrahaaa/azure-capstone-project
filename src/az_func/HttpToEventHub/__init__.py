import datetime
import json
import logging
import random

import requests
import azure.functions as func


def main(req: func.HttpRequest) -> str:
    req_body = req.get_json()
    name = req_body.get('subreddit')
    body = req_body.get('body')
    createdAt = req_body.get('time')

    timestamp = datetime.datetime.utcnow()

    eventContent = {
        "name": name,
        "body": body,
        "processedAt": f'{timestamp}'
    }

    return json.dumps(eventContent)
