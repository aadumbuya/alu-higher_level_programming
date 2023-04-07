#!/bin/bash
# This script sends a JSON POST request to URL and displays the body of the response
curl -s -H "content-type: application/json" -d "$(cat "$2")" "$1"
