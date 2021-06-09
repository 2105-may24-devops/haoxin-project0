#!/usr/bin/env bash


python project.py
   if cmp output.txt r.txt; then
   		echo "pass."

   	else
   		echo "fail."

   	fi

