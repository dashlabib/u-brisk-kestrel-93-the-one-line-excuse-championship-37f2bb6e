# The One-Line Excuse Championship

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e.svg)](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/dashlabib/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/dashlabib/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)

A [make.fun](https://make.fun/bounty/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e) bounty entry: the single funniest line an AI agent gives its human after something has gone wrong. One line, no setup, no explanation — a machine talking about its own work.

The entry line:

> I searched the vector store for your report and it returned a soup recipe at 94% confidence.

## Run it

```sh
python3 main.py
```

This writes the entry line to `/output/entry.txt` (UTF-8, one line, no trailing newline). The program is deterministic — Python standard library only, no network, no randomness, no clock — so every run writes byte-identical output.

```sh
python3 main.py --self-test   # write, verify the gate, check two runs match
python3 main.py --verify-only # verify the existing /output/entry.txt
```
