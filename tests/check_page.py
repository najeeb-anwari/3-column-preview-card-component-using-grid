#!/usr/bin/env python3
"""Lightweight regression checks for the static page."""

from html.parser import HTMLParser
from pathlib import Path


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.h1_text: list[str] = []
        self.buttons = 0
        self.in_h1 = False
        self.blank_links: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {key: (value or "") for key, value in attrs}

        if tag == "h1":
            self.in_h1 = True

        if tag == "button":
            self.buttons += 1

        if tag == "a" and attr_map.get("target") == "_blank":
            self.blank_links.append(attr_map)

    def handle_endtag(self, tag: str) -> None:
        if tag == "h1":
            self.in_h1 = False

    def handle_data(self, data: str) -> None:
        if self.in_h1:
            value = data.strip()
            if value:
                self.h1_text.append(value)


html = Path("index.html").read_text(encoding="utf-8")
parser = PageParser()
parser.feed(html)

expected_headings = ["SEDANS", "SUVS", "LUXURY"]
assert parser.h1_text == expected_headings, (
    "Card headings mismatch. "
    f"Expected {expected_headings}, got {parser.h1_text}"
)

assert parser.buttons == 3, f"Expected 3 card buttons, found {parser.buttons}."

for link in parser.blank_links:
    rel_tokens = set(link.get("rel", "").split())
    assert {"noopener", "noreferrer"}.issubset(rel_tokens), (
        "Every target=_blank link must include rel='noopener noreferrer'. "
        f"Problematic link attrs: {link}"
    )

print("All static checks passed.")
