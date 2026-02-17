# Instructor Guide: Git Workflow Strategy

This course uses an **Immutable Release** git strategy to minimize student friction.

## The Core Rule
**Once a file is pushed to GitHub and students have started working on it, DO NOT MODIFY IT.**

If you modify a file that students have also modified (e.g., they wrote code in `Chapter1.ipynb` and you fix a typo in the same file), they will encounter a **Merge Conflict** when they pull. Most students will not know how to resolve this.

## How to Release Content
1.  **Create new files** locally (e.g., `chapters/Chapter2.ipynb`).
2.  **Commit and Push** them to GitHub.
3.  **Tell Students**: "Open GitHub Desktop and click 'Fetch origin' to get the new chapter."

## How to Fix Errors (The "Safe" Way)
If you find a critical error in a released notebook:

### Option A: The Announcement (Preferred)
Post an announcement on Moodle/Canvas/Slack:
> "Note: In Question 3, the variable should be `df_clean`, not `df`. Please correct this in your notebook."

### Option B: The Versioned Fix
1.  Copy the notebook to a new file: `Chapter1_v2_FIXED.ipynb`.
2.  Push the new file.
3.  Tell students to use the new version if they haven't started, or copy their answers over.

## What if I *Must* Edit a File?
If you absolutely must edit a released file (e.g., `README.md` or a syllabus that students likely haven't modified):
1.  Commit and Push.
2.  If a student complains about a conflict, tell them:
    *   "Rename your existing file to `My_Chapter1.ipynb`."
    *   "Pull again."
    *   "Copy your work into the new clean file."

## Summary
*   **Additions are safe.** (Adding Week 2, Week 3, etc.)
*   **Modifications are dangerous.** (Editing Week 1 after release).
