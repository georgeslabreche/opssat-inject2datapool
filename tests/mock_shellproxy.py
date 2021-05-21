# -*- coding: utf-8 -*-

class MockShellProxy:
    def uptime(self):
        return 40112

    def free_memory(self):
        return \
            '             total       used       free     shared    buffers     cached\n' \
            'Mem:       1026800     198248     828552       1068       6952      71672\n' \
            '-/+ buffers/cache:     119624     907176\n' \
            'Swap:            0          0          0'