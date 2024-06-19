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

## Acknowledgements

Thank you for following these guidelines and for your contribution to the project!
