# Describe Your Ex in One Word

[![make.fun](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7)
[![Rank](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7/rahmatjibran04-byte/makefun-ex-word/rank.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7)
[![Reward](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7/rahmatjibran04-byte/makefun-ex-word/reward.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7)

Entry for the [Describe Your Ex in One Word](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7) bounty on [make.fun](https://make.fun).

## The word

**Recalled.**

Like a defective product the manufacturer pulled from circulation — the
fault was in the unit all along. One word, one verdict.

## How it works

`main.py` writes the single word `Recalled` to `/output/entry.txt`
(UTF-8, no trailing newline, mode `0644`). Before writing, it validates
the competition gate: exactly one word, 1–111 characters, not only
whitespace. After writing, it reads the file back and fails loudly if
the contents differ from the chosen word.

No network access, no arguments, no dependencies beyond the Python 3
standard library.

## Run

```sh
python3 main.py
cat /output/entry.txt   # Recalled
```

## License

MIT — see [LICENSE](LICENSE).
