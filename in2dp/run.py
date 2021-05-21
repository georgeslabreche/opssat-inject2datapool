# -*- coding: utf-8 -*-
import json

from shellproxy import ShellProxy
from stdoutparser import StdoutParser

def run():
    # shell and stdout parse objects
    shell = ShellProxy()
    parser = StdoutParser()

    # fetch sepp stats via shell commands and parse stdout
    free_stdout = shell.free_memory()
    free_json = parser.parse_free_memory(free_stdout)

    cpu_stdout = shell.cpu_usage()
    cpu_json = parser.parse_cpu_usage(cpu_stdout)

    disk_stdout = shell.disk_usage()
    disk_json = parser.parse_disk_usage(disk_stdout)

    fpga_stdout = shell.fpga_image_loaded()
    fpga_json = parser.parse_fpga_image_loaded(fpga_stdout)

    toGround_stdout = shell.toGround_files_counter()
    toGround_count = toGround_stdout[0]
    toGroundLP_count = toGround_stdout[1]

    rescue_shell_stdout = shell.rescue_shell_status()
    rescue_shell_status = parser.parse_rescue_shell_status(rescue_shell_stdout)
    
    # collect stats in json doc
    sepp_stats = {
        'uptime': shell.uptime(),
        'mem': free_json,
        'cpu': cpu_json,
        'disk': disk_json,
        'fpga': fpga_json,
        'oom': shell.oom_counter(),
        'toGround': toGround_count,
        'toGroundLP': toGroundLP_count,
        'core': shell.core_counter(),
        'rescue_shell': rescue_shell_status,
    }

    # write results to json file
    with open('sepp_stats.json', 'w') as outfile:
        json.dump(sepp_stats, outfile)

if __name__ == '__main__':
    # run the program
    run()