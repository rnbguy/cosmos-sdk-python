# cosmos-sdk-python

Python GRPC client for Cosmos-SDK

```sh
git submodule update --init --recursive

. "$(poetry env info -p)/bin/activate"

poetry install
python -m cosmos_sdk.build
python examples/query_all_balances.py
```
