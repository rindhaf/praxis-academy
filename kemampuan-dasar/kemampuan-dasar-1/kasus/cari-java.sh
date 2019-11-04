#!/bin/bash
filejava=$java
if [ -f "$filejava" ]; then
echo "Ada file java pada " $java
else
echo "Tidak ada file java"
fi
