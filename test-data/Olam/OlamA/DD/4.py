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
package = 'com.olam'
activity ='com.olam.MainSearch'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.3)
MonkeyRunner.sleep(0.3)
device.touch(53,1701, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(311,1537, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(437,1519, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(945,1710, 'DOWN_AND_UP')
