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
device.touch(525,93, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(503,447, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(92,631, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(634,471, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(726,933, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(726,219, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(772,927, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(198,938, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(576,1816, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(709,806, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(346,171, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(743,1487, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(491,460, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(936,907, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(357,1514, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(173,1764, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(426,673, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(552,1483, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(266,406, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(928,1138, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(758,1455, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(636,1687, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(523,454, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(476,518, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(850,277, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(265,1373, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(279,774, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(516,866, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(150,767, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(524,526, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(154,1672, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(481,1692, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(415,940, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(587,956, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(140,1396, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(651,1496, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(402,395, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(466,1528, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(325,776, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(441,713, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(558,1719, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(496,445, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(489,303, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(429,920, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(921,1769, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(817,388, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(291,116, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(728,1793, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(587,1725, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(87,53, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(970,1078, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(460,1393, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(862,1586, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(498,1506, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(23,137, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(137,353, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(466,1620, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(471,1454, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(843,888, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(363,76, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(586,1009, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1027,390, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(132,693, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(269,89, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(17,734, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(181,445, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(497,1664, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(452,97, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(910,70, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(822,1353, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(761,489, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(325,77, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(495,1643, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1020,779, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(903,645, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1073,80, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1072,1696, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(1069,1692, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(945,671, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.1)
device.touch(922,946, 'DOWN_AND_UP')
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
