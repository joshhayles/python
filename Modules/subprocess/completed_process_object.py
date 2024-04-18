import subprocess

# command
command = ["ls", "-l"]

# execute command
result = subprocess.run(command, capture_output=True, text=True)

print(result.stdout)

# output
"""
total 0
drwxr-xr-x  6 joshhayles  staff  192 Jan 31 01:41 DSAs
drwxr-xr-x  2 joshhayles  staff   64 Jan 17 21:08 Debugging
drwxr-xr-x  2 joshhayles  staff   64 Jan 17 21:05 Lists
drwxr-xr-x  3 joshhayles  staff   96 Feb 26 19:42 Methods
drwxr-xr-x  4 joshhayles  staff  128 Apr 18 12:33 Modules
drwxr-xr-x  2 joshhayles  staff   64 Jan 18 05:43 OOP
drwxr-xr-x  3 joshhayles  staff   96 Feb 16 07:17 Sets
drwxr-xr-x  2 joshhayles  staff   64 Jan 16 08:58 Strings
drwxr-xr-x  2 joshhayles  staff   64 Jan 17 21:08 Testing
drwxr-xr-x  2 joshhayles  staff   64 Jan 17 21:05 Tuples
"""