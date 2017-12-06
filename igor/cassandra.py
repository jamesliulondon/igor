from subprocess import PIPE, Popen
import json

resultset = {}
script = """
df -h |awk '/^\//{print $1 " " $8}'
"""

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]


def main(self):
    raw_output = str(cmdline(script)).splitlines()
    for line in raw_output:
        l = str(line).split(" ")
        x = l[0]
        y = l[1]

        resultset.update({x: y})

    return resultset
