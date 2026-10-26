import time


sprite = Sprite('Tobi')
quarky = Quarky()

# Initialize two IR sensors
linefollow = AdvanceLineFollowing(2)

# Configure left and right sensors
linefollow.setlinefollowerparameter('left', 'IR-L')
linefollow.setlinefollowerparameter('right', 'IR-R')

# PID settings from your blocks
linefollow.setPIDconstantparameter(0.85, 0, 1)
linefollow.setPIDspeedparameter(80, 0, 80)

# Turn speed
linefollow.setturingspeed(70)

# Calibrate sensors
linefollow.calibrateir()

time.sleep(5)

#path1
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("right","next")
linefollow.dolinefollowingwithPID(2)
linefollow.turnrobotusingir("right","next")
quarky.drawpattern("aaggaaaagagaaaaaagaaaaaagaaaaggggga")
time.sleep(1)
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("right","next")
linefollow.turnrobotusingir("right","next")
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("left","next")
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("left","next")
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("right","next")
linefollow.turnrobotusingir("right","next")

#path2
linefollow.dolinefollowingwithPID(3)
linefollow.turnrobotusingir("left","next")
linefollow.turnrobotusingir("left","next")

#path4
linefollow.dolinefollowingwithPID(2)
linefollow.turnrobotusingir("right","next")
linefollow.dolinefollowingwithPID(2)
linefollow.turnrobotusingir("right","next")
linefollow.turnrobotusingir("right","next")


linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("left","next")
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("left","next")
linefollow.dolinefollowingwithPID(2)
linefollow.turnrobotusingir("left","next")
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("right","next")
linefollow.turnrobotusingir("right","next")

#path3

linefollow.dolinefollowingwithPID(2)
time.sleep(1)
linefollow.turnrobotusingir("right","next")
linefollow.turnrobotusingir("right","next")
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("left","next")
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("right","next")
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("left","next")
linefollow.dolinefollowingwithPID(1)
time.sleep(1)
linefollow.turnrobotusingir("right","next")
linefollow.turnrobotusingir("right","next")
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("right","next")

#path 5
linefollow.dolinefollowingwithPID(2)
time.sleep(1)
linefollow.turnrobotusingir("right","next")
linefollow.turnrobotusingir("right","next")
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("left","next")
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("left","next")
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("right","next")
linefollow.dolinefollowingwithPID(1)
time.sleep(1)
linefollow.turnrobotusingir("right","next")
linefollow.turnrobotusingir("right","next")
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("right","next")
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("right","next")
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("left","next")
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("right","next")
time.sleep(1)
linefollow.turnrobotusingir("right","next")
linefollow.dolinefollowingwithPID(1)
linefollow.turnrobotusingir("left","next")
linefollow.dolinefollowingwithPID(2)