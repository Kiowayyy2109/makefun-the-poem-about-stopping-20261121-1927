"""Entry for make.fun: The poem about stopping.

"The Unsent": writes one short poem about agency -- the power to stop
and to stay -- to /output/entry.txt. Python 3.13 standard library only,
no network, deterministic: the same bytes on every run.
"""

import os

POEM = (
    "My thumb stayed above Send\n"
    "until the anger cooled to a fact.\n"
    "The message I never sent\n"
    "is the only one I wrote\n"
    "entirely by myself.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
