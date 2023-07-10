#!/bin/bash

source ./.venv/bin/activate
pytest --webdriver Firefox --headless

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
  exit 0
else
  exit 1  # Return 1 if any error occurs (including errors from incorrect setup e.g. missing driver)
fi