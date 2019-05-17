#! /usr/bin/python3
import google
import sys
from googlesearch import search

query=sys.argv[1]
for i in search(query,tld="co.in",num=5,start=0,stop=5):
	print(i)

