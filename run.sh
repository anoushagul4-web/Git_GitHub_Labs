#!/bin/bash
set -e

export APP_ENV="${APP_ENV:-dev}"
export APP_NAME="${APP_NAME:-cloud-app}"

python3 system_check.py
