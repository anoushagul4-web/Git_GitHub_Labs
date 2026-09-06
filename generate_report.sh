#!/bin/bash
set -e

export AWS_REGION="${AWS_REGION:-eu-west-1}"
export ENVIRONMENT="${ENVIRONMENT:-dev}"

python3 report.py > cloud_report.txt

echo "Report generated: cloud_report.txt"
