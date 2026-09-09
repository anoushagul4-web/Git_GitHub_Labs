#!/usr/bin/env python3

import os
import sys

service_name = os.getenv("SERVICE_NAME", "demo-service")

# TODO: make the check fail when the service is unavailable.
# For this lab, simulate the service state with:
# SERVICE_STATE=up python3 health_check.py
# SERVICE_STATE=down python3 health_check.py

state = os.getenv("SERVICE_STATE", "up")

print(f"Checking {service_name}...")

if state == "up":
    print("HEALTHY")
else:
    print("UNHEALTHY")
    sys.exit(1)
