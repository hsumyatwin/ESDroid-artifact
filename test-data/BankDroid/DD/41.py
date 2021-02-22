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
package = 'com.liato.bankdroid'
activity ='com.liato.bankdroid.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.6)
MonkeyRunner.sleep(0.6)
device.touch(779,119, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(1020,132, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(416,1792, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(950,1716, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(297,296, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(158,111, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(144,216, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(1014,127, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(967,159, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(980,331, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(586,581, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(511,1086, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(479,732, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(308,1794, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(705,1723, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(220,399, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(117,227, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(564,463, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(860,1710, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(520,1695, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(534,1373, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(936,959, 'DOWN_AND_UP')
