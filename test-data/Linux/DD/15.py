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
package = 'ru.meefik.linuxdeploy'
activity ='ru.meefik.linuxdeploy.activity.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(1)
MonkeyRunner.sleep(1)
device.touch(82,121, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(399,417, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1017,139, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(634,910, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(115,1406, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(892,684, 'DOWN_AND_UP')
