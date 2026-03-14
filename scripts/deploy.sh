#!/bin/sh

set -e

# Pull latest changes
ssh user@host 'cd /path/to/deployment && git pull'

# Build and restart containers
ssh user@host 'cd /path/to/deployment && docker-compose pull && docker-compose up -d --build'

# Run migrations
ssh user@host 'cd /path/to/deployment && ./scripts/migrate.sh'