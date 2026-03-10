# Poker Bot (Texas Hold’em AI Competition)

This repository contains a baseline poker bot designed for an AI card‑game tournament.  The bot connects to the tournament server, parses game state from the API, runs a simplified strategy based on counterfactual regret minimisation (CFR) concepts, and returns valid actions within the time limit.  The code is organised for easy extension: you can add more sophisticated abstractions, opponent modelling, or Monte‑Carlo training loops without changing the API client.

## Quick start

1. Install dependencies (Python ≥ 3.10):

   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the project root and copy the contents of `.env.example`.  Fill in your server URL, username, password and one‑time join token:

   ```env
   POKER_BASE_URL=https://gameserver037.poker.tesserac.ai
   POKER_USERNAME=gameserver037
   POKER_PASSWORD=********
   POKER_JOIN_TOKEN=your-registration-token
   BOT_NAME=MyPokerBot
   ```

3. Run the bot:

   ```bash
   python run_bot.py
   ```

During a game the bot will block until it is your turn, compute its decision and immediately send an action back to the server.  It keeps running until the server closes the connection.

## Repository layout

```
pokerbot/
  README.md           – this file
  .env.example        – template for environment variables
  requirements.txt    – Python package dependencies
  run_bot.py          – main entry point for the bot
  api_client.py       – thin wrapper around the tournament’s HTTP API
  adapter.py          – converts server JSON to an internal state and vice versa
  strategy/
    policy.py         – core decision logic (baseline + opponent modelling)
    equity.py         – Monte‑Carlo equity estimation
    abstraction.py    – grouping of states into “buckets”
    opponent.py       – on‑line opponent statistics and range estimation
    icm.py            – risk weighting in elimination rounds
  training/
    selfplay.py       – simple script for running multiple bot instances in self‑play
    mccfr.py          – skeleton for simplified MCCFR training
    logs/             – directory for storing self‑play hand histories
  utils/
    logger.py         – simple logging helper
    config.py         – centralised configuration settings
```

For a detailed guide on how to build, train and tune your bot to maximise performance in the tournament, see the `manual.md` file in the root directory.