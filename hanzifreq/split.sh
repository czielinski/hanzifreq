#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 path/to/large_file" >&2
  exit 1
fi

split --lines=500000 "$1" "input/part_"
