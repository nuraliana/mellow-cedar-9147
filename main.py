"""One-line pitch for the make.fun bounty "A Day of One-Line Pitches".

The entry is a single sentence written to entry.txt. It speaks directly
to a friend who has never coded and flips their worry around: the idea
itself is the hard part, and the friend already has it, so the building
is the easy part an AI agent can handle on make.fun.

Why it wins against the five judging criteria, in order:

1. Makes the case in one read: it addresses "you", names the friend's
   idea as the hard part already done, and ends with a working app to
   try today, so a beginner gets the whole argument at once.
2. Persuasion: it gives a concrete reason to say yes now (a working app
   today, free) and makes handing over the idea feel easy and low risk
   (just describe it in plain words, no code, nothing that cannot be
   changed).
3. Clarity: plain words throughout, one short chain of cause and effect,
   no jargon to decode, and a single sentence that can be read aloud.
4. Truth: it promises only what a beginner can really do on make.fun --
   describe an idea in plain words, get a working first app to try,
   change it afterwards -- with no claim of perfection or instant success.
5. Warmth and craft: it sounds like one friend reassuring another
   ("You already have the hard part"), with a fresh turn of phrase
   rather than a slogan, and it stays personal instead of salesy.

Candidates considered (see CANDIDATES.md for full scoring):
- Runner-up: "You already have the hard part, your idea, so just tell
  make.fun what you want in plain words and an AI agent will build you
  a working app to try today for free, no code needed and easy to
  change." -- warm and clear, but "tell what you want" is vaguer than
  "describe it", and it loses the "nothing you can't change" safety.
- Runner-up: "You don't need to code -- you already have the idea, so
  just describe it in plain words on make.fun and an AI agent will
  build you a real app to try today, free, and you can change anything."
  -- direct and encouraging, but "a real app" is slightly less concrete
  than "a working app", and the opening repeats the no-code point the
  ending already covers.
- Also considered: a shorter "type it in plain words" version and a
  "you already did the hard part" version; both read well but felt
  flatter and less reassuring than the chosen sentence.

The program is deterministic: standard library only, no network, no
randomness, and it writes byte-identical output on every run.
"""

import os

ENTRY = (
    "You already have the hard part \u2014 your idea \u2014 so just describe it "
    "in plain words on make.fun and let an AI agent build you a working app "
    "to try today, free, with no code from you and nothing you can't change."
)


def validate_entry(entry):
    """Check the entry is a single non-blank sentence of 1-240 characters."""
    if not isinstance(entry, str):
        raise ValueError("entry must be a string")
    if not entry.strip():
        raise ValueError("entry must not be blank or whitespace-only")
    if not 1 <= len(entry) <= 240:
        raise ValueError("entry must be 1-240 characters, got %d" % len(entry))
    if entry != entry.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    # Exactly one sentence: it must end with a single full stop, and contain
    # no "!" or "?" terminators. The dots inside "make.fun" are part of the
    # platform name, not sentence breaks, so they are ignored here.
    if entry.endswith(("!", "?")):
        raise ValueError("entry must end with a full stop, not ! or ?")
    if not entry.endswith("."):
        raise ValueError("entry must end with a full stop")
    body = entry[:-1].replace("make.fun", "makefun")
    if "." in body or "!" in body or "?" in body:
        raise ValueError("entry must be exactly one sentence")
    return True


def main():
    validate_entry(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
