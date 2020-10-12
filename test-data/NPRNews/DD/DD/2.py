#start monkey test
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
easy_device=EasyMonkeyDevice(device)
package = 'org.npr.android.news'
activity ='org.npr.android.news.StationListActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(1)
device.touch(26,1678, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(532,1122, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(736,870, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(109,949, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(461,129, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(728,784, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(205,260, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(215,770, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(110,136, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(568,515, 'DOWN_AND_UP')
