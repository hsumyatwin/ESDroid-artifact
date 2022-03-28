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
package = 'es.senselesssolutions.gpl.weightchart'
activity ='es.senselesssolutions.gpl.weightchart.ChartActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(1)
device.touch(695,1560, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(326,1304, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(236,1855, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1631,995, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(487,1282, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(235,1861, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(487,1689, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1619,983, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(558,1730, 'DOWN_AND_UP')
