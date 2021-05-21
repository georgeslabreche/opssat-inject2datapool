# -*- coding: utf-8 -*-

class StdoutParser:
    '''Parses given stdout strings'''

    def parse_free_memory(self, stdout):
        '''Parse the stdout string returned from invoking the free command'''

        # split stdout into lines
        stdout_lines = stdout.split('\n')

        # remove blank values from lines
        stats_L1 = list(filter(None, stdout_lines[1].split(' ')))
        stats_L2 = list(filter(None, stdout_lines[2].split(' ')))

        # build json
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