# Authoring conventions

These conventions supplement `instructions.md` and the approved `template.md`.
They do not change the required exercise structure, file paths, or deliverables.
The instructions and approved template take precedence.

## Voice and clarity

- Address the learner as "you" in a friendly, professional tone.
- Use active voice, familiar words, US spelling, and short paragraphs.
- Explain the purpose of an action before giving the steps.
- Define unfamiliar technical terms and acronyms when first used.
- Use current official product names, verified against current documentation.
- Avoid promotional claims, unnecessary jargon, cultural idioms, and stereotypes.
- Use inclusive, gender-neutral language.

## Procedures and presentation

- Use sentence-case headings and precise imperative verbs for procedures.
- Prefer input-neutral verbs such as "select" rather than "click".
- Keep steps focused on one meaningful action or a tightly related set of actions.
  Break long procedures into meaningful subtasks rather than arbitrary chunks.
- Clearly identify the application, pane, terminal, or file where an action occurs.
- Use bold for UI labels and keyboard shortcuts, and inline code for filenames,
  paths, identifiers, commands, and all values the learner types.
- Give code fences language labels and distinguish expected output from input.
- Explain code in terms of the exercise outcome, not just its syntax.
- Remind learners to save edited files before running or verifying them.
- Include observable verification after meaningful changes.
- Preserve the template's numbered-list, callout, and browser-link conventions.
  Use full documentation URLs for external Learn pages; use relative links only
  for files actually included in the exercise package.
- Use tables for genuinely comparative information and descriptive alt text for
  actual supplied images. Do not rely on color alone to convey meaning.

## Audience and practical reliability

- For developers, use incremental implementation and short verification cycles,
  with complete imports and dependencies and starter placeholders matching steps.
- For IT professionals, explain the starting environment, permissions, operational
  impact, and a safe rollback path for changes.
- For business users, favor the relevant graphical interface and explain expected
  results in business terms. Do not introduce code or command-line setup unless
  the requested outcome requires it.
- Estimate duration from the actual work, including reading, execution, validation,
  and likely troubleshooting. Do not inflate task counts to fill a duration.
- Keep resource names, variables, paths, and scenario details consistent. Introduce
  each file, endpoint, and resource before learners use it.
- State relevant preview restrictions and provide safe, targeted recovery guidance
  for common failures without implying that unperformed cloud checks succeeded.

## Provenance

Adapted authoring guidance from the canonical Microsoft Learn writing style guide
and lab exercise writer at revision
`514ec951c8c6abb83f5b1580a45c13459b34a8ec`:

- https://github.com/MicrosoftLearning/learning-lab-agents/blob/514ec951c8c6abb83f5b1580a45c13459b34a8ec/.github/instructions/microsoft-learn-style-guide.md
- https://github.com/MicrosoftLearning/learning-lab-agents/blob/514ec951c8c6abb83f5b1580a45c13459b34a8ec/.github/agents/lab-exercise-writer.agent.md
