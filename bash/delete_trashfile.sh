#!/bin/bash

LOG_FILE="deleted_files.log"
touch $LOG_FILE
chmod +w $LOG_FILE

find . -type f \( -name "*.bak" -o -name "~*~" \) -exec sh -c 'echo "{}"; rm {}' \; 2>&1 | tee -a $LOG_FILE
echo "Deleted files are recorded in the log file: $LOG_FILE"
