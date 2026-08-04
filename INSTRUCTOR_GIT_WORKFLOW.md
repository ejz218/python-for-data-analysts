# Instructor Guide: Git Workflow Strategy

This course uses an **Immutable Release** git strategy to minimize student friction.

## The Core Rule
**Once a file is pushed to GitHub and students have started working on it, DO NOT MODIFY IT.**

If you modify a file that students have also modified (e.g., they wrote code in `Chapter1.ipynb` and you fix a typo in the same file), they will encounter a **Merge Conflict** when they pull. Most students will not know how to resolve this.

The operative words are **have started working on it**. A released chapter that nobody has opened yet is not yet load-bearing, and correcting it in place is safe. See Option C.

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

### Option C: In-Place Correction Before Students Begin
Use this when a released chapter contains a **substantive error** and the class has **not started the chapter yet**. An announcement (Option A) does not work when the fix spans many cells, and a versioned file (Option B) leaves a known-wrong notebook sitting in `chapters/` for the rest of the semester.

All five conditions must hold:

1.  **The error is substantive, not cosmetic.** A factual claim that is wrong, or code whose output will contradict what the notebook tells students to expect. Typos go in an announcement.
2.  **Nobody has started the chapter.** Check the actual schedule, do not assume. If the chapter is assigned this week, it is too late.
3.  **The correction ships before the "begin the chapter" announcement,** so the pull and the start are the same event for every student.
4.  **The corrected notebook has been executed end to end** against the real dataset in `data/`, and every number in the prose has been checked against that file. Correcting one error while introducing another is worse than leaving it alone.
5.  **The update instructions include a `git status` step and a recovery path.** This is not optional, for the reason in the warning below.

⚠️ **"Has not edited it" is narrower than it sounds.** Opening a notebook and running a single cell stores outputs in the `.ipynb`, which makes the file **modified** as far as git is concerned even though the student typed nothing. Those students will hit `Your local changes would be overwritten` on pull. Give them this in the update instructions:

```bash
cd ~/Desktop/buan446
git status
# If chapters/ChapterN....ipynb is listed as changed and you want to keep your work,
# save it under your own name first (File > Save Notebook As…), then:
git checkout -- chapters/ChapterN_Whatever.ipynb
git pull
```

Also give them a **positive confirmation check** rather than "you should be fine." Name something visible that only exists in the corrected version, for example "scroll to the bottom and confirm you see Section 8.12," so a silently failed pull does not go unnoticed.

**Precedent:** Chapter 8 was corrected in place on 2026-08-03 under this option. The heatmap section asserted a positive relationship between study hours and GPA where the real correlation is 0.044, ten cells omitted the Graduate class year and silently dropped 74 students, and the saved figure in Section 8.7 had an axis range that clipped every bar. Students were on Chapter 6 at the time.

## What if I *Must* Edit a File?
If you absolutely must edit a released file (e.g., `README.md` or a syllabus that students likely haven't modified):
1.  Commit and Push.
2.  If a student complains about a conflict, tell them:
    *   "Rename your existing file to `My_Chapter1.ipynb`."
    *   "Pull again."
    *   "Copy your work into the new clean file."

## Summary
*   **Additions are safe.** (Adding Week 2, Week 3, etc.)
*   **Modifications are dangerous** once students are in the file. (Editing Week 1 after release.)
*   **Modifications before students start are acceptable** if the error is substantive, the notebook is verified against the real data, and the update instructions carry a `git status` step and a confirmation check. (Option C.)
*   **When in doubt, do not modify.** The cost of a merge conflict falls on the student, who cannot fix it. The cost of a versioned file falls on you, and you can.
