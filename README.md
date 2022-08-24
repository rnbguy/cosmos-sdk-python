# cosmos-sdk-python

Python GRPC client for Cosmos-SDK

```sh
git submodule update --init --recursive

. "$(poetry env info -p)/bin/activate"

poetry install
python -m cosmos_sdk.build

python examples/query_all_balances.py <COSMOSHUB_GRPC_ENDPOINT> # prints Binance validator balance
```

## Disclaimer

This project is bleeding-edge and does not conform with Poetry package structure.

Only meant for learning Cosmos-SDK GRPC clients in Python.
