#!/bin/bash
# script to post from json file
curl -s -d "@$2" "$1" -H "Content-Type: application/json"
