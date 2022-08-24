import sys
from pathlib import Path

import pkg_resources
from grpc_tools import protoc

args = []

for e in [
    "cosmos-sdk/proto",
    "cosmos-proto/proto",
    "gogoproto",
    "googleapis",
]:
    args += [f"--proto_path=third_party/{e}"]

args += ["--python_out=."]
args += ["--grpc_python_out=."]

for e in ["cosmos-sdk/proto", "cosmos-proto/proto", "gogoproto/gogoproto"]:
    args += list(map(str, Path(f"third_party/{e}").rglob("*.proto")))


def main():
    proto_include = pkg_resources.resource_filename("grpc_tools", "_proto")
    return protoc.main([""] + args + [f"-I{proto_include}"])


if __name__ == "__main__":
    sys.exit(main())
