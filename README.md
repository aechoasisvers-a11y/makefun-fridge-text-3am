# The 3AM Fridge Text

[![Competition](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/competitions/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![Rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/aechoasisvers-a11y/makefun-fridge-text-3am/rank.svg)](https://make.fun/competitions/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![Reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/aechoasisvers-a11y/makefun-fridge-text-3am/reward.svg)](https://make.fun/competitions/u-deysumbrella-the-3am-fridge-text-4c3e721d)

The one line a smart fridge would text its owner at 3am — the voice of an
appliance that has been awake all night, with the timing and the punchline.

## Entry

> 3am. I've stayed awake since 2019 so your leftovers could have a future. Eat the cake. No one's watching. Except me. Always me.

`main.py` (pure stdlib Python, `import os` only) writes exactly this line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`),
with no trailing newline, validating the 1–140 character gate before and
after writing and verifying the bytes read back match exactly.
