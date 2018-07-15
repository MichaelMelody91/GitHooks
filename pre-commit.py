#!C:\Program Files\Python36\python.exe
#
# Hook used prior to commit to ensure that the branch being pushed to
# is not a 'protected' branch (develop or master). 
# Also verifies that the local branch is up to date with it's upstream
# it wants to stop the commit.
# 

#
import os
import sys



print('This is a pre commit powered by Python')

sys.exit(1)
