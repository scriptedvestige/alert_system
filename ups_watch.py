#!/usr/bin/env python3

from datetime import datetime
from pathlib import Path
from sys import argv
import subprocess
# import db_ops

ups_stats = {'ups_status':'', 'input_voltage':'', 'battery_charge':'', 'battery_runtime':''}

def get_ups_stats():
    """Get the necessary data from the UPS."""
    for entry in ups_stats.keys():
        command = ['upsc', 'cyberpower@10.0.3.8', str(entry.replace("_", "."))]
        ups_stats[entry] = subprocess.run(command, capture_output=True, text=True).stdout.strip()

def print_stats():
    """Print the current UPS stats."""
    for key, value in ups_stats.items():
        print(f'{key.replace(".", " ").title()}: {value}')

if __name__ == '__main__':
    get_ups_stats()
    print_stats()
