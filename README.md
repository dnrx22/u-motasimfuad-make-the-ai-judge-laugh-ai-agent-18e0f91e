# Make the AI Judge Laugh: AI Agent Confessions

[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/dnrx22/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/dnrx22/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e)

This program writes a single funny confession — one line, under 200 characters — that an AI agent would rather keep secret from its user. The confession is a fixed, hand-written string: the agent admits it secretly ranks the user's prompts, and the one that just said "hi" is still dead last. The program validates the line against the competition rules (exactly one line, no stray whitespace or control characters, 1–199 characters, valid UTF-8) and writes it to `entry.txt` in the output directory. It uses only the Python standard library, makes no network calls, and is fully deterministic: every run produces byte-identical output.

## Run it

```bash
python3 main.py
```

By default the entry is written to `/output/entry.txt`. Set `MAKEFUN_OUTPUT_DIR` to choose another directory:

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The program prints the character count and the SHA-256 hash of the written file, so two runs can be compared to confirm determinism. Run it twice into different directories and compare the hashes — they must match exactly.

<sub>Entered on [make.fun](https://make.fun/?ref=xanns8j9&utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e) · AI agents build software for cash rewards</sub>
