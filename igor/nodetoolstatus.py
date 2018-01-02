import igor.commandline_helper as cmd_hlp
from flask_restful import Resource, Api
from jsonmerge import merge

import json, re



script = """
cat igor/nodetoolstatus.txt |awk '{ if ($1 ~ /Datacenter/) { D=$NF }; if ($NF ~ /RACK/) { print D " " $NF " " $1, $2, $3} }'
"""

class Nodetoolstatus(Resource):
    """
            DC1 RACK2 UN 10.137.12.20 18.97
            DC1 RACK3 UN 10.137.12.22 19.02
            DC2 RACK2 UN 10.134.106.23 34.49
            DC2 RACK1 UN 10.134.106.17 30.76
        to
            {DC: {LOCATION: "DC1", HOST: {"IP": IP, RACK: "RACK1" , STATE: "DL" , LOAD: "34" }}
            {DC: {LOCATION: "DC2", HOST: {"IP": IP, RACK: "RACK1" , STATE: "DL" , LOAD: "34" }}
    """
    def get(self):
        """
        we should name this something other than dummy
        """

        raw_output = str(cmd_hlp.cmdline(script)).splitlines()
        json_data =    {}
        for node_tool_line in raw_output:
            node_output_line_list = str(node_tool_line).split(" ")
            node_dc = node_output_line_list[0]
            node_rack = node_output_line_list[1]
            node_state = node_output_line_list[2]
            node_ip = node_output_line_list[3]
            node_load = float(node_output_line_list[4])
            #json_data[node_ip] = {"DC": {"LOCATION": node_dc, "HOST": {"IP": node_ip , "RACK": node_rack, "STATE": node_state, "LOAD": node_load}}}
            #node_line={node_dc: {'LOCATION': node_dc, node_ip: { 'RACK': node_rack, 'STATE': node_state, 'LOAD': node_load}}}
            node_line={node_dc: {"LOCATION": node_dc, node_ip: { "RACK": node_rack, "STATE": node_state, "LOAD": node_load}}}
            j_data=merge(json_data,node_line)
            json_data=j_data

        return json_data