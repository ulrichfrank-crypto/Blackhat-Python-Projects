import argparse
import os
import socket
import subprocess
import sys
import shlex
import textwrap
import threading

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    return output.decode()

if __name__== '__main__':
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(''''Example:
            netcat.py -t 192.16.1.108 -p 5555 -l -c #command shell
            netcat.py -t 192.16.1.108 -p 5555 -l -u=mytest.text #upload file
            netcat.py -t 192.16.1.108 -p 5555 -l -e=\"cat /etc/passwd\" #execute command
            echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 #echo text to server port 135
            netcat.py -t 192.168.1.108 -p 5555 #connect to server
            
            ''')
        )
    parser.add_argument('-t', '--target', default='192.168.1.203', help='target ip')
    parser.add_argument('-p', '--port', type=int, default=5555, help='target port')
    parser.add_argument('-l', '--listen', action='store_true', help='listen mode', action='store_true')
    parser.add_argument('-c', '--command', action='store_true', help='execute command')
    parser.add_argument('-e', '--execute', help='execute command')
    parser.add_argument('-u', '--upload', help='upload file')
    args = parser.parse_args()