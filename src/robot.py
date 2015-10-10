#!/usr/bin/env python3

import wpilib
#from DriveManager import DriveManager
'''
Created on Apr 9, 2015

@author: Nothing to see here
'''
#import DriveManager as drive    
from DriveManager import dminstance as drive
#from Lifter import instance as lifter

def Drive():
    return drive

#def Lifter():
    #return lifter
    

class MyRobot(wpilib.IterativeRobot):
    passed = False
    autoTimer = wpilib.Timer()
    
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        #self.lift = Lifter()
        self.drive = Drive()
        self.drivejoystick = wpilib.Joystick(0)
        self.lifterjoystick = wpilib.Joystick(1)
        self.lifter = wpilib.Talon(4)
        wpilib.SmartDashboard.putNumber("multiplier", 0.75)
        wpilib.SmartDashboard.putNumber("lifterState", 0)
        self.lifterState = 0 #0 means not moving, 1 means moving
        
    def autonomousInit(self):
        """This method is called when autonomous is first entered."""
        self.passed = False
        self.autoTimer.start()
        print("Entered autonomous safely!")

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        if not self.passed and not self.autoTimer.hasPeriodPassed(7):
            self.drive.autoupdate(0, 0.5, 0)
            self.passed = True
        else:
            self.drive.autoupdate(0, 0, 0)
    
    def teleopInit(self):
        """ This function is called when teleop is first entered """
        self.autoTimer.stop()
        wpilib.IterativeRobot.teleopInit(self)

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drive.update(self.drivejoystick)
        if self.drivejoystick.getRawButton(3) and not self.drivejoystick.getRawButton(1):
            self.lifter.set(1)
            self.lifterState = 1
        elif not self.drivejoystick.getRawButton(3) and self.drivejoystick.getRawButton(1):
            self.lifter.set(-1)
            self.lifterState = 1
        elif not self.drivejoystick.getRawButton(3) and not self.drivejoystick.getRawButton(1):
            self.lifter.set(0)
            self.lifterState = 0
        elif self.drivejoystick.getRawButton(3) and self.drivejoystick.getRawButton(1):
            self.lifter.set(0)
            self.lifterState = 0
        wpilib.SmartDashboard.putNumber("lifterState", lifterState)
        

    def testPeriodic(self):
        """This function is called periodically during test mode."""

if __name__ == "__main__":
    wpilib.run(MyRobot)
