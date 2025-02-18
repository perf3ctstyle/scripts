#!/bin/bash
response=$(curl --location 'https://catfact.ninja/breeds?limit=1' --header 'Accept: application/json')
echo "$response" | jq -r ".first_page_url"
