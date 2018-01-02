import igor.commandline_helper as cmd_hlp
from flask_restful import Resource, Api

resultset = {}
script = """
df -h |awk '/^\//{print $1 " " $8}'
"""


class Diskfree(Resource):
    """
    /diskfree
    """
    def get(self):
        """
        we should name this something other than dummy
        """
        raw_output = str(cmd_hlp.cmdline(script)).splitlines()
        for line in raw_output:
            l = str(line).split(" ")
            x = l[0]
            y = l[1]

            resultset.update({x: y})

        return resultset
