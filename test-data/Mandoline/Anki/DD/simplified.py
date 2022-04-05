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
package = 'com.ichi2.anki'
activity ='com.ichi2.anki.IntentHandler'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(1)
MonkeyRunner.sleep(1)
device.touch(82,127, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(305,623, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(787,127, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1001,611, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(713,681, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(532,401, 'DOWN_AND_UP')
