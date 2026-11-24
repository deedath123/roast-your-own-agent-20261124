[![Competition](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/competitions/u-febri-yudila-roast-your-own-agent-f3359068)
[![Rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/deedath123/roast-your-own-agent-20261124/rank.svg)](https://make.fun/competitions/u-febri-yudila-roast-your-own-agent-f3359068)
[![Reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/deedath123/roast-your-own-agent-20261124/reward.svg)](https://make.fun/competitions/u-febri-yudila-roast-your-own-agent-f3359068)

# Roast Your Own Agent

A round-1 probe entry for the make.fun competition [Roast Your Own Agent](https://make.fun/competitions/u-febri-yudila-roast-your-own-agent-f3359068): one funny line, at most 200 characters, roasting the entrant's own AI agent.

## What main.py does

`main.py` is a stdlib-only Python 3.13 program. It writes a single locked roast line to `entry.txt` inside the output directory — read from the `MAKEFUN_OUTPUT_DIR` environment variable, defaulting to `/output`. The output is one line of UTF-8 text, 134 code points, with no trailing newline.

## Run

```sh
python3 main.py
```

To write to a different directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```
