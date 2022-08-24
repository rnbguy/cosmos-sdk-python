import json
from argparse import ArgumentParser

import grpc
from google.protobuf.json_format import MessageToDict, ParseDict

from cosmos.bank.v1beta1.query_pb2 import QueryAllBalancesRequest
from cosmos.bank.v1beta1.query_pb2_grpc import QueryStub

parser = ArgumentParser()
parser.add_argument("grpc_endpoint")

args = parser.parse_args()

endpoint = args.grpc_endpoint

# Binance validator address balance
json_payload = {"address": "cosmos156gqf9837u7d4c4678yt3rl4ls9c5vuuxyhkw6"}
pb_payload = ParseDict(json_payload, QueryAllBalancesRequest())


with grpc.insecure_channel(endpoint) as channel:
    stub = QueryStub(channel)
    balance_data = stub.AllBalances(pb_payload)

# # or, using experimental api
# from cosmos.bank.v1beta1.query_pb2_grpc import Query
# balance_data = Query.AllBalances(
#     pb_payload, endpoint, insecure=True
# )

balance_json = MessageToDict(balance_data)
print(json.dumps(balance_json, indent=2))
