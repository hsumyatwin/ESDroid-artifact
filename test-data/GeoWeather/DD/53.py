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
package = 'wangdaye.com.geometricweather'
activity ='wangdaye.com.geometricweather.ui.activity.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.5)
MonkeyRunner.sleep(0.5)
device.touch(689,1024, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1033,139, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(696,267, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(351,1045, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(331,1035, 'DOWN_AND_UP')
