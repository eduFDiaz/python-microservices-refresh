import os
from typing_extensions import override
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings

import logging

MONGO_HOST = os.environ.get("MONGO_HOST", "mongodb")
TEMPORAL_URL = os.environ.get("TEMPORAL_URL", "temporal:7233")
TEMPORAL_NAMESPACE = os.environ.get("TEMPORAL_NAMESPACE", "default")
TEMPORAL_QUEUE_NAME = os.environ.get("TEMPORAL_QUEUE_NAME", "test-queue")
MEMGRAPH_HOST = os.environ.get("MEMGRAPH_HOST", "memgraph")
MEMGRAPH_PORT = int(os.environ.get("MEMGRAPH_PORT", 7687))

class Settings(BaseSettings):
    temporal_url: str = TEMPORAL_URL
    temporal_namespace: str = TEMPORAL_NAMESPACE
    temporal_queue_name: str = TEMPORAL_QUEUE_NAME
    memgraph_host: str = MEMGRAPH_HOST
    memgraph_port: int = MEMGRAPH_PORT

settings = Settings()

temporal_url = settings.temporal_url
temporal_namespace = settings.temporal_namespace
temporal_queue_name = settings.temporal_queue_name
memgraph_host = settings.memgraph_host
memgraph_port = settings.memgraph_port

import logging
FORMAT = "[%(asctime)s - %(levelname)s - %(filename)s:%(funcName)21s:%(lineno)s] %(message)s"
# Set up basic configuration for logging
logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt='%H:%M:%S', filename='./WORKFLOW_MS.log', filemode='w')

# Create an instance of the logger
logger = logging.getLogger()

api_credentials = {
    'REST': {
        'username': 'admin',
        'password': 'C1sco12345',
        'paramsFile': './Models/PARAMS/REST_PARAMS.yml'
    },
    'CLI': {
        'username': 'admin',
        'password': 'C1sco12345',
        'paramsFile': './Models/PARAMS/CLI_PARAMS.yml'
    },
    'NETCONF': {
        'username': 'admin',
        'password': 'C1sco12345',
        'paramsFile': './Models/PARAMS/NETCONF_PARAMS.yml'
    },
    'GRPC': {
        'username': 'grpc_user',
        'password': 'grpc_pass',
        'paramsFile': './Models/PARAMS/GRPC_PARAMS.yml'
    }
}

class Global_params:
    _instance = None
    _singleton_data = {
        "interfaceName":["GigabitEthernet1"],
    }
    # _singleton_data = {
    # "city_id":["AUSTIN"],
    # "site_id":["site1"],
    # "sites": [ 
    #     {"name" : "site1"},
    #     {"name" : "site2"}
    # ]
    # }
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def getitem(self, key):
        return self._singleton_data[key]

    def setitem(self, key, value):
        self._singleton_data[key] = value
    
    def update(self, value):
        self._singleton_data.update(value)
    
    def getMap(self):
        return self._singleton_data
    
    @override
    def __str__(self) -> str:
        return str(self._singleton_data)