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
package = 'com.spisoft.quicknote'
activity ='com.spisoft.quicknote.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.5)
MonkeyRunner.sleep(0.5)
device.touch(919,83, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(332,992, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(993,554, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(945,1127, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(982,153, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(699,932, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(923,1695, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(165,437, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(432,463, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(660,748, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(467,678, 'DOWN_AND_UP')
