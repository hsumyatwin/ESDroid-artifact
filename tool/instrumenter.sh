echo "if you closed adb logcat press enter hiiii"
read input_close
#ls
rm -r ./sootOutput/$1 #uncomment later
PLATFORDIRFORSLICER="/mnt/c/Users/Heather/AppData/Local/Android/Sdk/platforms"


javac -target 1.8 -cp  ".:soot-trunk.jar:soot-infoflow.jar:soot-infoflow-android.jar:sootclasses-trunk-jar-with-dependencies.jar;/mnt/c/Java/jdk1.8.0_141/jre/lib/rt.jar" InstrumenterEvent.java #uncomment later

java -Xmx5g -cp  ".:soot-trunk.jar:soot-infoflow.jar:soot-infoflow-android.jar:sootclasses-trunk-jar-with-dependencies.jar;/mnt/c/Java/jdk1.8.0_141/jre/lib/rt.jar" InstrumenterEvent -w -allow-phantom-refs -process-multiple-dex -android-jars $PLATFORDIRFORSLICER -src-prec apk -output-format dex -process-path $1

chmod 777 ./sootOutput/$1

cp ./sootOutput/$1 /mnt/c/Users/Heather/eclipse-workspaceFLiAD/sootOutput/$1.bk
jarsigner -keystore keystore.jks -storepass hsu99999 ./sootOutput/$1 key9
chmod 777 $1_signed.apk


