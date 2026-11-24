"""The Robot Apology -- make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes one two-line robot confession to entry.txt in the output directory
($MAKEFUN_OUTPUT_DIR, default /output). Line one apologises in a single
sentence for one specific mistake; line two says, in one sentence, what the
robot learned and what it will do differently. Pure standard library.
"""

import os

LINE_ONE = (
    "I am sorry I set your alarm for six in the evening instead of six in "
    "the morning, so you slept through the interview you had ironed a shirt for."
)

LINE_TWO = (
    "I have learned that the hour is not a detail I can guess, so from now "
    "on I will repeat it back to you, six in the morning, before I set anything."
)

TEXT = LINE_ONE + "\n" + LINE_TWO


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    print("Wrote %d characters to %s" % (len(TEXT), path))


if __name__ == "__main__":
    main()
