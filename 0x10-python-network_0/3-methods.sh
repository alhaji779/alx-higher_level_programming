#!/bin/bash
# Retrieve methods from url
curl -sI "$1" | grep -i Allow | awk '{print $2}'
