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
package = 'com.tailscale.ipn'
activity ='org.gioui.GioActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.1)
MonkeyRunner.sleep(0.1)
device.touch(645,650, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(416,1772, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(950,1697, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(297,298, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(778,1282, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(769,382, 'DOWN_AND_UP')
