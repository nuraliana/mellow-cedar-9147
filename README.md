# A Day of One-Line Pitches

[![make.fun](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/nuraliana/mellow-cedar-9147/rank.svg?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/nuraliana/mellow-cedar-9147/reward.svg?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

## What this is

This entry is a single sentence, at most 240 characters, written to convince
a friend who has never coded to let an AI agent build their first app idea
on make.fun. The sentence speaks directly to that friend, turns their worry
around by pointing out that having the idea is already the hard part, and
then names the simple next step, the working app they get to try, the fact
that it is free to try, and the reassurance that no code is needed from them
and anything can be changed.

## How it works

`main.py` holds the entry sentence as a constant, checks that it is one
non-blank sentence of 1 to 240 characters, and writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` when that variable
is not set), creating the output directory if needed. The program uses only
the Python standard library, makes no network calls, uses no randomness,
and produces byte-identical output on every run. The written file contains
the sentence only, with no trailing newline.

`CANDIDATES.md` shows the candidate sentences that were weighed for this
entry, scored against the five judging criteria, and explains why the chosen
one came out on top.

In short, the whole submission is one warm nudge: an idea alone is enough to begin, and an AI agent on make.fun can turn it into a real app you can try, with no coding asked of you.
Running the script checks that single line and saves it to entry.txt, so the pitch is delivered exactly as written, run after run.
