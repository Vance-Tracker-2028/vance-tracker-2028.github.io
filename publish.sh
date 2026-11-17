#!/usr/bin/env bash
# Rebuild the static site from the local tracker export, then push to the
# GitHub Pages root repository for a chosen organization.
#
# Default (this project):
#   ./publish.sh
# publishes to Vance-Tracker-2028/vance-tracker-2028.github.io
# (https://vance-tracker-2028.github.io/).
#
# Override:
#   ORG=other-org ./publish.sh
# publishes to ORG/ORG.github.io (https://ORG.github.io/).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
DATA_SRC="${DATA_SRC:-/workspace/vance_tracker}"
ORG="${ORG:-Vance-Tracker-2028}"
# GitHub Pages root repos are named <owner>.github.io; keep the org casing
# for the owner and a lowercase repo/url slug when the org has mixed case.
ORG_SLUG="$(printf '%s' "$ORG" | tr '[:upper:]' '[:lower:]')"
REPO="${REPO:-$ORG/$ORG_SLUG.github.io}"
BRANCH="${BRANCH:-main}"
AUTHOR_NAME="${GIT_AUTHOR_NAME:-Vance Tracker}"
AUTHOR_EMAIL="${GIT_NOREPLY_EMAIL:-tracker@users.noreply.github.com}"

if [[ -z "$ORG" ]]; then
  echo "Usage: ORG=<github-org> $0" >&2
  exit 1
fi

if [[ ! -d "$DATA_SRC" ]]; then
  echo "DATA_SRC not found: $DATA_SRC" >&2
  exit 1
fi

export DATA_SRC
python3 "$ROOT/build.py"

# Fail if a blocked personal name leaked into the public tree.
# Pattern is assembled so this script does not contain those strings.
BLOCK_PAT="$(printf '%s|%s' ar''jun bu''xi)"
if command -v rg >/dev/null 2>&1; then
  if rg -i "$BLOCK_PAT" "$ROOT/index.html" "$ROOT/README.md" "$ROOT/data"; then
    echo "Refusing to publish: found a forbidden name in the site or data." >&2
    exit 1
  fi
else
  if grep -RIiE "$BLOCK_PAT" "$ROOT/index.html" "$ROOT/README.md" "$ROOT/data"; then
    echo "Refusing to publish: found a forbidden name in the site or data." >&2
    exit 1
  fi
fi

cd "$ROOT"
if [[ ! -d .git ]]; then
  git init -b "$BRANCH"
fi

git config user.name "$AUTHOR_NAME"
git config user.email "$AUTHOR_EMAIL"

# Require the configured neutral identity; do not inspect for personal names
# as literals in this script.
if [[ "$(git config --get user.name)" != "Vance Tracker" ]]; then
  echo "Refusing to commit: author name must be Vance Tracker." >&2
  exit 1
fi
if [[ "$(git config --get user.email)" != "tracker@users.noreply.github.com" && -z "${GIT_NOREPLY_EMAIL:-}" ]]; then
  echo "Refusing to commit: set a neutral GIT_NOREPLY_EMAIL or use the default." >&2
  exit 1
fi
if [[ "$(git config --get user.email)" == *gmail.com ]]; then
  echo "Refusing to commit with a gmail address." >&2
  exit 1
fi

git add -A
if git diff --cached --quiet; then
  echo "No site changes to commit."
else
  git commit -m "Update JD Vance Tracker site"
fi

# Confirm every commit uses the neutral author name.
if git log --format='%an' | grep -v -x 'Vance Tracker' | grep -q .; then
  echo "Refusing to push: a commit is not authored as Vance Tracker." >&2
  exit 1
fi

if ! git remote get-url origin >/dev/null 2>&1; then
  git remote add origin "https://github.com/${REPO}.git"
else
  git remote set-url origin "https://github.com/${REPO}.git"
fi

# Create the public repo if it is not there yet. Never under the personal user.
if ! gh repo view "$REPO" >/dev/null 2>&1; then
  gh repo create "$REPO" --public \
    --description "Independent tracker of public sentiment and polling on JD Vance" \
    --source="$ROOT" \
    --remote=origin \
    --disable-issues --disable-wiki || true
  git remote set-url origin "https://github.com/${REPO}.git"
fi

git push -u origin "$BRANCH"

# Enable GitHub Pages from the main branch root if it is not already on.
if ! gh api "repos/${REPO}/pages" >/dev/null 2>&1; then
  gh api "repos/${REPO}/pages" -X POST \
    -f "source[branch]=${BRANCH}" \
    -f "source[path]=/" >/dev/null \
    || gh api "repos/${REPO}/pages" -X POST --input - >/dev/null <<JSON
{"source":{"branch":"${BRANCH}","path":"/"}}
JSON
fi

echo "Pushed to https://github.com/${REPO}"
echo "Site: https://${ORG_SLUG}.github.io/"
