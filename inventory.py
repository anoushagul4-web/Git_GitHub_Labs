#!/usr/bin/env python3

import platform
import shutil

print("=== Server Inventory ===")
print(f"Hostname: {platform.node()}")
print(f"OS: {platform.system()} {platform.release()}")

# Disk Usage
total, used, free = shutil.disk_usage("/")

print(f"Disk Total: {total // (1024**3)} GB")
print(f"Disk Used: {used // (1024**3)} GB")
print(f"Disk Free: {free // (1024**3)} GB")

# Developer B:
# Add a memory section.
# On Linux you may read /proc/meminfo.

print("========================")
