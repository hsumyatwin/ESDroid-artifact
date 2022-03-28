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
package = 'ch.fixme.cowsay'
activity ='ch.fixme.cowsay.Main'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.3)
MonkeyRunner.sleep(0.3)
device.touch(699,935, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(547,977, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(396,901, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(760,629, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(12,1294, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(805,1129, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(254,746, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(985,356, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(4,528, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(965,585, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(463,1270, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(441,682, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(726,1363, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(966,1081, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(552,610, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(583,1771, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(663,110, 'DOWN_AND_UP')
