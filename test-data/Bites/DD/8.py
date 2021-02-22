#start monkey test seedNo 0
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
device = MonkeyRunner.waitForConnection()
package = 'caldwell.ben.bites'
activity ='caldwell.ben.bites.Bites'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.2)
MonkeyRunner.sleep(0.2)
device.touch(584,1014, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(870,270, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(1070,1850, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.2)
device.touch(1000,1862, 'DOWN_AND_UP')
