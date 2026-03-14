#!/bin/sh

set -e

# Check if Docker is installed
if ! [ -x "$(command -v docker)" ]; then
  echo 'Error: Docker is not installed.' >&2
  exit 1
fi

# Start Docker Compose
exec docker-compose up