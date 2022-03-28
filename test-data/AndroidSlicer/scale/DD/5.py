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
package = 'com.davemorrissey.labs.subscaleview.sample'
activity ='com.davemorrissey.labs.subscaleview.sample.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.5)
MonkeyRunner.sleep(0.5)
device.touch(928,841, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(338,1266, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(67,614, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(553,1079, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(629,183, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(225,1090, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(71,142, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(655,1557, 'DOWN_AND_UP')
