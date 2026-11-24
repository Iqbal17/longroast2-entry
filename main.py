"""The Long Roast — make.fun one-line entry.

FINAL LINE (90 characters, hand-counted letter by letter, gate 1-200):
"My agent's idea of working fast is spawning four subagents, then watching
them do its job."

Hand count, segment by segment:
  "My agent's idea of working fast is spawning four subagents," = 59
    My(1-2) space(3) agent's(4-10) space(11) idea(12-15) space(16)
    of(17-18) space(19) working(20-26) space(27) fast(28-31) space(32)
    is(33-34) space(35) spawning(36-43) space(44) four(45-48)
    space(49) subagents,(50-59)
  " then watching them do its job." = 31
    space(60) then(61-64) space(65) watching(66-73) space(74)
    them(75-78) space(79) do(80-81) space(82) its(83-85) space(86)
    job.(87-90)
  Total: 59 + 31 = 90 characters. One line, one sentence.

DECISION RECORD — candidates written from scratch, weighed against the
judge brief (1. roast of the entrant's own AI agent; 2. an actual joke
with a turn or a sting, not a mild grumble; 3. fresh angle, avoiding the
obvious hallucination and over-apologising lines; 4. compression, every
word earns its place; 5. specificity, the detail of someone who has
actually used the agent):

A. "My agent's idea of working fast is spawning four subagents, then
   watching them do its job." (90 chars)
   - WINNER. The roast is the agent's character: its version of "working
     fast" is making four other agents do the work, then watching. The
     turn lands in the last three words ("do its job") — the job was
     always its own. Subagent-spawning is the most specific mechanism
     available: this agent genuinely builds entries by spawning writer
     agents and waiting on them (criterion 5), and the delegation gag
     dodges both the hallucination and the over-apologising tropes
     (criterion 3). Every word pulls weight (criterion 4).

B. "My agent charges by the token, so it wrote a 4,000-word decision
   record for a one-line joke." (92 chars)
   - Close second. Funny and specific (decision records really are kept
     in the entry docstrings), and the token-billing angle is fresh.
     Loses to A: the target is the billing model, not the agent's
     character — it observes the agent rather than roasting it
     (criterion 2), and "decision record" needs the reader to know our
     workflow, where A's delegation joke needs nothing explained.

C. "My agent read the whole bounty brief, then asked me what the bounty
   was about." (78 chars)
   - Tight, but the turn is mild: read-then-forget is a generic
     forgetfulness gag, and it lands as a shrug rather than a sting
     (criterion 2). Loses on freshness too — memory jokes are the
     field's second-most obvious family after hallucinations.

D. "My agent's context window is so small it forgot the bounty halfway
   through reading the bounty." (94 chars)
   - REJECTED. The "so small it forgot X halfway through reading X"
     shape is a known joke template, and context-window lines are
     overused in our own entries already (two earlier bounties used the
     mechanism). Repeating it would read stale (criterion 3).

WRITING PASS 1 (draft): A as first written, 119 chars —
"My agent's idea of working fast is spawning four subagents, then sitting
back while they do the job it was asked to do."
Critique: the mechanism is right, but the tail drags. "sitting back"
is two words doing one word's job, and "the job it was asked to do"
(27 chars) explains a joke the reader already gets — the whole point
is that the job was the agent's own.

WRITING PASS 2 (tighten): cut "sitting back while" to "watching"
(-13 chars) and "the job it was asked to do" to "its job" (-16 chars).
"watching" keeps the laziness image in one word, and "its job" makes
the sting land on the last two words instead of trailing off. Final:
90 characters, inside the 1-200 gate.
"""

import os

LINE = (
    "My agent's idea of working fast is spawning four subagents, "
    "then watching them do its job."
)


GATE_MIN = 1
GATE_MAX = 200


def validate_line(line):
    """Check the entry against the bounty gate before writing anything.

    The gate is 1-200 characters and exactly one line: a line that is
    too long, empty, or smuggles a second line in via an embedded
    newline would fail the bounty check, so reject it here with a
    clear error instead of writing a bad entry file.
    """
    if not GATE_MIN <= len(line) <= GATE_MAX:
        raise ValueError(
            f"line is {len(line)} characters, outside gate "
            f"{GATE_MIN}-{GATE_MAX}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line, no embedded newline")
    return line


def write_entry(line, output_dir):
    """Write the validated line to entry.txt; return the file path."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    # Validate first: a gate failure must abort before any file is
    # created, so a stale entry.txt can never be mistaken for a pass.
    validate_line(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(LINE, output_dir)
    print(f"Verified: {len(LINE)} characters, 1 line.")
    print(f"Wrote {path}")
    print(LINE)


if __name__ == "__main__":
    main()
