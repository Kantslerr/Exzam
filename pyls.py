#!/usr/bin/env python3f = open("/home/kantsler/Desktop/project/index.html", 'w')
import subprocess
import string
import re
my_list = list()
a = str(subprocess.check_output(["pwd"]))
a = re.sub("[(|)|']" , "" ,a)
z = "Information about directory:  ", a
my_list.append(z)
b =str(subprocess.check_output(["uname", "-o"]))
c = "Information about the operation system:   ", b
my_list.append(c)
with open("/home/kantsler/Desktop/project/index.html", 'w') as f:
	for x in my_list:
		f.write(str(x) + "\n")
