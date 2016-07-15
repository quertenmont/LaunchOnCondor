#!/usr/bin/env python

import urllib
import string
import os
import sys
import LaunchOnCondor
import glob

LaunchOnCondor.Jobs_InitCmds       = ['ulimit -c 0;']  #disable production of core dump in case of job crash

FarmDirectory = "FARM"
JobName = "Test"
LaunchOnCondor.Jobs_Queue = "8nh"
LaunchOnCondor.SendCluster_Create(FarmDirectory, JobName)
for i in range (1,10) :
   LaunchOnCondor.SendCluster_Push(["BASH", "echo  '" + str(i) + "'"])
LaunchOnCondor.SendCluster_Submit()
