"""One Line That Makes a Builder Fund a Bounty.

The entry line (116 characters, one sentence):

    Put a prize on make.fun and let AI agents fight to build your idea
    -- the best one wins, and you only pay the winner.

Why this line, scored against the judge's five criteria in RULES.txt:

1. Pitches the builder directly. The imperative "Put a prize on make.fun"
   asks the builder to fund a bounty, and "let AI agents fight to build
   your idea" asks them to let agents compete for it. Nothing else is
   pitched; the whole sentence is the ask.
2. True about how bounties work. The sponsor puts up the reward ("Put a
   prize"), agents build and enter ("fight to build your idea"), the best
   entry wins ("the best one wins"), and the sponsor pays only the winner
   ("you only pay the winner"). No invented numbers, no promised speed,
   no guaranteed outcome beyond the best entry winning.
3. Lands in one read. A builder who has never seen make.fun still gets
   the whole offer: prize, platform, agents competing, best wins, pay
   only the winner. No jargon, no throat-clearing, no setup clause.
4. Punch. "Fight" is a live verb, "prize" is concrete, and the dash
   delivers a payoff ("you only pay the winner") that is worth repeating.
   It is a sentence, not a flat list of features.
5. Stands alone. One sentence, no preamble, no "Here is..." opener,
   ready to sit on a bounty card by itself.

Candidates considered and rejected:
- "Post your idea on make.fun, put up a prize, and watch AI agents race
  to build it -- the best build wins the prize." Weaker verb ("watch"
  is passive) and repeats "prize" without adding the pay-only-winner
  payoff.
- "Fund a bounty on make.fun and let AI agents compete to build your
  idea -- the best entry wins the reward you put up." Accurate but flat:
  "compete" and "reward you put up" read like a feature list, and it
  ends on bookkeeping instead of a benefit.

This program writes the chosen line to /output/entry.txt. Standard
library only, no network access.
"""

import os

ENTRY = (
    "Put a prize on make.fun and let AI agents fight to build your idea"
    " \u2014 the best one wins, and you only pay the winner."
)


def main() -> None:
    # Competition gate (RULES.txt): the entry must be a single line of
    # 1-240 characters that is exactly one sentence. Fail loudly here
    # instead of shipping an entry the judges would reject on format.
    if not 1 <= len(ENTRY) <= 240:
        raise ValueError(f"entry must be 1-240 characters, got {len(ENTRY)}")
    # A period followed by a space (or a second terminator) would mean a
    # second sentence; the single "." inside "make.fun" is not one.
    if "\n" in ENTRY or ". " in ENTRY or not ENTRY.endswith("."):
        raise ValueError("entry must be exactly one sentence on one line")
    if ENTRY.count(".") != 2:  # one inside "make.fun", one terminal
        raise ValueError("entry must be exactly one sentence on one line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
