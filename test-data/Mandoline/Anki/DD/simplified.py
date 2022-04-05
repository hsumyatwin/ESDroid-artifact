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
package = 'com.rigid.birthdroid'
activity ='com.rigid.birthdroid.BirthdroidActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.3)
MonkeyRunner.sleep(0.3)
device.touch(949,109, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(622,229, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(186,154, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(971,1453, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(322,1141, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(1012,1438, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(634,462, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(587,649, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(684,598, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(985,1530, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(757,772, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(232,1851, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(230,1848, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(229,1846, 'DOWN_AND_UP')
