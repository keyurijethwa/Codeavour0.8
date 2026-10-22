import time

def main():
    expansion=QuarkyMiniExpansion()
    expansion.miniinitialise()
    
    expansion.runmotor('L',1,80)
    expansion.runmotor('R',2,60)
    
    time.sleep(0.75)
    
    expansion.stoprobot()

main()