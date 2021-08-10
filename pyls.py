#!/usr/bin/env python3f = open("/home/kantsler/Desktop/project/index.html", 'w')
import subprocess
import string
import re
my_list = list()
a = "Information about directory:  "
my_list.append(a)
b = str(subprocess.check_output(['pwd']))
my_list.append(b)
c = "Information about the operation system:   "
my_list.append(c)
d = subprocess.check_output(["uname", "-o"])
my_list.append(d)
i = "mywork"
my_list.append(i)
with open("/home/kantsler/Desktop/project/index.html", 'w') as f:
	for x in my_list:
		f.write(str(x) + '\n')

