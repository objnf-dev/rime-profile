#!/bin/sh
cat ./proc_out.txt >> ./merged.txt
sort -n ./merged.txt | uniq > ./final.txt
cat header.txt final.txt > luna_pinyin.beautifulrime.dict.yaml
