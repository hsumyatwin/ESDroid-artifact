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
package = 'com.mitzuli'
activity ='com.mitzuli.MainActivity'
runComponent = package+'/'+activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(0.5)
device.touch(790,485, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(689,1029, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(645,648, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(416,1792, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(950,1715, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(297,289, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(158,103, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(591,1756, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(112,1160, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(444,1426, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1070,918, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(806,1350, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(883,1536, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(569,1642, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(144,208, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1057,1331, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(772,314, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(500,70, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(77,674, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(366,1572, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1050,1583, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(662,377, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(235,1563, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(10,1278, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(833,1314, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(228,1438, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1021,87, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(426,1562, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(849,1807, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(954,362, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1039,1334, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(732,1475, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(477,874, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(921,944, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1072,1765, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(381,145, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(77,114, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(522,1769, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1069,1410, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(542,511, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(334,1552, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(56,80, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(382,215, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(919,69, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(332,996, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(993,549, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(945,1133, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(982,141, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(699,935, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(547,977, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(396,901, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(760,629, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(12,1294, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(805,1129, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(254,746, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(985,356, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(4,528, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(965,585, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(463,1270, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(441,682, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(726,1363, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(966,1081, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(552,610, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(583,1771, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(663,110, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(744,1169, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(884,1364, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(682,615, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(811,397, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(132,1315, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1008,609, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(572,377, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(123,1264, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(409,1103, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1016,1000, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(231,649, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(270,1354, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(98,527, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(203,585, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(819,144, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(93,1629, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(577,213, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(574,191, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(191,1614, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(378,1794, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(622,1124, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(295,964, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1021,445, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(983,97, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(296,1237, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(311,175, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(244,308, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(652,1340, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(328,1161, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(38,901, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(100,1310, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(469,1501, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(653,1243, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(486,668, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(291,1371, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(222,325, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(994,1270, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(990,125, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(210,1074, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1043,645, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(149,233, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(886,1239, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(463,905, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(896,1010, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(631,1112, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(404,65, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(745,1316, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(74,946, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(747,1469, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(780,662, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(68,676, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(563,1742, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(749,276, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(546,1645, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(180,676, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(751,119, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(281,879, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(439,388, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(317,1074, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(182,715, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(790,485, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(689,1029, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(645,648, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(416,1792, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(950,1715, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(297,289, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(158,103, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(591,1756, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(112,1160, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(444,1426, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1070,918, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1300,113, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1020,121, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(1001,127, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(863,125, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(355,1601, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(247,1839, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(80,154, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(253,1868, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(848,1866, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)
device.touch(428,871, 'DOWN_AND_UP')
MonkeyRunner.sleep(0.5)