'''
Created on Apr 30, 2015

@author: Nothing to see here
'''
import wpilib

class Lifter(object):
    '''
    Controls the lifter
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        self.lifter = wpilib.Talon(4)
        
    def update(self, amt):
        '''
        Use this in Teleop or Autonomous
        '''
        wpilib.SmartDashboard.putBoolean("Works", True)
        wpilib.SmartDashboard.putNumber("Lifter amount", -amt)
        self.lifter.set(-amt, 0)
        
instance = Lifter()