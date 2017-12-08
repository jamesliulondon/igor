import igor.commandline_helper as cmd_hlp

resultset = {}
script = """
df -h |awk '/^\//{print $1 " " $8}'
"""


def main(self):
    raw_output = str(cmd_hlp.cmdline(script)).splitlines()
    for line in raw_output:
        l = str(line).split(" ")
        x = l[0]
        y = l[1]

        resultset.update({x: y})

    return resultset
