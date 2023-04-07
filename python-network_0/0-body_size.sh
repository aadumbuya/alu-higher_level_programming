#!/bin/bash
# This script sends the request to URL and Displays the size of the of the response
curl -s "$1" | wc -c
