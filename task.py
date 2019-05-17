from googlesearch import search
import sys
query=sys.argv[1]

for i in search(query, tld='co.in', lang='es', stop=5):
    print(i)
