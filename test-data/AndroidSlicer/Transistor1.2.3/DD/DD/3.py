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
package = 'org.y20k.transistor'
activity ='org.y20k.transistor.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.1)
MonkeyRunner.sleep(0.1)
device.touch(882,1403, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1004,341, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(941,311, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1012,1463, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(858,975, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1023,315, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(964,1012, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(986,424, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(996,389, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(859,348, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(896,1005, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1075,494, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(945,446, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(953,473, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1056,136, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(989,1204, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(883,1199, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1077,427, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(940,872, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(931,837, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(969,1799, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(998,1644, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(970,920, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(953,603, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1017,1735, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(903,368, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(979,1031, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(988,1436, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1013,424, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(914,1416, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(907,1771, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1037,1517, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(893,1173, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(858,1162, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(903,1593, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1015,1322, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(971,1778, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(891,1300, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1041,284, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(995,904, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(879,1138, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(863,1093, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(873,198, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1009,554, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(992,1540, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(936,1106, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(922,1587, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1023,802, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(941,539, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1020,1604, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(866,862, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1050,1631, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(870,1392, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(952,1799, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(870,1084, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(984,1215, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1060,496, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(912,1293, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(932,1121, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(927,112, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(958,708, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(960,376, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1008,1308, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1023,1678, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(989,1184, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(881,1410, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(925,1594, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(998,1677, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(901,1376, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(892,143, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(941,1431, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1016,260, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1027,122, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(927,1224, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(952,763, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1023,702, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1028,628, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(971,898, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(886,125, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(956,1267, 'DOWN_AND_UP')
