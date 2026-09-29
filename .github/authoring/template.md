---
lab:
    title: '[Action] [task or outcome] with [product, technology, or context]'
    description: '[In approximately 20-25 words, describe the observable outcome, key subtasks or technologies, context, and level-defining guidance or tradeoffs.]'
    duration: 00  # duration in minutes; replace with a positive integer
    level: 100 # 100 basic concepts, 200 foundations, 300 practical usage, 400 advanced scenarios, 500 expert design
    islab: true # if this is not a lab that should be listed in the catalog, set to false
    status: 'in-development' # in-development or released
    targetDate: '2026-09-29' # Example only: replace with the actual generation date (YYYY-MM-DD), unless the author supplies a release/update date
---
<!--
Edit the metadata above to manage the list of exercises in the home page of the GitHub site that gets generated.
You can delete the module and edit index.md in the root of the repo to customize the display so that only the exercises are listed.
To enable GitHub page publishing, edit the Pages settings for the repo and publish from the main branch.
-->

# [Action] [task or outcome] with [product, technology, or context]

This exercise should take approximately **XX** minutes to complete. <!-- update with estimated duration -->

<!--
Match the title in the metadata above, the Learn Exercise unit, and the ILT slide.
Start with a specific, observable action and identify the primary task and topic, product, or technology.
Prefer literal wording. Do not use promotional language, level labels, or broad verbs such as "learn," "explore," or "discover" when a more specific action is known.
-->

In this exercise, you will [describe in approximately 20-25 words the observable outcome, key subtasks or technologies, context, and level-defining guidance, independence, constraints, or tradeoffs].

<!--
Expand the title without repeating it. Use precise performance verbs such as identify, explain, configure, apply, integrate, compare, evaluate, adapt, design, or optimize.
Describe only activities the exercise contains. Do not use promotional claims, provide only a topic list, present prior knowledge as an outcome, or claim hands-on practice, independence, production use, or optimization unless the exercise supports the claim.
Make the dominant end-of-exercise outcome clear enough for a reviewer to identify the level from the description.
-->

## Scenario

You are a [relevant role] at [type of organization]. [Describe a realistic problem or need.] In this exercise, you will [create, configure, evaluate, or improve something] so that [meaningful user or business outcome].

<!--
Use two to four sentences to help learners recognize why the exercise is relevant to them.
Give the learner a realistic role, problem or decision, beneficiary, and reason the outcome matters.
Connect the scenario directly to the exercise outcome. Avoid unnecessary company names, fictional backstory, details that do not affect the tasks, and repetition of the description or task instructions.
-->

## Prior knowledge

<!--
List only the prior knowledge and experience learners genuinely need before starting. Describe entry knowledge rather than material taught in the exercise, and be specific enough for learners to judge their readiness.
Keep prior knowledge separate from the description and do not duplicate the learning objectives. Put required tools, environments, assets, accounts, licenses, permissions, access, and setup tasks in "Before you start."
Use **None** when no prior knowledge is required.
-->

- [Required prior knowledge or experience]

## Before you start

<!--
Add steps to get the learner to the starting point for the exercise. This might be cloning the repo and running a script or performing some manual steps.

Only include this section if exercise-specific setup is necessary AND the same preparation applies to self-paced (on Learn) and managed (in hosted ILT lab profiles) scenarios. Otherwise delete this section.
If self-paced/ILT-specific setup steps are required, include them in the Learn "Exercise" unit from where learners open this exercise and in the Skillable lab profile instructions before this Markdown file is imported.

Do not include requirements for getting an Azure (or other) subscription. Assume the learner has a functioning lab environment.

If complex setup steps apply to ALL exercises in the repo (for example, installing and configuring client-side tools), create a separate 00-setup.md file with instructions and link to it.

List the environment, tools, access requirements, and in-repo assets that the learner needs. This includes required accounts, licenses, permissions, and exercise-specific setup tasks. Use exact versions only when the exercise depends on them. Finish with a quick smoke test that verifies the setup and provides observable, unambiguous success criteria. Do not ask the learner to begin the exercise until the smoke test passes.
-->

Before you start this exercise, make sure your environment is ready.

### Environment

<!-- Describe the required operating system, runtime, cloud environment, accounts, licenses, permissions, access, and other exercise-specific configuration. Do not include instructions for obtaining a subscription. -->

- [Required environment or service, including the minimum version or configuration when relevant]
- [Required account, license, access, or permissions]

### Tools

<!-- List every tool the learner uses in the exercise. Include a command to verify each installed tool when practical. -->

- [Tool name and version, if version-specific]: verify by running `[verification command]`.
- [Tool name]: [required configuration or extension]

### Exercise assets

<!-- List only assets stored in this repository that the learner needs. Link to each file or folder by using a relative path, and explain what it is used for. Store downloadable code/data in Labfiles. If no assets are needed, say so. -->

- [Asset name](../../Labfiles/01-exercise-slug/data/example.csv): [purpose]
- [Asset folder](../../Labfiles/01-exercise-slug/): [purpose]

### Verify your setup

<!-- Provide the smallest safe smoke test that confirms the environment, tools, permissions, and assets are ready. State the exact expected output or observable state. Include troubleshooting guidance or a link when a common failure is likely. -->

1. Run `[smoke-test command or action]`.
1. Confirm that [specific expected output, status, or observable result].

Your setup is ready when [clear, measurable success criterion]. Do not continue until this check succeeds.

## Task <!-- Change to an appropriate task title with an imperative verb phrase (e.g. "Configure the application") -->

First, you need to ...

1. Step 1
1. Use `inline code formatting` for anything the learner types (not just code), because it creates a [T] link in the hosted Skillable environment.
1. If the learner must open a website, include a clickable link AND the URL formatted as code. For example: "Open the [Microsoft Learn](https://learn.microsoft.com){:target="_blank"} website at `https://learn.microsoft.com`." The `{:target="_blank"}` tag opens the link in a new browser tab.
1. For file downloads, store the actual files in `Labfiles` and use verified raw GitHub URLs when published. Include both a clickable download link and the literal URL in inline code. Before publication, refer to the generated ZIP and relative paths; never invent a published repository URL.
1. Alternatively, for a developer audience, have learners clone the supplied repository if appropriate.
1. Indent multiline code blocks to match the list item:

    ```python
    # This is an example of an
    # indented code block.
    ```

1. If a screenshot is supplied, resize it appropriately so normal text is roughly the same size as the surrounding text. Full application windows are generally about 1200x900 pixels. Store screenshots in a case-sensitive `Media` subfolder beside this exercise. Indent images within lists:

    ![A screenshot of an application.](./Media/edge-copilot.png)

    <!-- This is an example reference only. Include it in generated output only if that image is supplied. -->

1. Use a note for additional explanation, context, or links:

    > **Note**: This is a note.

1. Use environment-neutral wording where self-paced and hosted environments vary:
    - "Sign in using your Azure credentials."
    - "Select an existing resource group or create a new one."
    - Keep phrases consistent for Skillable replacement-text rules.
    <!-- Put delivery-specific credentials and setup instructions outside this shared file, in the Learn exercise unit or Skillable profile. -->
1. etc.

## Next task

Now, ...

1. Step 1
1. Step 2
1. etc.

## Task with subtasks

Use subtasks when a task contains distinct activities.

### Subtask 1

1. Step 1
1. Step 2
1. etc.

### Subtask 2

1. Step 1
1. Step 2
1. etc.

## Clean up

<!-- Include when resources, temporary assets, or reversible changes require cleanup. Otherwise delete this section. Never delete pre-existing or shared training resources. -->

Now that you've finished the exercise, remove the resources created specifically for it to avoid unnecessary resource usage.

1. Step 1
1. etc.
