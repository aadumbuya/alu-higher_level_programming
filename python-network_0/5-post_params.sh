#!/bin/bash
# This script sends a POST request and gisplays the body response using curl
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
