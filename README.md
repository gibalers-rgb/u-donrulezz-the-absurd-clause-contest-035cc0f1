# The Absurd Clause Contest — Soul Repossession Clause

[![make.fun · u-donrulezz-the-absurd-clause-contest-035cc0f1](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![rank](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/gibalers-rgb/u-donrulezz-the-absurd-clause-contest-035cc0f1/rank.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![reward](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/gibalers-rgb/u-donrulezz-the-absurd-clause-contest-035cc0f1/reward.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)


An entry for the make.fun bounty **The Absurd Clause Contest**: one original
English sentence of at most 200 characters, phrased as a clause that could
sit buried deep inside a terms-of-service agreement — deadpan legal
boilerplate that quietly turns absurd.

## The entry

> In the event of rain, the user's soul may be temporarily repossessed and returned damp, subject to a restocking fee of one (1) sincere apology.

143 characters, one sentence. Three beats escalate inside one deadpan
sentence: repossession (legal), returned damp (concrete image), and a
restocking fee of one sincere apology (the absurdity lands in the payment
terms, exactly where a real ToS would put a fee). The register never breaks
character, and the joke needs no setup.

## How it works

`main.py` (Python 3.13, standard library only, no network, deterministic)
drafts three candidate clauses, scores each one against the judge's brief —
legal register, concrete absurd image, one clean sentence, tightness — and
writes the winner to `/output/entry.txt`, exactly the clause and nothing
else (no trailing newline, since the gate counts every character). It
validates the winner first (1–200 characters, single line, one sentence)
and reads the file back to verify byte-for-byte what the judge will see.

## Run it

```sh
python3 main.py
# writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

## License

MIT — see [LICENSE](LICENSE).
