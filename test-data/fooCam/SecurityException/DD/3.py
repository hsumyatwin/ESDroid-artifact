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
device.touch(201,244, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(142,1652, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(878,541, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(518,1462, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(516,1687, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(151,347, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(230,480, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(112,1040, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1044,421, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(639,336, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(643,1784, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(75,535, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(679,269, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(97,506, 'DOWN_AND_UP')
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
