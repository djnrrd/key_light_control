#!/bin/sh

SCRIPT=$(readlink -f "$0")
BASEDIR=$(dirname "$SCRIPT")

$BASEDIR/venv/bin/python $BASEDIR/lights.py
