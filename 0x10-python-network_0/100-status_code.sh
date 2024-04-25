#!/bin/bash
# Script to pull status code from header
curl -s -L -X HEAD -w "%{http_code}" "$1"
