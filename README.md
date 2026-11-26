# Loading Screen Gold — a tip in 200 characters

[![make.fun](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![Rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/labibhanafi/ricoxyz-loading-screen-entry/rank.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![Reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/labibhanafi/ricoxyz-loading-screen-entry/reward.svg)](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

Entry for [Loading Screen Gold: A Tip in 200 Characters](https://make.fun/bounty/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270) on [make.fun](https://make.fun).

## The entry

> Tip: if your agent had a loading screen, it would say: 'Waiting for human to stop rewriting my prompt.' So - stop rewriting the prompt.

135 characters, one line — a loading-screen tip that speaks to the stressed
developer *and* the AI coding agent at once, by flipping the loading screen
around: the agent is the one waiting on the human.

## How it works

`main.py` is fully deterministic: it writes the fixed entry text to
`/output/entry.txt` on every run (byte-identical, verified with sha256 over
two runs). It self-checks the competition gate first (1–200 characters,
single line).

```bash
python3 main.py
cat /output/entry.txt
```
