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
device.touch(796,1398, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(480,615, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(612,1173, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(758,571, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(772,384, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1016,1167, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(433,936, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(563,149, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(995,987, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(656,722, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(700,567, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(936,262, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(877,1071, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(774,300, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(224,843, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(495,1797, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(233,1850, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(823,204, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(63,1599, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(663,527, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(147,755, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(1022,231, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(790,857, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(819,1439, 'DOWN_AND_UP')
MonkeyRunner.sleep(1)
device.touch(612,976, 'DOWN_AND_UP')
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
MonkeyRunner.sleep(1)