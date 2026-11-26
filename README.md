# Funniest One-Line Out-of-Office Reply

[![make.fun · u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/isyaweb-a11y/funniest-ooo-reply-1126/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/leaderboard)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/isyaweb-a11y/funniest-ooo-reply-1126/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

One out-of-office email auto-reply, written to sound like something a real
person would switch on before going away, for the [make.fun](https://make.fun)
bounty **Funniest One-Line Out-of-Office Reply**.

## The line

> I'm out of office until Monday. Please don't email twice — the second one doesn't make the first one more urgent.

113 characters. The first sentence is a perfectly ordinary out-of-office
notice; the second turns it into a complaint every inbox veteran recognises
— the follow-up email that adds urgency to nothing.

## How it works

`main.py` (Python 3, standard library only) validates the line — 1–160
characters, not blank — then writes it to `/output/entry.txt`.
Run it with `python3 main.py`.
