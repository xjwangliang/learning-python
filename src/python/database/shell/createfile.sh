#!/bin/sh
#var1=1
#while test $var1 -le $2
#do
#        mkdir $1$var1
#       var1=$(($var1+1))
#done
var1=1
pre=wang
while test $var1 -le $2
	do
        	touch $pre$1$var1
		var1=`expr  $var1 + 1`
		#var1=$(($var1+1))
	done

#    运行时输入:mycomm.sh  user  10000
