#start monkey test
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
easy_device=EasyMonkeyDevice(device)
package = 'net.phunehehe.foocam'
activity ='net.phunehehe.foocam.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.1)
device.touch(985,365, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(972,1008, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(795,395, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(256,241, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1678,546, 'DOWN_AND_UP')
