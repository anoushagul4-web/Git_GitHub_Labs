#!/usr/bin/env python3

import platform
import shutil

print("=== Server Inventory ===")
print(f"Hostname: {platform.node()}")
print(f"OS: {platform.system()} {platform.release()}")

# Developer A:
# Add a disk usage section using shutil.disk_usage().

# Memory Usage
with open("/proc/meminfo") as f:
    meminfo = f.readlines()

for line in meminfo:
    if line.startswith("MemTotal:"):
        total_memory = int(line.split()[1]) // 1024
    elif line.startswith("MemAvailable:"):
        available_memory = int(line.split()[1]) // 1024

print(f"Memory Total: {total_memory} MB")
print(f"Memory Available: {available_memory} MB")

print("========================")
