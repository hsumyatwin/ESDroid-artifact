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
package = 'com.ringdroid'
activity ='com.ringdroid.RingdroidSelectActivity'
runComponent = package+'/'+activity
#device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.3)
MonkeyRunner.sleep(0.3)
device.touch(1015,128, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(1026,532, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(1054,690, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(931,1140, 'DOWN_AND_UP')
