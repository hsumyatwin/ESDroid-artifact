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
MonkeyRunner.sleep(3)
device.touch(540,1719, 'DOWN_AND_UP')
MonkeyRunner.sleep(3)
device.touch(678,1713, 'DOWN_AND_UP')
MonkeyRunner.sleep(3)
device.touch(1028,146, 'DOWN_AND_UP')
MonkeyRunner.sleep(3)
device.touch(792,904, 'DOWN_AND_UP')
MonkeyRunner.sleep(3)
device.touch(398,1023, 'DOWN_AND_UP')
MonkeyRunner.sleep(3)
subprocess.call([r'rotateL.bat'])
