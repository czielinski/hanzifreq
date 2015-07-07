#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo >&2 "Usage: $0 path/to/large.file"
  echo >&2 "This script takes a large file and splits it"
  echo >&2 "into smaller files in the directory 'input/'"
  exit 1
fi

type split >/dev/null 2>&1 || {
  echo >&2 "ERROR: Please install 'split'."
  exit 1
}

split --lines=500000 "$1" "input/part_"
