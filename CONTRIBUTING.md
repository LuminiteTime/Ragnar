# Contributor Guide

To ensure a smooth development and collaboration process, please follow these guidelines.

## Git Workflow

We use the Git-flow branching model. Here is a brief description of our process:

### Main Branches

- **main**: Stores the official release history. Each commit in this branch represents a new release version.
- **dev**: Used for integrating all new features and changes that will be included in the next release.

### Starting Work on an Issue

1. **Create a Merge Request on GitLab**:
   - Go to the "Issues" section, choose an issue, and click "Create merge request".
   - Delete "Draft: Resolve " and quotation marks around the issue name.
   - Set the target branch to `dev`.
   - This will automatically create a new branch for this issue.

2. **Switch to the New Branch**:
    ```sh
    git checkout <feature_bracnch_name>
    ```

### Developing the Issue

1. **Make Changes**:
    - Implement the necessary changes in the issue bracnh.
    - Commit changes with meaningful messages:
      ```sh
      git add .
      git commit -m "Implement feature 1"
      ```
    - Push changes to the remote repository:
      ```sh
      git push origin <feature_bracnch_name>
      ```

### Completing the Issue

1. **Create a Merge Request for Review**:
   - Go to the "Merge Requests" section on GitLab.
   - Find the open Merge Request for `feature/ISSUE-123`.
   - Assign the Merge Request to yourself and select a reviewer.

2. **Review Process**:
   - The reviewer will provide feedback.
   - Address the feedback and push additional commits if necessary.

3. **Merge into `dev`**:
    - Once approved, the reviewer will merge the `feature/ISSUE-123` branch into `dev`.

    ```sh
    git checkout dev
    git merge <feature_bracnch_name>
    ```

### Handling Hotfixes

1. **Create a Hotfix Branch**:
    ```sh
    git checkout main
    git checkout -b <hotfix_branch_name>
    git push origin <hotfix_branch_name>
    ```

2. **Fix the Issue**:
    - Implement the hotfix and push changes.
    - Merge the hotfix branch into `main` and `dev`:
    ```sh
    git checkout main
    git merge <hotfix_branch_name>
    git checkout dev
    git merge <hotfix_branch_name>
    git branch -d <hotfix_branch_name>
    ```


# Code Review Guidelines

To maintain the quality of our codebase and ensure that all contributions meet the highest standards, we have established the following code review guidelines. Please follow these steps when submitting or reviewing code.

## For Contributors

1. **Ensure Code Quality**:
    - Before submitting a pull request, make sure your code follows the project's coding standards and best practices (see "Coding Standards" section bellow).
    - Cover your code with local tests and run them to ensure your changes do not introduce any new issues.

2. **Merge Request Submission**:
    - Provide a detailed description of the changes in the merge request. Include the purpose of the change and any relevant details.
    - Link the merge request to any related issue(s) in the issue tracker.

3. **Respond to Feedback**:
    - Be open to feedback and suggestions from reviewers.
    - Address all comments and questions in the merge request discussion. If changes are requested, make them, push updates to the branch, and notify your reviewer by tagging them.

## For Reviewers

1. **Review for Quality and Consistency**:
    - Ensure the code follows the project's coding standards and best practices (see "Coding Standards" section bellow).
    - Check for code clarity, maintainability, and scalability.

2. **Functional Testing**:
    - Verify that the changes work as expected and do not introduce new issues.
    - Suggest additional test cases if necessary.

3. **Provide Constructive Feedback**:
    - Offer clear feedback and explain the reasoning behind your suggestions.
    - Highlight what you appreciate about the contribution as well as any areas for improvement.

4. **Timely Reviews**:
    - Aim to complete reviews within a reasonable timeframe to keep the project moving forward.

## Finalizing the Review

- Once all feedback has been addressed, the reviewer should approve the merge request.
- The merge request can then be merged into the target branch, typically `dev`, following the project's merging strategy.

# Coding Standards

## Python Coding Standards
### Following PEP 8:
Ensure all Python code follows the PEP 8 style, which also includes conventions for variable naming. For example, use snake_case for function and variable names, and PascalCase for class names.

### Optimization and Performance:
Write efficient Python code by choosing the right data structures, avoiding unnecessary computations, and using generators where applicable to save memory.

### Readability and Documentation:
Prioritize writing clean, readable code. Functions and classes should be small and focused on a single responsibility. Use type hints to improve code clarity and help with static analysis (SonarLint is preferable to use). Document public interfaces with concise, informative docstrings following the docstring conventions. Use comments wisely to explain some complex logic.

## Svelte Coding Standards
### Adherence to Component Structure:
Organize Svelte components according to the following rules. This involves grouping script, markup, and styles in a single .svelte file, with script tags at the top. Follow naming conventions for components (e.g., PascalCase). Refer to the Svelte style guide for specifics.

### Reactivity and State Management:
Manage Svelte's reactivity model efficiently. Use stores for global state management and minimize derived state to reduce unnecessary computations. When interacting with props and reactive statements, ensure changes do not cause unintended side effects or performance issues.

### Readability and Documentation:
Keep components small and focused. Break down large components into smaller, reusable ones. Use meaningful names for components, props, and functions. Document each component's purpose and its props using comments at the top of the file or inline where necessary. For complex logic or side effects, provide comments that explain the reasons of creating it.

In both Python and Svelte projects, ensure that all code contributions are covered by appropriate tests to verify functionality.


## Acknowledgements

Thank you for following these guidelines and for your contribution to the project!
