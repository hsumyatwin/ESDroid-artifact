#Imports the monkeyrunner modules used by this program
import os;
from subprocess import Popen
from subprocess import PIPE
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.MonkeyDevice import takeSnapshot
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer
from com.android.monkeyrunner import MonkeyView
import random
import sys
import subprocess
from sys import exit
from random import randint

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
easy_device=EasyMonkeyDevice(device)

#parameter
seedNo=3
#com.muledog.calculator,org.liberty.android.fantastischmemodev,org.jessies.dalvikexplorer,es.senselesssolutions.gpl.weightchart,cx.hell.android.pdfview,org.npr.android.news,com.beem.project.beem,org.fdroid.fdroid
#.MainActivity,org.liberty.android.fantastischmemo.ui.AnyMemo,ChartActivity,ChooseFileActivity,StationListActivity,.ui.Login,FDroid
#'Cal_','AnyMemo_','Dalvik','Chart_','Ppfv_','Npr_','Been_','FDroid_','Gcash_','Pix_'
#appName='FDroid_FSoE'
#appName='FDroid_FSoE'
package = 'org.gnucash.android'
activity ='org.gnucash.android.ui.account.AccountsActivity'
maxX=1080 #device X width # 1080
maxY=1920 #device Y width#1920 1818
eventCount=5000
casecnt=3
#filename=appName+str(seedNo)+'.py'
filename=str(seedNo)+'.py'
delayBetEvent=0.1 #delay percentage bet: events

#option percentage for future

#start process
f = open(filename,'w')
runComponent = package+'/'+activity
device.startActivity(component=runComponent)

f.write("#start monkey test seedNo "+str(seedNo)+"\n")
f.write("import os;\n")
f.write("from subprocess import Popen\n")
f.write("from subprocess import PIPE\n")
f.write("from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage\n")
f.write("from com.android.monkeyrunner.MonkeyDevice import takeSnapshot\n")
f.write("from com.android.monkeyrunner.easy import EasyMonkeyDevice\n")
f.write("from com.android.monkeyrunner.easy import By\n")
f.write("from com.android.chimpchat.hierarchyviewer import HierarchyViewer\n")
f.write("from com.android.monkeyrunner import MonkeyView\n")
f.write("import random\n")
f.write("import sys\n")
f.write("import subprocess\n")
f.write("from sys import exit\n")
f.write("from random import randint\n")
f.write("device = MonkeyRunner.waitForConnection()\n")
f.write("easy_device=EasyMonkeyDevice(device)\n")
f.write("package = '"+package+"'\n")
f.write("activity ='"+activity+"'\n")
f.write("runComponent = package+'/'+activity\n")
f.write("device.startActivity(component=runComponent)\n")
f.write("MonkeyRunner.sleep("+str(delayBetEvent)+")\n")
random.seed(seedNo)
for i in range(1,eventCount):
 xM = randint(0,maxX)
 yM = randint(0,maxY)
 device.touch(xM,yM,'DOWN_AND_UP') 
 f.write("device.touch("+str(xM)+","+str(yM)+","+" 'DOWN_AND_UP'"+")\n")
 f.write("MonkeyRunner.sleep("+str(delayBetEvent)+")\n")
 MonkeyRunner.sleep(delayBetEvent)
 #rotation test
 #f.write("subprocess.call([r'rotateL.bat'])\n")
 #f.write("MonkeyRunner.sleep("+str(delayBetEvent)+")\n")
 #subprocess.call([r'rotateL.bat'])
 #MonkeyRunner.sleep(delayBetEvent)
 #f.write("subprocess.call([r'rotateP.bat'])\n")
 #f.write("MonkeyRunner.sleep("+str(delayBetEvent)+")\n")
 #subprocess.call([r'rotateP.bat'])
 #stop while exception found read file
 if 'Exception' in open('logerr.txt').read():
  f.write("Stop!!!\n")#system.exit
f.write("#end monkey test\n")
f.close()