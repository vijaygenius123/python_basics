import sys
from variables import *

sys.tracebacklimit = 0


try:
    name
except NameError as err:
    raise SystemExit("Did You name the variable as `name` ?")
    
print("Nice To Meet You {}".format(name))

try:
    sum_of_numbers
except NameError as err:
    raise SystemExit("Did You create the variable  `sum_of_numbers` ?")

print("Nice!! You Have Defined sum_of_numbers")
if(sum_of_numbers==4):
    print("Amazing, It Evaluated  To 4")
else:
    print("Hmmm, Somethings Wrong. Does the expression evaluate to 4??")

try:
    nick_name
except NameError as err:
    raise SystemExit("Did You create the variable  `nick_name` ?")

print("Nice!! You Have Defined nick_name")
if(name==nick_name):
    print("Thats Nice, Your Nick Name Is The Same As Your Name")
else:
    print("Did You Assign The Variable `name` to `nick_name` ??")

print("You Have Passes This Test")


