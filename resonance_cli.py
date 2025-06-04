#!/usr/bin/env python3
"""CLI to log shard names with timestamps."""
import argparse
from datetime import datetime
from pathlib import Path

LOG_FILE = Path(__file__).parent / "glyphs" / "resonance.log"
GOLD = "\033[38;5;220m"
RESET = "\033[0m"


def log_shard(shard_name: str) -> None:
    """Append a shard entry with timestamp to the resonance log."""
    timestamp = datetime.now().isoformat(timespec="seconds")
    entry = f"{timestamp} - {shard_name}\n"
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(entry)
    print(f"{GOLD}{entry.strip()}{RESET}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Log shard resonance")
    parser.add_argument("shard", nargs="?", help="Shard name to log")
    args = parser.parse_args()
    shard = args.shard or input("Enter shard name: ")
    log_shard(shard)


if __name__ == "__main__":
    main()
