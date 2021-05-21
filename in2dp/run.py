# -*- coding: utf-8 -*-

from shellproxy import ShellProxy
from stdoutparser import StdoutParser

def run():
    shell = ShellProxy()
    parser = StdoutParser()

    free_stdout = shell.free_memory()
    free_json = parser.parse_free_memory(free_stdout)

    print(free_json)

if __name__ == '__main__':
    run()