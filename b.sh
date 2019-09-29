#!/bin/bash
a=0
while true
do
	((a++))
	echo -e "\n"
	echo "---------######正在进行第 $a 次尝试。`date '+%Y-%m-%d %H:%M:%S'`"
	https_proxy=https://localhost:1080 scrapy crawl biu
	https_proxy=https://localhost:1080 scrapy crawl fangao
	https_proxy=https://localhost:1080 scrapy crawl huoguo
	https_proxy=https://localhost:1080 scrapy crawl niao
	https_proxy=https://localhost:1080 scrapy crawl zhu
	https_proxy=https://localhost:1080 scrapy crawl zuipao
	https_proxy=https://localhost:1080 scrapy crawl bayinhe
	https_proxy=https://localhost:1080 scrapy crawl tuzi
	for b in `seq -w 30 -1 0`
	do
		echo -en "---------将会在$b秒后重试。\r"  
	  sleep 1;
	done
done
