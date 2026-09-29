# Lab creation agent output

Reviewable Microsoft Learn exercise packages produced by a lab-authoring agent.
This repository is public. Include only publishable content, synthetic data, and
configuration placeholders; never include credentials or private customer data.

## Repository layout

```text
Instructions/
    Exercises/
        01-exercise-slug.md
        Media/                     # Only for actual supplied images
Labfiles/
    01-exercise-slug/
        <starter code and configuration>
        data/                      # When required
.github/
    authoring/
        agent-instructions.md
        template.md
        authoring-conventions.md
```

Do not create an empty starter application for a portal-only exercise; include
any required data in `Labfiles`.
Keep exercise numbering and asset paths consistent across the package.

## Review drafts

[Generate an inventory reorder report with Python](Instructions/Exercises/01-inventory-replenishment.md)
is a 20-minute exercise with learner starter code and synthetic CSV data. The
exercise and [public writer-instruction snapshot](.github/authoring/agent-instructions.md)
are drafts for human review, not approved publication-ready content.

## Authoring and review

Use the approved [exercise template](.github/authoring/template.md) and
[authoring conventions](.github/authoring/authoring-conventions.md).
Replace template values and remove authoring comments from learner-facing files.
Use the actual generation date for `lab.targetDate` unless an author supplies a
release or update date. The template date is an example, not a default.

For each exercise:

1. Create a topic branch, such as `labs/01-exercise-slug`.
1. Add the exercise under `Instructions/Exercises` and supporting assets under
   the corresponding `Labfiles` directory.
1. Open a pull request. Record sources, assumptions, and verification limitations
   in the pull request rather than adding extra learner-document sections.
1. Review the content and validation results before merging. Do not overwrite
   another exercise's files or replace shared resources without review.

The validation workflow checks metadata, required headings, duration placement,
template comments, and local inline links. It does not execute generated code,
provision cloud resources, verify external URLs, or establish technical accuracy.
It passes when no exercises exist, so initialization does not require a fake lab.
Branch protection is not configured by this scaffold.

## Run validation locally

Use Python 3.11 or later. From the repository root, run:

```powershell
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
python scripts/validate_labs.py
```

## Publishing integration

The repository is ready to receive files, but automatic Foundry-to-GitHub
publishing is not connected yet. The intended publishing flow is:

1. Generate the exercise and supporting files.
1. Validate the package and inspect the files intended for publication.
1. Publish the files to a new branch and open a pull request.

The inventory exercise was submitted through an explicitly authorized one-off
publishing session, not an automatic Foundry-to-GitHub integration.

Keep research access read-only. A separate publisher should have write permission
only to this repository and explicit safeguards against overwriting unrelated
paths. Do not store a personal access token or Azure credential in this repository.
