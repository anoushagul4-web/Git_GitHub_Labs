#!/bin/bash

SERVICE_NAME="${SERVICE_NAME:-demo-service}"

echo "Running health check for $SERVICE_NAME"

python3 health_check.py

# TODO: detect Python failure using the exit status ($?)
# and print either SUCCESS or ALERT.
