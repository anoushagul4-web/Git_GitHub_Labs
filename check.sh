#!/bin/bash

SERVICE_NAME="${SERVICE_NAME:-demo-service}"

echo "Running health check for $SERVICE_NAME"

python3 health_check.py

if [ $? -eq 0 ]; then
    echo "SUCCESS: $SERVICE_NAME is healthy."
else
    echo "ALERT: $SERVICE_NAME is unhealthy!"
    exit 1
fi
