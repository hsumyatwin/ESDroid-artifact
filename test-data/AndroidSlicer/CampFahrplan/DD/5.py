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
package = 'nerd.tuxmobil.fahrplan.congress.debug'
activity ='nerd.tuxmobil.fahrplan.congress.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.8)
MonkeyRunner.sleep(0.8)
device.touch(740,520, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.8)
device.touch(326,1384, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.8)
device.touch(963,1373, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.8)
device.touch(851,1387, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.8)
device.touch(631,1393, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.8)
device.touch(440,1397, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.8)
device.touch(420,1560, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.8)
device.touch(320,1387, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.8)
device.touch(892,681, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.8)
device.touch(235,1868, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.8)
device.touch(798,124, 'DOWN_AND_UP')
