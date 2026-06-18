#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path
from sys import argv

LOG_FILE = Path(__file__).parent / "events.log"

def main():
    event_type = argv[1] if len(argv) > 1 else "UNKNOWN"
    with LOG_FILE.open("a") as f:
        f.write(f"{datetime.now().isoformat()} {event_type}\n")

if __name__ == "__main__":
    main()
