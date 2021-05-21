# -*- coding: utf-8 -*-

from enum import Enum

class RescueShellStatus(Enum):
    RUNNING     = 0
    MAINTENANCE = 1
    DEGRADED    = 2
    OTHER       = 3

class StdoutParser:
    '''Parses given stdout strings'''

    def parse_free_memory(self, stdout):
        '''Parse the stdout string returned from invoking the free command'''

        # split stdout into lines
        stdout_lines = stdout.split('\n')

        # remove blank values from lines
        stats_L1 = list(filter(None, stdout_lines[1].split(' ')))
        stats_L2 = list(filter(None, stdout_lines[2].split(' ')))

        # build json object
        stats_json = {
            'total': int(stats_L1[1]),
            'used': int(stats_L1[2]),
            'free': int(stats_L1[3]),
            'shared': int(stats_L1[4]),
            'buffers': int(stats_L1[5]),
            'cached': int(stats_L1[6]),
            'used_minus_bufferscache': int(stats_L2[2]),
            'free_plus_bufferscache': int(stats_L2[3])
        }

        # return json
        return stats_json

    def parse_cpu_usage(self, stdout):
        # split stdout line into list of non-Empty substrings
        stats = list(filter(None, stdout.split(' ')))
        
        # remove all '%' characters
        stats = [s.replace('%', '') for s in stats]

        # build json object
        stats_json = {
            'usr': int(stats[1]),
            'sys': int(stats[3]),
            'nic': int(stats[5]),
            'idle': int(stats[7]),
            'io': int(stats[9]),
            'irq': int(stats[11]),
            'sirq': int(stats[13])
        }

        return stats_json

    def parse_disk_usage(self, stdout):
        '''Parse the stdout string returned from invoking the disk usage command'''

        # split stdout into lines
        stdout_lines = stdout.split('\n')

        # remove blank values from lines
        stats = list(filter(None, stdout_lines[1].split(' ')))

        # build json object
        stats_json = {
            'size': int(stats[1]),
            'used': int(stats[2]),
            'available': int(stats[3]),
            'available_percentage': int(stats[4].replace('%', ''))
        }

        return stats_json

    def parse_fpga_image_loaded(self, stdout):
        '''Parse the stdout string returned from invoking the devmem command'''

        if stdout == 'Bus error (core dumped)':
            return 0xffffffff
        else:
            return int(stdout, 16)

    def parse_rescue_shell_status(self, stdout):
        '''Parse the stdout string returned from invoking the rescue shell status command'''

        if stdout == 'running':
            return RescueShellStatus.RUNNING
        elif stdout == 'maintenance':
            return RescueShellStatus.MAINTENANCE
        elif stdout == 'degraded':
            return RescueShellStatus.DEGRADED
        else:
            return RescueShellStatus.OTHER