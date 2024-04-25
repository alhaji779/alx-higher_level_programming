#!/bin/bash
# Script to get the content size from a url header
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
