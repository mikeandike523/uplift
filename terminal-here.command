#!/bin/bash
# Get the directory path of the current script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Open Terminal in that directory
open -a Terminal "$DIR"
exit
