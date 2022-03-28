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
package = 'app.librenews.io.librenews'
activity ='app.librenews.io.librenews.views.MainFlashActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.3)
MonkeyRunner.sleep(0.3)
device.touch(985,387, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(4,555, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(726,1372, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(894,720, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(720,199, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(920,277, 'DOWN_AND_UP')
