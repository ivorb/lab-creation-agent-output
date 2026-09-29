"""Check exercise structure and local inline links without running lab code."""

import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


def prose_only(text):
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if marker:
            token, suffix = marker.groups()
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not suffix.strip():
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines)


def check_links(path, root, text):
    errors = []
    for match in re.finditer(r"!?\[[^\]\n]*\]\(\s*(?:<([^>]+)>|([^\s)]+))", text):
        target = match.group(1) or match.group(2)
        parts = urlsplit(target)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        relative = unquote(parts.path)
        if "\\" in relative:
            errors.append(f"Use forward slashes in Markdown links: {target}")
            continue
        resolved = (path.parent / relative).resolve()
        if not resolved.is_relative_to(root.resolve()):
            errors.append(f"Local link leaves the repository: {target}")
        elif not resolved.exists():
            errors.append(f"Missing local link target: {target}")
    return errors


def validate_file(path, root):
    text = path.read_text(encoding="utf-8")
    errors = []
    front = re.match(r"\A---[ \t]*\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.DOTALL)
    body = text[front.end():] if front else text
    prose = prose_only(body)
    errors.extend(check_links(path, root, prose))
    if "<!--" in prose:
        errors.append("Remove authoring HTML comments.")
    # Shared setup documents are linked support material, not standalone labs.
    if path.name == "00-setup.md":
        return errors
    if not front:
        return errors + ["Missing YAML front matter."]
    try:
        metadata = yaml.safe_load(front.group(1))
    except yaml.YAMLError as error:
        return errors + [f"Invalid YAML: {error}"]
    lab = metadata.get("lab") if isinstance(metadata, dict) else None
    if not isinstance(lab, dict):
        return errors + ["Front matter must contain a lab mapping."]
    for field in ("title", "description"):
        if not isinstance(lab.get(field), str) or not lab[field].strip():
            errors.append(f"lab.{field} must be a nonempty string.")
    duration = lab.get("duration")
    if type(duration) is not int or duration <= 0:
        errors.append("lab.duration must be a positive integer.")
    if type(lab.get("level")) is not int or lab["level"] not in (100, 200, 300, 400, 500):
        errors.append("lab.level must be 100, 200, 300, 400, or 500.")
    if type(lab.get("islab")) is not bool:
        errors.append("lab.islab must be a boolean.")
    if lab.get("status") not in ("in-development", "released"):
        errors.append("lab.status must be in-development or released.")
    target_date = lab.get("targetDate")
    if not isinstance(target_date, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", target_date):
        errors.append("lab.targetDate must be a quoted YYYY-MM-DD string.")
    else:
        try:
            date.fromisoformat(target_date)
        except ValueError:
            errors.append("lab.targetDate must be a real calendar date.")
    lines = [line.strip() for line in prose.splitlines() if line.strip()]
    headings = [line for line in lines if line.startswith("# ")]
    expected_title = f"# {lab.get('title', '')}"
    if headings != [expected_title] or not lines or lines[0] != expected_title:
        errors.append("The body must start with a single H1 matching lab.title.")
    expected_duration = f"This exercise should take approximately **{duration}** minutes to complete."
    if len(lines) < 2 or lines[1] != expected_duration:
        errors.append("Put the matching duration statement immediately after the H1.")
    if len(lines) < 3 or not lines[2].startswith("In this exercise, you will "):
        errors.append("Put the outcome description immediately after the duration.")
    h2s = [line for line in lines if line.startswith("## ")]
    if h2s[:2] != ["## Scenario", "## Prior knowledge"]:
        errors.append("The first sections must be Scenario, then Prior knowledge.")
    if "## Before you start" in h2s:
        if h2s.index("## Before you start") != 2:
            errors.append("Before you start must follow Prior knowledge.")
        setup = prose.split("## Before you start", 1)[1].split("\n## ", 1)[0]
        h3s = re.findall(r"^### (.+)$", setup, re.MULTILINE)
        if h3s != ["Environment", "Tools", "Exercise assets", "Verify your setup"]:
            errors.append("Setup subsections must be Environment, Tools, Exercise assets, Verify your setup.")
    if re.search(r"^#{4,}\s", prose, re.MULTILINE):
        errors.append("Use only H1, H2, and H3 headings.")
    return errors


def main():
    root = Path(__file__).resolve().parents[1]
    files = sorted((root / "Instructions" / "Exercises").rglob("*.md"))
    failures = 0
    for path in files:
        for error in validate_file(path, root):
            print(f"{path.relative_to(root).as_posix()}: {error}", file=sys.stderr)
            failures += 1
    if failures:
        print(f"Failed: {failures} issue(s) in {len(files)} Markdown file(s).", file=sys.stderr)
        return 1
    print(f"Validated {len(files)} exercise/setup Markdown file(s). No lab code was executed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
