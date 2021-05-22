# -*- coding: utf-8 -*-
import json
import logging
from logging.handlers import RotatingFileHandler

from shellproxy import ShellProxy
from stdoutparser import StdoutParser

def init_logger():
    '''initialize logger'''

    # log formatter
    log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

    # log file name
    log_file = 'run.log'

    # max 5 megabyte log file
    my_handler = RotatingFileHandler(log_file, mode='a', maxBytes=2*1024*1024, 
                                    backupCount=2, encoding=None, delay=0)

    # set logging stuff
    my_handler.setFormatter(log_formatter)
    my_handler.setLevel(logging.INFO)

    logger = logging.getLogger('root')
    logger.setLevel(logging.INFO)

    # add handler
    logger.addHandler(my_handler)

    return logger


def run():
    # initialize the application logger
    logger = init_logger()

    # shell and stdout parse objects
    shell = ShellProxy()
    parser = StdoutParser()

    # the json object that will contain all the collected stats
    sepp_stats = {}

    # fetch sepp stats via shell commands and parse stdout

    # uptime
    try:
        sepp_stats['uptime'] = shell.uptime()

    except Exception:
        logger.error('Error fetching uptime', exc_info=True)

    # free memory
    try:
        free_stdout = shell.free_memory()
        free_json = parser.parse_free_memory(free_stdout)
        sepp_stats['mem'] = free_json

    except Exception:
        logger.error('Error fetching memory usage', exc_info=True)

    # cpu usage
    try:
        cpu_stdout = shell.cpu_usage()
        cpu_json = parser.parse_cpu_usage(cpu_stdout)
        sepp_stats['cpu'] = cpu_json

    except Exception:
        logger.error('Error fetching cpu usage', exc_info=True)

    # disk usage
    try:
        disk_stdout = shell.disk_usage()
        disk_json = parser.parse_disk_usage(disk_stdout)
        sepp_stats['disk'] = disk_json

    except Exception:
        logger.error('Error fetching disk usage', exc_info=True)

    # fpga image loaded
    try:
        fpga_stdout = shell.fpga_image_loaded()
        fpga_json = parser.parse_fpga_image_loaded(fpga_stdout)
        sepp_stats['fpga'] = fpga_json

    except Exception:
        logger.error('Error fetching fpga image loaded', exc_info=True)

    # out of memory counter
    try:
        sepp_stats['oom'] = shell.oom_counter()

    except Exception:
        logger.error('Error fetching out of memory counter', exc_info=True)

    # filestore toGround and toGroundLP file count
    try:
        toGround_stdout = shell.toGround_files_counter()
        sepp_stats['toGround'] - toGround_stdout[0]
        sepp_stats['toGroundLP'] =  toGround_stdout[1]

    except Exception:
        logger.error('Error fetching file count in toGround and toGroundLP', exc_info=True)

    # core
    try:
        sepp_stats['core'] = shell.core_counter()

    except Exception:
        logger.error('Error fetching number of cores enabled', exc_info=True)

    # rescue sell status
    try:
        rescue_shell_stdout = shell.rescue_shell_status()
        rescue_shell_status = parser.parse_rescue_shell_status(rescue_shell_stdout)
        sepp_stats['rescue_shell'] = rescue_shell_status

    except Exception:
        logger.error('Error fetching rescue shell status', exc_info=True)

    # write results to json file
    try:
        with open('sepp_stats.json', 'w') as outfile:
            json.dump(sepp_stats, outfile, indent=4)

    except Exception:
        logger.error('Error writing sepp stats to json file', exc_info=True)

if __name__ == '__main__':
    # run the program
    run()