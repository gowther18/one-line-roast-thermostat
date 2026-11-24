"""One-Line Roast: The Gadget You Use Every Day.

Writes one roast line to /output/entry.txt. The target is the smart
thermostat: it learned the household routine, so it waits until the
room is finally comfortable and then changes the temperature anyway.
The sting lands at the end -- the thermostat is the only roommate
who gaslights its owner about the weather. Every clause is an
everyday truth (smart thermostats learn schedules; they adjust on
their own; the room never stays the temperature you want), and the
joke turns on a device whose whole job is comfort making its owner
less comfortable on purpose.
"""

from pathlib import Path

TEXT = (
    "My smart thermostat learned my routine, so now it waits until "
    "I'm comfortable and changes the temperature \u2014 the only "
    "roommate who gaslights me about the weather."
)


# The competition accepts a single line of 1 to 200 characters.
# A newline would break the "one line" part of the brief even if the
# character count fits, so the gate rejects one as well.
MIN_CHARS = 1
MAX_CHARS = 200


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry text must be a single line")


def main() -> None:
    check_length(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
