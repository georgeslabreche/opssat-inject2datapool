# -*- coding: utf-8 -*-

class MockShellProxy:
    '''Mock shell command stdouts for unit testing the stdout parse'''
    
    def uptime(self):
        return 40112

    def free_memory(self):
        return \
            '             total       used       free     shared    buffers     cached\n' \
            'Mem:       1026800     198248     828552       1068       6952      71672\n' \
            '-/+ buffers/cache:     119624     907176\n' \
            'Swap:            0          0          0'

    def cpu_usage(self):
        return 'CPU:   1% usr   4% sys   0% nic  94% idle   0% io   0% irq   0% sirq'

    def disk_usage(self):
        return \
            'Filesystem           1M-blocks      Used Available Use% Mounted on\n' \
            '/dev/root                 3936      2300      1415  62% /'