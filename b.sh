#!/bin/bash
a=0
while true
do
	((a++))
	echo -e "\n"
	echo "---------######正在进行第 $a 次尝试。`date '+%Y-%m-%d %H:%M:%S'`"
	scrapy crawl biu
	scrapy crawl fangao
	scrapy crawl huoguo
	scrapy crawl moyu
	scrapy crawl niao
	scrapy crawl shengzhe
	scrapy crawl tuzi
	for b in `seq -w 30 -1 0`
	do
		echo -en "---------将会在$b秒后重试。\r"  
	  sleep 1;
	done
done
