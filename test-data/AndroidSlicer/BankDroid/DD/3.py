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
device.touch(1057,1333, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(772,321, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(500,78, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(77,680, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(366,1573, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(1050,1584, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(662,383, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(235,1564, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(10,1281, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(833,1316, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(228,1439, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(1021,95, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(426,1563, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(849,1807, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.6)
device.touch(954,368, 'DOWN_AND_UP')
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
