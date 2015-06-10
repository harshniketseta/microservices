#!/bin/bash

for i in {1..100000}
do
	for i in {1..100000}
	do       
	    curl -s "http://localhost:3001/do_pageview.js" &
	done
done