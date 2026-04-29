# Design System

## Design Philosophy
FlowAI is built on the principles of **Clarity, Fluidity, and Depth**. The UI must feel organic yet highly technical, utilizing glassmorphism, subtle glowing effects, and a dark-mode-first aesthetic to represent "The Intelligence Layer."

## Color System
Our palette is rooted in dark, space-like backgrounds with vibrant, energetic accents.

| Token | Hex | HSL | Usage |
|-------|-----|-----|-------|
| `--bg-base` | `#0a0a0a` | `0, 0%, 4%` | Main page background |
| `--bg-surface` | `#141414` | `0, 0%, 8%` | Cards, modals, dropdowns |
| `--text-primary` | `#ffffff` | `0, 0%, 100%` | Headings, active states |
| `--text-secondary`| `#a1a1aa` | `240, 5%, 65%`| Body text, inactive icons |
| `--accent-primary`| `#3b82f6` | `217, 91%, 60%`| Primary buttons, links |
| `--accent-glow` | `#8b5cf6` | `258, 90%, 66%`| Neon highlights, gradients |

### Gradients
- **Hero Text**: `linear-gradient(135deg, var(--text-primary), var(--text-secondary))`
- **Orb Background**: `radial-gradient(circle at center, var(--accent-glow), transparent 70%)`

## Typography
**Font Family**: `Inter`, `sans-serif` (Chosen for exceptional readability at small sizes and a modern, tech-forward geometric structure).

**Type Scale**:
- `h1`: `clamp(2.5rem, 5vw, 4rem)`
- `h2`: `clamp(2rem, 4vw, 3rem)`
- `h3`: `clamp(1.5rem, 3vw, 2rem)`
- `body`: `1rem` (16px) base
- `small`: `0.875rem`

## Spacing System
Based on a `4px` baseline grid.
- `--spacing-xs`: 0.25rem (4px)
- `--spacing-sm`: 0.5rem (8px)
- `--spacing-md`: 1rem (16px)
- `--spacing-lg`: 2rem (32px)
- `--spacing-xl`: 4rem (64px)
- `--section-padding`: `clamp(4rem, 10vh, 8rem)`

## Effects
- **Glassmorphism**: `background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.05);`
- **Glow**: `box-shadow: 0 0 20px rgba(139, 92, 246, 0.15);`

## Components Catalog
- **Buttons**:
  - Primary: Filled accent background, subtle hover glow.
  - Secondary: Glassmorphic background, border, text accent on hover.
- **Cards**:
  - Bento Grid: Distinct border-radius (`24px`), hover lift (`translateY(-4px)`).
  - Pricing: Highlighted tier gets an animated gradient border.
- **Badges**: Pill-shaped, small text, subtle background tint based on status.

## Animation Principles
- **Easing**: `cubic-bezier(0.16, 1, 0.3, 1)` (snappy start, smooth finish).
- **Duration**: Fast interactions (150ms), structural reveals (600ms).
- **Stagger**: 100ms offset for lists and bento items.

## Responsive Breakpoints
- `mobile`: `< 768px`
- `tablet`: `768px - 1024px`
- `desktop`: `1024px - 1440px`
- `ultrawide`: `> 1440px`

## Accessibility Tokens
- Minimum contrast ratio enforced: 4.5:1 for text.
- Focus rings: `outline: 2px solid var(--accent-primary); outline-offset: 2px;`
