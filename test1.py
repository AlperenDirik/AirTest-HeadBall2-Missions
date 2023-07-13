# -*- encoding=utf8 -*-
__author__ = "Alpeen"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
touch(Template(r"tpl1689273295773.png", record_pos=(-0.371, -0.293), resolution=(1080, 2400)))
wait(Template(r"tpl1689273352540.png", record_pos=(0.006, 0.052), resolution=(1080, 2400)))
touch(Template(r"tpl1689273364147.png", record_pos=(-0.264, 0.043), resolution=(1080, 2400)))
sleep(5.0)

exists(Template(r"tpl1689273478208.png", record_pos=(0.308, -0.163), resolution=(2400, 1080)))
assert_not_exists(Template(r"tpl1689273478208.png", record_pos=(0.308, -0.163), resolution=(2400, 1080)),"if pop up not showing on screen")
keyevent("BACK")

wait(Template(r"tpl1689273618853.png", record_pos=(-0.157, 0.155), resolution=(2400, 1080)))
touch(Template(r"tpl1689273626158.png", record_pos=(-0.162, 0.154), resolution=(2400, 1080)))
assert_exists(Template(r"tpl1689273683838.png", record_pos=(-0.091, 0.043), resolution=(2400, 1080)), "If any mission is available, go in the mission")
touch(Template(r"tpl1689273723948.png", record_pos=(0.141, -0.062), resolution=(2400, 1080)))
exists(Template(r"tpl1689273757218.png", record_pos=(0.227, 0.024), resolution=(2400, 1080)))
touch(Template(r"tpl1689273767484.png", record_pos=(0.464, -0.19), resolution=(2400, 1080)))
assert_not_exists(Template(r"tpl1689273944564.png", record_pos=(0.015, -0.001), resolution=(2400, 1080)), "Showing pop-ups") or assert_not_exists(Template(r"tpl1689274079344.png", record_pos=(0.216, 0.149), resolution=(2400, 1080)), "if close button is disabled")

wait(Template(r"tpl1689273618853.png", record_pos=(-0.157, 0.155), resolution=(2400, 1080)))
touch(Template(r"tpl1689273626158.png", record_pos=(-0.162, 0.154), resolution=(2400, 1080)))
assert_exists(Template(r"tpl1689273683838.png", record_pos=(-0.091, 0.043), resolution=(2400, 1080)), "If any mission is available, go in the mission")
touch(Template(r"tpl1689273723948.png", record_pos=(0.141, -0.062), resolution=(2400, 1080)))
exists(Template(r"tpl1689273757218.png", record_pos=(0.227, 0.024), resolution=(2400, 1080)))
touch(Template(r"tpl1689273767484.png", record_pos=(0.464, -0.19), resolution=(2400, 1080)))
assert_not_exists(Template(r"tpl1689273944564.png", record_pos=(0.015, -0.001), resolution=(2400, 1080)), "Showing pop-ups") or assert_not_exists(Template(r"tpl1689274079344.png", record_pos=(0.216, 0.149), resolution=(2400, 1080)), "if close button is disabled")



wait(Template(r"tpl1689273618853.png", record_pos=(-0.157, 0.155), resolution=(2400, 1080)))
touch(Template(r"tpl1689273626158.png", record_pos=(-0.162, 0.154), resolution=(2400, 1080)))
assert_exists(Template(r"tpl1689273683838.png", record_pos=(-0.091, 0.043), resolution=(2400, 1080)), "If any mission is available, go in the mission")
touch(Template(r"tpl1689273723948.png", record_pos=(0.141, -0.062), resolution=(2400, 1080)))
exists(Template(r"tpl1689273757218.png", record_pos=(0.227, 0.024), resolution=(2400, 1080)))
touch(Template(r"tpl1689273767484.png", record_pos=(0.464, -0.19), resolution=(2400, 1080)))
assert_not_exists(Template(r"tpl1689273944564.png", record_pos=(0.015, -0.001), resolution=(2400, 1080)), "Showing pop-ups") or assert_not_exists(Template(r"tpl1689274079344.png", record_pos=(0.216, 0.149), resolution=(2400, 1080)), "if close button is disabled")

sleep(1.0)
swipe(Template(r"tpl1689274661930.png", record_pos=(0.016, 0.156), resolution=(2400, 1080)), vector=[-0.3303, 0.023])
sleep(3.0)

snapshot(msg="Swiped Left")

swipe(Template(r"tpl1689275152261.png", record_pos=(0.033, 0.146), resolution=(2400, 1080)), vector=[0.3322, 0.0303])

sleep(3.0)
snapshot(msg="Swiped Right")

print("passed JIRA-4568")







