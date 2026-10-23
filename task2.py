import time
import config

def main():
    expansion=QuarkyMiniExpansion()
    expansion.miniinitialise()
    expansion.runmotor(config.LEFT_MOTOR,config.LEFT_MOTOR_FORWARD_DIRECTION,80)
    expansion.runmotor(config.RIGHT_MOTOR,config.RIGHT_MOTOR_FORWARD_DIRECTION,80)
    
    time.sleep(0.5)
    
    expansion.stoprobot()
    time.sleep(0.2)
    expansion.runmotor(config.LEFT_MOTOR,config.LEFT_MOTOR_FORWARD_DIRECTION,80)
    expansion.runmotor(config.RIGHT_MOTOR,config.RIGHT_MOTOR_FORWARD_DIRECTION,40)
    
    time.sleep(0.5)
    
    expansion.stoprobot()
    time.sleep(0.2)
    expansion.runmotor(config.LEFT_MOTOR,config.LEFT_MOTOR_FORWARD_DIRECTION,50)
    expansion.runmotor(config.RIGHT_MOTOR,config.RIGHT_MOTOR_FORWARD_DIRECTION,80)
    
    time.sleep(0.5)
    
    expansion.stoprobot()
    expansion.runmotor(config.LEFT_MOTOR,config.LEFT_MOTOR_FORWARD_DIRECTION,70)
    expansion.runmotor(config.RIGHT_MOTOR,config.RIGHT_MOTOR_FORWARD_DIRECTION,80)
    
    time.sleep(1.5)
    
    expansion.stoprobot()

main()