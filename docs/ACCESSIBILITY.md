# Accessibility

FlowAI is committed to ensuring digital accessibility for people with disabilities. We are continually improving the user experience for everyone, and applying the relevant accessibility standards.

## WCAG 2.1 AA Compliance Checklist
- [x] **Color Contrast**: All text maintains a minimum contrast ratio of 4.5:1 against its background.
- [x] **Keyboard Navigation**: The entire site is navigable via the `Tab` key.
- [x] **Focus Indicators**: Visible focus rings are provided for all interactive elements.
- [x] **Semantic HTML**: Proper use of `<header>`, `<nav>`, `<main>`, `<section>`, and `<footer>`.
- [x] **Heading Hierarchy**: Only one `<h1>` per page, with sequential heading levels (`<h2>`, `<h3>`) without skipping.
- [x] **Aria Labels**: Used where visible text is not present (e.g., mobile menu toggle, social icons).
- [x] **Alt Text**: Descriptive `alt` attributes on all meaningful images; empty `alt=""` on purely decorative images.
- [x] **Motion Control**: Respects user OS preferences via `@media (prefers-reduced-motion: reduce)`.

## Tools Used for Audit
- **Lighthouse**: Automated accessibility auditing in Chrome DevTools.
- **WAVE (Web Accessibility Evaluation Tool)**: Browser extension for visual overlay of accessibility issues.
- **Keyboard Testing**: Manual testing using Tab, Enter, Space, and Esc keys exclusively.

## Known Issues and Workarounds
- The Canvas background particle animation (if implemented) is purely decorative and hidden from screen readers via `aria-hidden="true"`. It automatically disables if `prefers-reduced-motion` is active.

## Testing Methodology
Accessibility testing is a mandatory step before deploying new features. It involves:
1. Automated scans (Lighthouse).
2. Keyboard-only navigation check.
3. Screen reader testing.

## Screen Reader Testing Notes
Tested with:
- **VoiceOver (macOS/iOS)**
- **NVDA (Windows)**

Forms have been explicitly tested to ensure `<label>` elements properly announce the corresponding `<input>` fields.
