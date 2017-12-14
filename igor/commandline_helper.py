"""
TODO: NAME app
"""
from subprocess import PIPE, Popen

#resultset = {}
#script = """
#df -h |awk '/^\//{print $1 " " $8}'
#"""

def cmdline(command):
    """
    This will get run a commandline execution
    """
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]
