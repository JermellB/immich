import os
import sys

import requests
from security import safe_requests

port = os.getenv("IMMICH_PORT", 3003)

try:
    response = safe_requests.get(f"http://localhost:{port}/ping", timeout=2)
    if response.status_code == 200:
        sys.exit(0)
    sys.exit(1)
except requests.RequestException:
    sys.exit(1)
