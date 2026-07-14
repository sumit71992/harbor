#!/bin/bash

mkdir -p /logs/verifier

pytest /tests/test_outputs.py -rA || true

if [ -f /app/report.json ]; then
    echo "1" > /logs/verifier/reward.txt
else
    echo "0" > /logs/verifier/reward.txt
fi

exit 0