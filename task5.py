import time

def main():
    intellio = QuarkyIntellio()
    intellio.moveservointime("S1",155,1)
    expansion=QuarkyMiniExpansion()
    expansion.miniinitialise()
    
    expansion.runmotor('L',1,80)
    expansion.runmotor('R',2,80)
    
    time.sleep(0.75)
    
    expansion.stoprobot()
    intellio.moveservointime("S1",100,1)
    time.sleep(0.3)
    expansion.runmotor('L',2,80)
    expansion.runmotor('R',1,80)
    
    time.sleep(1)
    
    expansion.stoprobot()

main()