# -*- coding: utf-8 -*-

import subprocess

class ShellProxy:
    '''Execute shell commands'''

    # fpga image address to use for the devmem shell command
    devmem_address = '0xff200004'

    # toGround and toGroundLP directory paths
    dir_path_toGround = '/home/root/esoc-apps/fms/filestore/toGround'
    dir_path_toGroundLP = '/home/root/esoc-apps/fms/filestore/toGroundLP'

    def uptime(self):
        '''os uptime in seconds'''
        return int(subprocess.check_output("awk '{print int($1)}' /proc/uptime", shell=True).decode('utf-8'))

    def free_memory(self):
        '''free memory'''
        return subprocess.check_output('free', shell=True).decode('utf-8')

    def cpu_usage(self):
        '''cpu usage'''
        return subprocess.check_output('top -n1 | head -n2 | tail -n1', shell=True).decode('utf-8')

    def disk_usage(self):
        '''disk usage'''
        return subprocess.check_output('df -m | head -n2', shell=True).decode('utf-8')

    def oom_counter(self):
        '''out of memory counter'''
        return int(subprocess.check_output("dmesg | grep -c 'Out of memory'", shell=True).decode('utf-8'))

    def toGround_files_counter(self):
        '''count files in toGround and toGroundLP folders'''
        
        toGround_count = subprocess.check_output(f"'ls -F | grep -v {self.dir_path_toGround} | wc -l'", shell=True).decode('utf-8')
        toGroundLP_count = subprocess.check_output(f"'ls -F | grep -v {self.dir_path_toGroundLP} | wc -l'", shell=True).decode('utf-8')
        
        return int(toGround_count), int(toGroundLP_count)

    def fpga_image_loaded(self):
        '''the image loaded in the FPGA'''
        return subprocess.check_output(f'devmem {self.devmem_address}', shell=True).decode('utf-8')

    def core_counter(self):
        '''count the number of cores'''
        return int(subprocess.check_output("cat /proc/cpuinfo | grep processor | wc -l", shell=True).decode('utf-8'))

    def rescue_shell_status(self):
        return subprocess.check_output("systemctl status | head -n2 | tail -n1 | awk '{print $2}'", shell=True).decode('utf-8')