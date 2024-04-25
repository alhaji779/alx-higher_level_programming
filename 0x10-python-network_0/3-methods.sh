#!/bin/bash
# Retrieve methods from url
curl -sI "$1" | grep -i Allow | cut -d ' ' -f2-
