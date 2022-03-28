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
package = 'ch.blinkenlights.android.vanilla'
activity ='ch.blinkenlights.android.vanilla.LibraryActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(3)
device.touch(376,135, 'DOWN_AND_UP')
MonkeyRunner.sleep(3)
device.touch(399,156, 'DOWN_AND_UP')
MonkeyRunner.sleep(3)
device.touch(118,171, 'DOWN_AND_UP')
MonkeyRunner.sleep(3)
device.touch(21,139, 'DOWN_AND_UP')
MonkeyRunner.sleep(3)
device.touch(790,491, 'DOWN_AND_UP')
MonkeyRunner.sleep(3)
device.touch(689,1024, 'DOWN_AND_UP')
MonkeyRunner.sleep(3)
device.touch(645,650, 'DOWN_AND_UP')
MonkeyRunner.sleep(3)
device.touch(416,1772, 'DOWN_AND_UP')
MonkeyRunner.sleep(3)
device.touch(950,1697, 'DOWN_AND_UP')
MonkeyRunner.sleep(3)
device.touch(297,298, 'DOWN_AND_UP')
MonkeyRunner.sleep(3)
device.touch(158,117, 'DOWN_AND_UP')
MonkeyRunner.sleep(3)