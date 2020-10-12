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
package = 'com.ringdroid'
activity ='com.ringdroid.RingdroidSelectActivity'
runComponent = package+'/'+activity
#device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.3)
MonkeyRunner.sleep(0.3)
device.touch(994,1260, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(990,131, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(210,1067, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(1043,644, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(149,238, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(886,1229, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(463,900, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(896,1003, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(631,1104, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(404,72, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(745,1305, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(74,941, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(747,1456, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(780,661, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(68,674, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(563,1725, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(749,280, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(546,1630, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(180,674, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(751,126, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(281,874, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(439,391, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(317,1066, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(182,713, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(253,1002, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(102,877, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(324,897, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(816,500, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(1015,128, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(1026,532, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(1056,716, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(1054,690, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(921,1136, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.3)
device.touch(931,1140, 'DOWN_AND_UP')
