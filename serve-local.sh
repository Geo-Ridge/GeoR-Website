#!/bin/bash
echo "Starting Jekyll development server with local configuration..."
echo "Navigate to: http://127.0.0.1:4000/"
echo ""
bundle exec jekyll serve --config _config.yml,_config_local.yml
