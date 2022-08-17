# ESDroid
ESDroid is a debugging tool for Android App.

# Usage
ESDroid is in Python and Java. You can find the source code under "implementation" directory and the required scripts for running the tool under the "tool" directory. The tested data is available under "test-data."

1. After cloning/extracting the tool directory in a folder (e.g., ~/ESDroid-artifact/tool), you need to change the ***PLATFORDIRFORSLICER*** parameter in 3 script files (**instrumenter.sh**, **preSlicer.sh**, and **ESDroid.sh**). ***PLATFORDIRFORSLICER*** is the path of your android sdk/platforms folder.

2. Copy the app apk file (eg; app-debug.apk) that you want to do the slicing into the tool directory (i.e., ~/ESDroid-artifact/tool/). 

3. Run the instrumenter script for the app using the following command to instrument the app and sign the instrumented apk file.

   > **./instrumenter.sh <apk_file>**
   
   P.S. Change the package name [E.g., com.muledog.calculator]   

4. Make sure that either your emulator is running or the phone is connected and accessible via adb. 
   Run the following command to install the instrumented app on the emulator.
   >**adb install C:\Users\Heather\eclipse-workspace\ESDroid-artifact\tool\sootOutput\app-debug.apk**
   
5. Make sure that either your emulator is running or the phone is connected and accessible via adb.    
   Run following command. This will log if the exception occurs.
   >**adb logcat Exception:E *:S > C:\Users\Heather\AppData\Local\Android\Sdk\tools\logerr.txt**
   
   Change the package name and activity name (i.e., ACTION_MAIN/an entry point for the application) in FLiADFSoE.py. 
   [E.g., package = 'com.muledog.calculator', activity ='com.muledog.calculator.MainActivity']
   
   Run the FLiADFSoE.py. This will generate the random events (i.e., 0.py), and the script will stop once the failed test case is found. 
   [E.g., .\monkeyrunner.bat .\FLiADFSoE.py for Windows PowerShell]
   
   Stop the logging command.
    
6. Run the following commands and then run the app on your emulator/real phone. This will collect the required log file for ESDroid.
   >**adb logcat Exception:E *:S > C:\Users\Heather\AppData\Local\Android\Sdk\tools\logerr.txt**
   
   >**adb logcat | find "FLiAD:" > <apk_file>.logcat.txt**     
   
   >[E.g., adb logcat | find "FLiAD:" > app-debug.apk.logcat.txt]
   
7. Change exceptionType, className, lineNumber (i.e., the failure point) got from logerr.txt at step 5 in FLiADDmin3.java. 
   >[E.g., NumberFormatException, MainActivity, 117]
   Run FLiADD.bat. This will simplify the event sequence. After you finish with running FLiADD.bat, stop the above command. 
   
8. Run the preSlicer script for the app:

   >**./preSlicer.sh <apk_file> <package_name>**
   
   >[E.g.,  ./preSlicer.sh app-debug.apk com.muledog.calculator]

   This will create a <apk_file>.logcat.processed.txt file. Each line starts with a number. You need to pick a number (your interesting point as the slicing criteria) to add to the next command. 

9. Run the ESDroid script for the app and then enter the number (i.e., from app-debug.apk.logcat.processed.txt) that you picked from previous step:

   >**./ESDroid.sh <apk_file> <package_name> <post_ToSlice>**
   
   >[E.g., ./ESDroid.sh app-debug.apk com.muledog.calculator 8980]
        
   Finally, you will have the slices files wrt your slicing criteria

# Replication package

The replication package is structured as follows:

```
    /
    .
    |--- implementation/      Implementation including libraries and source code
    |--- test-data/           List of apps tested
    |--- tool/                Working directory including the scripts
```

Each of the folders listed above are described in details in the remaining of this readme.

1. Implementation

```
implementation
    .
    |--- lib      List of dependencies.   
    |--- src      Source code of ESDroid. 
```

2. Test data (Experiment apps)

```
test-data
    .
    |--- AndroidSlicer     Experiment apps that compared against with AndroidSlicer.  
      |--- <App name>      App name.
      |--- DD              Delta Debugging result with python script and error log
      |--- SL              Slicing result
        |--- FSoE          Slice for the orginal event sequence
        |--- DFSoE         Slice for the simplified event sequence
    |--- Mandoline         Experiment apps that compared against with Mandoline.
      |--- <App name>      App name.
      |--- DD              Delta Debugging result with python script and error log
      |--- SL              Slicing result
        |--- FSoE          Slice for the orginal event sequence
        |--- DFSoE         Slice for the simplified event sequence
```

3. Working folder

```
tool
    .
    |--- resources      Required resources.   
    |--- sootOutput     Directory for instrumented apps.
```

# Note
Hsu: I have used Ubuntu, Window command line and emulator since I run ESDroid on Windows OS.
Due to file size, ESDroid.jar and preSlicer.jar are available at https://drive.google.com/drive/folders/1OOq9YEX9UxH4ewQSbnQJmS9pbCWCeu-m?usp=sharing
