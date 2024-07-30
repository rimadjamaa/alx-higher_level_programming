#!/bin/bash
# Get the byte size of the HTTP response header for a given URL.
url="$1"

# Use head command to get only the header and pipe it to wc -c
curl -s "$url" | wc -c
