@ECHO OFF
set CLASSPATH=.
set CLASSPATH=%CLASSPATH%;
set path=C:\Java\jdk1.8.0_141\bin
javac FLiADDmin3.java
java -Xms128m -Xmx384m -Xnoclassgc FLiADDmin3
pause