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
