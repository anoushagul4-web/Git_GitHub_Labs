#!/usr/bin/env python3

import os

region = os.getenv("AWS_REGION", "unknown")
environment = os.getenv("ENVIRONMENT", "unknown")

print("=== Cloud Report ===")
print(f"Region: {region}")
print(f"Environment: {environment}")
print("Credentials: [not displayed]")
