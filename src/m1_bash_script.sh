#!/bin/bash
# A sample Bash script, by Erla
echo Hello World!
python m1_test.py
for i in {1..10}
do
  echo "$i"
  python m1_test.py
done
