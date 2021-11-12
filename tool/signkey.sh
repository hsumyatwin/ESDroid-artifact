chmod 777 /mnt/c/Users/Heather/eclipse-workspace/FLiAD/sootOutput/$1

cp /mnt/c/Users/Heather/eclipse-workspace/FLiAD/sootOutput/$1 /mnt/c/Users/Heather/eclipse-workspace/FLiAD/sootOutput/$1.bk
jarsigner -keystore keystore.jks -storepass hsu99999 /mnt/c/Users/Heather/eclipse-workspace/FLiAD/sootOutput/$1 key9
chmod 777 $1


