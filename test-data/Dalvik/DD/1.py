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
package = 'org.jessies.dalvikexplorer'
activity ='org.jessies.dalvikexplorer.DalvikExplorerActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
device.touch(343,1202, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(930,1766, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(747,485, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(995,1375, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(560,1561, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(565,115, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(945,754, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(721,893, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(212,252, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(563,453, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(363,244, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(98,1159, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(372,426, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(10,1371, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(306,613, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(707,1731, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(293,1585, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(596,1673, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(916,1304, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(257,1286, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(235,1859, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(69,262, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)