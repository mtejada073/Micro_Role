from tokenize import String
from typing import Union
from xxlimited import Str
from fastapi import FastAPI
import requests
from prometheus_fastapi_instrumentator import Instrumentator
import logging.config

app = FastAPI()

Instrumentator().instrument(app).expose(app)


# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project. 
                                      # This will get the root logger since no logger in the configuration has this name.


@app.get("/")
def read_root():
    return  roleUsers()
    

@app.get("/roleUsers/{encryptedToken}")
def read_item(encryptedToken : str):
    list=roleUsers()
    for item in list:
        if item["encryptedToken"]==encryptedToken:
            return item


def roleUsers():
    url='https://62fef1fea85c52ee483e83bb.mockapi.io/roleUsers'
    response = requests.get(url, {}, timeout=5)
    return response.json()