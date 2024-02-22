#!/bin/bash

DESIRED_PLAYS=$1

counter=1
while [ $counter -le $DESIRED_PLAYS ]
do
  notone
  ((counter++))
done
