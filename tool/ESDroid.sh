PLATFORDIRFORSLICER="/mnt/c/Users/Heather/AppData/Local/Android/Sdk/platforms/"
SOURCESINK="SourcesAndSinks.txt"
HEAP="-Xms2048m -Xmx2048m" 
export JAVA_OPTS="$HEAP"
#apk = "app-debug.apk"
#package= "com.muledog.calculator"
java -jar ESDroid.jar $1 $2 $PLATFORDIRFORSLICER $SOURCESINK $3