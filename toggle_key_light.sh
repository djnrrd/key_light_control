#!/bin/sh

SCRIPT=$(readlink -f "$0")
BASEDIR=$(dirname "$SCRIPT")

. $BASEDIR/venv/bin/activate

if [ -n "$VIRTUAL_ENV" ]; then
  python3 $BASEDIR/lights.py
else
  echo "Unable to detect Virtual Environment"
fi
