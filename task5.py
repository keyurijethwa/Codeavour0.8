import time
import config

def main():
    intellio = QuarkyIntellio()
    intellio.moveservointime("S1",155,1)
    expansion=QuarkyMiniExpansion()
    expansion.miniinitialise()
    
    expansion.runmotor(config.LEFT_MOTOR,config.LEFT_MOTOR_FORWARD_DIRECTION,80)
    expansion.runmotor(config.RIGHT_MOTOR,config.RIGHT_MOTOR_FORWARD_DIRECTION,80)
    
    time.sleep(0.75)
    
    expansion.stoprobot()
    intellio.moveservointime("S1",100,1)
    time.sleep(0.3)
    expansion.runmotor(config.LEFT_MOTOR,config.LEFT_MOTOR_BACKWARD_DIRECTION,80)
    expansion.runmotor(config.RIGHT_MOTOR,config.RIGHT_MOTOR_BACKWARD_DIRECTION,80)
    
    time.sleep(1)
    
    expansion.stoprobot()

main()