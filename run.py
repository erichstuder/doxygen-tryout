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

    c_doc = c.add_parser('tests', help='tests')
    c_doc.add_argument('-t', '--test',
                    action='store_true',
                    help='run tests')

    arguments = parser.parse_args()

    if arguments.language == 'c':
        if arguments.domain == 'doc':
            if arguments.build:
                commands = ' cd c/doc/ '
                commands += ' && doxygen'
        elif arguments.domain == 'tests':
            if arguments.test:
                commands = 'cmake -S . -B build'
                commands += ' && cmake --build build'
                commands += ' && cd build && ctest --output-on-failure'
    elif arguments.language == 'cpp':
        pass # not yet implmented
    
    this_file_dir = pathlib.Path(__file__).resolve().parent
    try:
        subprocess.run(commands, cwd=this_file_dir, shell=True, check=True)
    except (subprocess.CalledProcessError, KeyboardInterrupt) as e:
        exit_code = getattr(e, 'returncode', 1)
        exit(exit_code)
