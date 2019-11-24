import subprocess
import shlex
s = 'ls -lh'
cmd = shlex.split(s)
cmd = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,bufsize=0)
data = cmd.stdout.read().decode('utf-8')
print(data)
# cmd = subprocess.Popen('dir',stdout=subprocess.PIPE,stderr=subprocess.PIPE,bufsize=0)
# print(cmd.stdout.flush())
# cmd.stdout.write()
cmd.stdout.flush()
cmd.stdout.readline()
data = cmd.stdout.read()