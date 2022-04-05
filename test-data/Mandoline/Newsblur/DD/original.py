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
package = 'com.newsblur'
activity ='com.newsblur.activity.InitActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(1)
device.touch(302, 250, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1017, 147, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(757, 142, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(605, 379, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
