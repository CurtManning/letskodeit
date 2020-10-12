#!/bin/env python3
"""

Usage: 'ltflaskctl.py upgrade' on webapp01 to upgrade to the latest tag

"""
import os
import socket
import sys

def main():
    HOSTNAME = socket.gethostname().lower()
    print("Hostname = " + HOSTNAME)

if __name__ == '__main__':
    main()