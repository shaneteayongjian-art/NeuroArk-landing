"""
Run multiple instances of the bot against each other for self‑play training.

Each bot connects to the same training server using a unique join token.  The
admin API must be used beforehand to set up a table that accepts multiple
players.  This script launches several subprocesses executing `run_bot.py`
with different environment tokens; logs are written to `training/logs`.

Usage:

    python training/selfplay.py --players 3 --tokens token1 token2 token3

Ensure that your `.env` file contains base credentials and that each token
corresponds to a registered bot on the training server.
"""
import argparse
import os
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv


def main() -> None:
    parser = argparse.ArgumentParser(description="Run multiple bots for self‑play")
    parser.add_argument("--players", type=int, default=3, help="Number of bot instances")
    parser.add_argument(
        "--tokens", nargs="*", help="List of join tokens for each bot.  If omitted, uses the same token from .env for all players."
    )
    parser.add_argument(
        "--logdir", type=str, default="training/logs", help="Directory to store logs (not yet implemented)"
    )
    args = parser.parse_args()

    load_dotenv()
    base_token = os.getenv("POKER_JOIN_TOKEN")

    if args.tokens:
        tokens = args.tokens
        if len(tokens) < args.players:
            print(f"Provided {len(tokens)} tokens for {args.players} players; fill the rest with the base token.")
            tokens = tokens + [base_token] * (args.players - len(tokens))
    else:
        tokens = [base_token] * args.players

    processes = []
    for i in range(args.players):
        env = os.environ.copy()
        env["POKER_JOIN_TOKEN"] = tokens[i]
        env["BOT_NAME"] = f"SelfPlayBot{i+1}"
        # Launch run_bot.py as a subprocess
        p = subprocess.Popen([sys.executable, "run_bot.py"], env=env)
        processes.append(p)
        print(f"Started bot {i+1} with token {tokens[i][:6]}...")

    try:
        # Wait for all processes to finish
        for p in processes:
            p.wait()
    except KeyboardInterrupt:
        print("Terminating self‑play bots...")
        for p in processes:
            p.terminate()


if __name__ == "__main__":
    main()