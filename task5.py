import time
import config


intellio = QuarkyIntellio()
expansion=QuarkyMiniExpansion()
expansion.miniinitialise()

def main():
    intellio.moveservointime("S1",155,1)
    
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


# Speak when the program initializes
intellio.speakTTS("Code Initialize")

# Keep checking the L button
while True:
    if intellio.readpushbutton(1):
        intellio.speakTTS("Robot start")
        time.sleep(2)
        intellio.speakTTS("Challenge Five start")
        time.sleep(2)
        main()
        intellio.speakTTS("Challenge Five Completed")

        # Wait until L is released
        while intellio.readpushbutton(1):
            time.sleep(0.1)

    time.sleep(0.1)