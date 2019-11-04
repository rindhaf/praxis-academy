#!/bin/bash
valid=true
count=1
while [ $valid ]
do
echo $counnt
if [ $count -eq 5 ];
then
break
fi
((count++))
done
