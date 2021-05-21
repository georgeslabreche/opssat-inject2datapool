# -*- coding: utf-8 -*-

import subprocess

class ShellProxy:
    '''Execute shell commands'''

    def uptime(self):
        '''os uptime in seconds'''
        return int(subprocess.check_output("awk '{print int($1)}' /proc/uptime", shell=True).decode('utf-8'))

    def free_memory(self):
        '''free memory'''
        return subprocess.check_output('free', shell=True).decode('utf-8')

    def cpu_usage(self):
        '''cpu usage'''

        # todo: top -n1 | head -n2
        pass

    def disk_usage(self):
        '''disk usage'''

        # todo: df -m | head -n2
        pass

    def oom_counter(self):
        '''out of memory counter'''
        return int(subprocess.check_output("dmesg | grep -c 'Out of memory'", shell=True).decode('utf-8'))

    def toGround_files_counter(self):
        '''count files in toGround and toGroundLP folders'''
        
        toGround_count = subprocess.check_output("'ls -F | grep -v /home/root/esoc-apps/fms/filestore/toGround | wc -l'", shell=True).decode('utf-8')
        toGroundLP_count = subprocess.check_output("'ls -F | grep -v /home/root/esoc-apps/fms/filestore/toGroundLP | wc -l'", shell=True).decode('utf-8')
        
        return int(toGround_count), int(toGroundLP_count)

    def fpga_image_loaded(self):
        '''the image loaded in the FPGA'''
        # todo: devmem 0xff200004
        pass

    def is_dual_core(self):
        '''is dual core enabled'''
        return int(subprocess.check_output("cat /proc/cpuinfo | grep processor | wc -l", shell=True).decode('utf-8'))
