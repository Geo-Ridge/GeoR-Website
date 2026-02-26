@echo off
echo Cleaning build directory...
rmdir /s /q _site
echo.
echo Building site...
bundle exec jekyll build --config _config.yml,_config_local.yml
echo.
echo Build complete! Starting server...
echo Navigate to: http://127.0.0.1:4000/
echo.
bundle exec jekyll serve --config _config.yml,_config_local.yml
