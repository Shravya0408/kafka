
from subprocess import *
import subprocess
import time
import random
def leader_election():
    broker_list =[2,3]
    new_broker = random.choice(broker_list)
    print(new_broker)
    return(new_broker)


p= subprocess.Popen('python broker1.py',stdout=PIPE,stderr=PIPE)
time.sleep(3)
p.kill()
print("BROKER HAS DIED")
#print("killed")
time.sleep(7)
#pick random
newBroker = leader_election()
if newBroker==2:
    q = Popen('python broker2.py')
else:
    r = Popen('python broker3.py')
