# Architecture

This document outlines the current architecture of FlowAI and the planned transition to a modern SaaS stack.

## Current Architecture (Static HTML/CSS/JS)
FlowAI currently runs as a static, vanilla web application. This ensures zero compilation steps, instant loading, and maximum baseline performance.

## File Structure
```
.
├── index.html         # Main entry point; semantic HTML5 structure
├── about.html         # About page
├── contact.html       # Contact page
├── privacy.html       # Privacy policy
├── terms.html         # Terms of service
├── 404.html           # Error page
├── css/
│   ├── style.css      # Global styles, variables, typography, utilities
│   ├── components.css # Modular component styles (buttons, cards)
│   └── pages/         # Page-specific overrides
├── js/
│   ├── main.js        # Global initialization, event listeners
│   ├── animations.js  # Intersection observers, count-up logic
│   └── utils.js       # Helper functions
└── assets/
    ├── img/           # Optimized WebP/SVG images
    └── icons/         # SVG icons
```

## CSS Architecture
We utilize a strict CSS Custom Properties strategy:
- **Global Tokens**: Defined in `:root` (colors, spacing, typography).
- **Component Tokens**: Scoped to specific blocks (e.g., `--btn-bg`).
- **BEM Methodology**: Block Element Modifier pattern is used selectively for complex components to maintain flat specificity.

## JavaScript Modules
- **`main.js`**: Bootstraps the application, handles mobile navigation toggle, form submission mockups.
- **`animations.js`**: Manages `IntersectionObserver` for `.reveal` classes and choreographs the bento grid staggering.

## Animation Choreography Map
1. **Hero Load**: Opacity fade-in (0.5s) -> Transform Y-axis translation.
2. **Scroll Reveal**: Elements marked `.reveal` fade and slide up when 10% visible in the viewport.
3. **Staggered Lists**: Bento grid items delay their reveal by `nth-child * 100ms`.

## Performance Optimizations
- **Asset Loading**: Images are lazy-loaded (`loading="lazy"`).
- **CSS Delivery**: Critical CSS is inline (planned), non-critical is deferred.
- **JS Deferral**: Scripts are loaded with the `defer` attribute.
- **Hardware Acceleration**: Animations use `transform` and `opacity` exclusively to trigger GPU compositing.

## Browser Support Matrix
- Chrome: Last 2 versions
- Firefox: Last 2 versions
- Safari: Last 2 versions
- Edge: Last 2 versions
- iOS Safari: Last 2 versions
- Android Chrome: Last 2 versions

## Known Limitations
- No backend persistence for contact forms.
- Static content requires manual updates.
- No user authentication or dynamic data loading.

## Future Architecture (Next.js)
See [MIGRATION_TO_NEXTJS.md](MIGRATION_TO_NEXTJS.md) for the detailed blueprint to move to Next.js 14, React Server Components, and Supabase.
