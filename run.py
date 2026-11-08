#!/usr/bin/env python3

import argparse
import subprocess
import time
import pathlib

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Execute common tasks (building, testing, ...)')

    language = parser.add_subparsers(dest='language', required=True)
    
    c_parser = language.add_parser('c', help='c project')
    c = c_parser.add_subparsers(dest='domain', required=True)
    
    cpp_parser = language.add_parser('cpp', help='cpp project')
    cpp = cpp_parser.add_subparsers(dest='domain', required=True)

    c_doc = c.add_parser('doc', help='documentation')
    c_doc.add_argument('-b', '--build',
                    action='store_true',
                    help='build documentation')

    arguments = parser.parse_args()

    if arguments.language == 'c':
        if arguments.domain == 'doc':
            commands = 'doxygen'

        #     if arguments.build:
        #         commands = 'cd c && cmake -S . -B build && cmake --build build && cmake -S . --graphviz=build/project.dot && dot -Tpng -o build/project.png build/project.dot'
        #     elif arguments.build_cpp:
        #         commands = 'cd cpp && cmake -S . -B build && cmake --build build && cmake -S . --graphviz=build/project.dot && dot -Tpng -o build/project.png build/project.dot'
    
    this_file_dir = pathlib.Path(__file__).resolve().parent

    cwd = this_file_dir / arguments.language / arguments.domain
    try:
        subprocess.run(commands, cwd=cwd, shell=True, check=True)
    except (subprocess.CalledProcessError, KeyboardInterrupt) as e:
        exit_code = getattr(e, 'returncode', 1)
        exit(exit_code)
