# Codebase Task Proposals

## 1) Typo fix task
**Issue found:** The first card heading in `index.html` reads `SEDNAS` instead of `SEDANS`.

**Proposed task:**
- Update the heading text from `SEDNAS` to `SEDANS`.
- Add a quick content check (or lightweight test) that verifies the three card titles are spelled correctly.

## 2) Bug fix task
**Issue found:** External links that open in a new tab use `target="_blank"` without a corresponding `rel="noopener noreferrer"`, which is a security bug (reverse tabnabbing risk).

**Proposed task:**
- Update all external links with `target="_blank"` to include `rel="noopener noreferrer"`.
- Verify no existing link behavior regresses.

## 3) Documentation discrepancy task
**Issue found:** `README.md` says users should be able to "See hover states for interactive elements," but there is no mention that keyboard users should also get a visible focus state, and the stylesheet currently defines only `:hover` behavior for buttons.

**Proposed task:**
- Update `README.md` to explicitly include keyboard focus visibility as an expected interactive behavior.
- Add matching note in implementation docs/comments (or inline CSS comment near button states) so docs and behavior expectations stay aligned.

## 4) Test improvement task
**Issue found:** There are no automated checks for key page content and accessibility/security-sensitive attributes.

**Proposed task:**
- Add a minimal test (for example with Playwright) that validates:
  - The three card headings render as expected.
  - Buttons are present and visible.
  - Any `target="_blank"` links include `rel="noopener noreferrer"`.
- Run this test in CI (or a local script) to catch regressions early.
