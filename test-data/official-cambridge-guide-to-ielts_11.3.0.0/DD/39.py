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
package = 'air.com.yudu.ReaderAIR4697674'
activity ='com.yudu.androidreader.BaseActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.5)
MonkeyRunner.sleep(0.5)
device.touch(1021,101, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(477,875, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(921,944, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1072,1751, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(381,158, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(522,1756, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1069,1403, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(542,518, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(877,1736, 'DOWN_AND_UP')
