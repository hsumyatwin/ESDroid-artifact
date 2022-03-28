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
package = 'com.addi'
activity ='com.addi.Addi'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(1)
MonkeyRunner.sleep(1)
device.touch(144,208, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(849,1807, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1007,1854, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(185,1669, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(367,988, 'DOWN_AND_UP')
