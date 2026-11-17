# JD Vance Tracker

An independent, static tracker of public polling and of large-account posts and outlet coverage concerning Vice President JD Vance.

This is not affiliated with any campaign, political party, or government office.

## What’s on the page

- Favorability averages and a table of opened national polls
- A 2028 Republican nomination comparison (Vance, Rubio, DeSantis, and others as reported)
- A sentiment overview of critical vs. supportive engagement by theme
- A filterable feed of posts and articles, with source links, engagement, and authenticity heuristics
- A sourced biography, including Vance’s 2016 criticism of Donald Trump, his later explanations, and the 2024 vice-presidential selection
- A myths-vs-facts page limited to claims examined by major fact-checkers
- Official government portraits (U.S. public domain), stored in `images/` with credits

The live site is the GitHub Pages root for the Vance-Tracker-2028 organization:

https://vance-tracker-2028.github.io/

## Build

Data files live in `data/` (`entries.json`, `polls.json`, `polls_2028.json`). To refresh them from a local tracker export and rebuild `index.html`:

```bash
DATA_SRC=/path/to/vance_tracker ./publish.sh
```

Or build without publishing:

```bash
DATA_SRC=/path/to/vance_tracker python3 build.py
```

## Publish

`publish.sh` rebuilds the page, commits, and pushes to `Vance-Tracker-2028/vance-tracker-2028.github.io` on the `main` branch (site root). Override with `ORG=other-org` to publish to `ORG/ORG.github.io` instead. Commit author name is `Vance Tracker`. The script will refuse to run if a personal name appears in the site, the data, or the commit identity.

Authenticity ratings on the site are heuristics, not proof.
