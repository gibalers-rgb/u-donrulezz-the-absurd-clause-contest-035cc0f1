#!/usr/bin/env python3
"""The Absurd Clause Contest — entry program.

Writes one original English sentence (<= 200 characters) to
/output/entry.txt: a deadpan terms-of-service clause that quietly turns
absurd. No network, no dependencies, deterministic.

The program drafts several clauses, scores each one against the judge's
brief (most important first), and writes the winner. The brief, in order:
  1. reads as a clause buried deep in a ToS agreement;
  2. funny on one reading, no outside setup;
  3. real legal boilerplate register until the absurdity hits;
  4. one concrete absurd image, not a vague shrug at the genre;
  5. one tight sentence, no wasted words, no explaining its own joke.
"""

import os
import sys

MAX_CHARS = 200

# Legal-register markers: words a real ToS clause would actually use.
LEGAL_WORDS = (
    "shall", "hereby", "pursuant", "subject to", "in the event of",
    "retained", "repossessed", "security deposit", "restocking fee",
    "upon termination", "within", "days",
)

# Drafts, each tagged with the concrete absurd image it turns on.
# (clause, absurd image)
CANDIDATES = [
    (
        "Upon termination, the user shall return all borrowed moonlight "
        "in its original container, undamaged, within fourteen (14) days "
        "of the final lunar eclipse.",
        "borrowed moonlight returned in its container",
    ),
    (
        "The user agrees that their shadow shall be retained by the "
        "Company as a security deposit and returned only in daylight, "
        "folded, within thirty (30) days.",
        "a shadow kept as a security deposit, returned folded",
    ),
    (
        "In the event of rain, the user's soul may be temporarily "
        "repossessed and returned damp, subject to a restocking fee "
        "of one (1) sincere apology.",
        "a soul repossessed, returned damp, fee paid in apology",
    ),
]


def score(clause: str, image: str) -> int:
    """Score a draft on the judge's criteria (higher is better).

    Legal register (+1 per legal marker, capped), concrete image (+2),
    single clean sentence (+1), tightness (+1 if under 160 chars).
    Invalid drafts (too long, not one sentence) score below zero and
    can never win.
    """
    text = clause.strip()
    if not text or len(text) > MAX_CHARS:
        return -100
    if text.count(".") != 1 or not text.endswith("."):
        return -100
    if "\n" in text:
        return -100
    points = 0
    lowered = text.lower()
    points += min(sum(1 for w in LEGAL_WORDS if w in lowered), 4)
    if image:
        points += 2  # concrete absurd image, specific not vague
    points += 1  # one clean sentence
    if len(text) <= 160:
        points += 1  # tight, no wasted words
    return points


def pick_winner():
    """Draft, test and rewrite: return the best-scoring clause."""
    ranked = sorted(
        ((score(text, image), text) for text, image in CANDIDATES),
        key=lambda item: (-item[0], len(item[1])),
    )
    best_score, best = ranked[0]
    if best_score < 0:
        raise ValueError("no draft passed the gate")
    return best, best_score, ranked


def validate(text: str) -> None:
    """Enforce the sealed scorer's gate: UTF-8, 1-200 chars, not blank."""
    if not text or not text.strip():
        raise ValueError("entry is empty or whitespace only")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    # One clean sentence: exactly one sentence-ending period, at the end.
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in '.'")


def main() -> int:
    clause, best_score, ranked = pick_winner()
    validate(clause)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts every character, so the file
    # holds exactly the clause and nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(clause)
    # Read back and verify byte-for-byte what the judge will see.
    with open(path, encoding="utf-8", newline="") as f:
        written = f.read()
    if written != clause:
        raise ValueError("round-trip check failed: file differs from clause")
    print("draft scores (best first):")
    for s, text in ranked:
        print(f"  {s}: {text[:60]}...")
    print(f"wrote {path} ({len(clause)} characters, score {best_score})")
    print(clause)
    return 0


if __name__ == "__main__":
    sys.exit(main())
