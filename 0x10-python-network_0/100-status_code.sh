#!/bin/bash
# Script to pull status code from header
curl -sL -X HEAD -w "%{http_code}" "$1"
