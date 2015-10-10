'''
Created on Apr 9, 2015

@author: Nothing to see here
'''
import wpilib
from RobotMap import instance as RobotMap


class _DriveManager(object):
    '''
    Controls the drive subsystem
    '''
    kP = 0.00005
    kI = 0.000005
    kD = 0.1
    
    
    
    
    
    def deadzone(self, amt, band=0.1):
        if amt < band:
            return 0
        else: return amt
    
    def clamp(self, amt, minimum, maximum):
        return max(minimum, min(maximum, amt))
    
    def __init__(self):
        self.leftMotor = wpilib.Talon(0)
        self.rightMotor = wpilib.Talon(1)
        self.leftSideMotor = wpilib.Talon(2)
        self.rightSideMotor = wpilib.Talon(3)
        
        self.leftEnc = wpilib.Encoder(0, 1)
        self.rightEnc = wpilib.Encoder(2, 3)
        self.leftSideEnc = wpilib.Encoder(4, 5)
        self.rightSideEnc = wpilib.Encoder(6, 7)
        
        self.arcDrive = wpilib.RobotDrive(self.leftMotor, self.rightMotor)
        """
        self.leftController = wpilib.PIDController(self.kP, self.kI, self.kD, self.leftEnc, self.leftMotor)
        self.rightController = wpilib.PIDController(self.kP, self.kI, self.kD, self.rightEnc, self.rightMotor)
        self.leftSideController = wpilib.PIDController(self.kP, self.kI, self.kD, self.leftSideEnc, self.leftSideMotor)
        self.rightSideController = wpilib.PIDController(self.kP, self.kI, self.kD, self.rightSideEnc, self.rightSideMotor)
        
        self.leftController.enable()
        self.rightController.enable()
        self.leftSideController.enable()
        self.rightSideController.enable()
        
        self.leftController.setContinuous(True)
        self.rightController.setContinuous(True)
        self.leftSideController.setContinuous(True)
        self.rightSideController.setContinuous(True)
        
        self.leftController.setInputRange(-5000, 5000)
        self.rightController.setInputRange(-5000, 5000)
        self.leftSideController.setInputRange(-5000, 5000)
        self.rightSideController.setInputRange(-5000, 5000)"""
        
    def update(self,joystick):
        x = self.clamp(joystick.getAxis(wpilib.Joystick.AxisType.kX), -1, 1)
        y = self.clamp(joystick.getAxis(wpilib.Joystick.AxisType.kY), -1, 1)
        z = self.clamp(joystick.getAxis(wpilib.Joystick.AxisType.kZ), -1, 1)
        
        #x = self.deadzone(x, 0.1)
        #y = self.deadzone(y, 0.1)
        #z = self.deadzone(z, 0.1)
        multiplier = wpilib.SmartDashboard.getNumber('multiplier', 0.75)

        left = self.clamp(-y+x, -1, 1)
        right = self.clamp(y+x, -1, 1)
        
        self.leftMotor.set(left * multiplier)
        self.rightMotor.set(right * multiplier)
        
        self.leftSideMotor.set(z * multiplier, 0)
        self.rightSideMotor.set(z * multiplier, 0)
        
    def autoupdate(self, x, y, z):
        x = self.deadzone(x, 0.1)
        y = self.deadzone(y, 0.1)
        z = self.deadzone(z, 0.1)
        
        left = self.clamp(-y + x, -1, 1)
        right = self.clamp(y+x, -1, 1)
        
        self.leftMotor.set(left)
        self.rightMotor.set(right)
        
        self.leftMotor.set(z)
        self.rightMotor.set(z)
        
dminstance = _DriveManager()
            
