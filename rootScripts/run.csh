#!/bin/csh -f

set filename = $1
set i = $2

printenv
pwd
ls

echo "\n\n"
echo "File name is $filename"


./createVerticaInputLoop_skim_condor.py $1 $2 $3

