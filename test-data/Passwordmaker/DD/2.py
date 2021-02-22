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
device.touch(790,513, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(689,1046, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(645,672, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(416,1792, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(950,1718, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(297,321, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(158,139, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(591,1757, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(112,1174, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(444,1434, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(1070,937, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(806,1360, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(883,1542, 'DOWN_AND_UP')
