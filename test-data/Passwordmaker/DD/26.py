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
package = 'org.passwordmaker.android'
activity ='org.passwordmaker.android.PasswordMakerProForAndroidActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.3)
MonkeyRunner.sleep(0.3)
device.touch(41,980, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(170,1176, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(960,1525, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(253,1862, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(244,1859, 'DOWN_AND_UP')
