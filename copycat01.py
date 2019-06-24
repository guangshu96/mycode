#!/usr/bin/python3

import shutil
import os

os.chdir('/home/student/mycode')
shutil.copy('5g_research/sdn_network.txt', '5g_research2/sdn_network.txt')
shutil.copytree('5g_research', '5g_researchbackup')
