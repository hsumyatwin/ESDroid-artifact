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
package = 'de.smasi.tickmate'
activity ='de.smasi.tickmate.Tickmate'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.3)
MonkeyRunner.sleep(0.3)
device.touch(542,511, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(334,1552, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(56,80, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(382,215, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(919,69, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(332,996, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(993,549, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(945,1133, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(982,141, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(699,935, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(547,977, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(396,901, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(760,629, 'DOWN_AND_UP')
