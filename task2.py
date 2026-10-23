import time
import config


intellio = QuarkyIntellio()
expansion=QuarkyMiniExpansion()
expansion.miniinitialise()

def main():
    
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

# Speak when the program initializes
intellio.speakTTS("Code Initialize")

# Keep checking the L button
while True:
    if intellio.readpushbutton(1):
        intellio.speakTTS("Robot start")
        time.sleep(2)
        intellio.speakTTS("Challenge Two start")
        time.sleep(2)
        main()
        intellio.speakTTS("Challenge Two Completed")

        # Wait until L is released
        while intellio.readpushbutton(1):
            time.sleep(0.1)

    time.sleep(0.1)