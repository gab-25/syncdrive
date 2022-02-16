#!/bin/bash

set -e

export PYTHONPATH="$PWD/syncdrive"

python3 -m unittest tests/syncdrive_tests.py -v
