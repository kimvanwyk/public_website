from glob import glob
import os.path
import textwrap

import arrow

TIL_DIR = "content/post/til"


def get_filename(arrow_date):
    ds = f"{arrow_date:YYMMDD}"
    files = glob(os.path.join(TIL_DIR, f"*{ds}*.md"))
    if files:
        files.sort()
        highest = int(files[-1].split(".md")[0].split("_")[-1])
    else:
        highest = 0
    fn = f"til_{ds}_{highest + 1}.md"
    return fn


def make_til_file(arrow_date):
    fn = get_filename(arrow_date)
    with open(os.path.join(TIL_DIR, fn), "w") as fh:
        fh.write(
            textwrap.dedent(
                f"""\
---
date: "{arrow_date:YYYY-MM-DD}"
tags: ["til"]
title: "Today I Learned: {arrow_date:DD/MM/YYYY} - "
---

"""
            )
        )


if __name__ == "__main__":
    from rich.prompt import Prompt

    ds = Prompt.ask("Date for TIL file (YYMMDD):", default=f"{arrow.now():YYMMDD}")
    make_til_file(arrow.get(ds, "YYMMDD"))
