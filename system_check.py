#!/usr/bin/env python3

import os
import sys

required = ["APP_ENV", "APP_NAME"]

missing = [name for name in required if not os.getenv(name)]

print("=== System Check ===")
print(f"Required variables checked: {len(required)}")

if missing:
    print("Missing required configuration:", ", ".join(missing))
    sys.exit(1)

print("Configuration OK")
print("No secret values are displayed.")
