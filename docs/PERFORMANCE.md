# Performance Metrics & Optimizations

## Current Lighthouse Scores (Target)
- **Performance**: 98-100
- **Accessibility**: 100
- **Best Practices**: 100
- **SEO**: 100

## Optimizations Applied

### 1. Asset Delivery
- All images utilize the `loading="lazy"` attribute, except for critical above-the-fold content (Hero section).
- SVGs are used for icons and illustrations to ensure infinite scaling and minimal file sizes.

### 2. CSS Delivery
- Core styles are minimal and structured to prevent render-blocking.
- Heavy use of CSS custom properties for efficient repainting during theme changes.

### 3. JavaScript Execution
- All scripts are loaded with the `defer` attribute, meaning they execute only after the HTML document is fully parsed.
- Vanilla JS means zero framework overhead, resulting in Time to Interactive (TTI) matching the First Contentful Paint (FCP).
- Intersection Observers are used for scroll events instead of `window.addEventListener('scroll')`, drastically reducing main thread blocking.

### 4. Animation Performance
- Animations exclusively modify `opacity` and `transform` properties.
- This delegates the animation work to the GPU via compositing, ensuring a smooth 60fps experience without layout thrashing.

## Performance Budget
For future development (Next.js Migration):
- Max First JavaScript Bundle Size: 100KB (gzipped).
- Max Total Image Payload per page: 500KB.
- LCP (Largest Contentful Paint) must remain under 1.5s on a simulated 4G network.

## How to Test Locally
1. Run a local web server (e.g., `npx serve .`).
2. Open Chrome Developer Tools.
3. Navigate to the "Lighthouse" tab.
4. Select "Mobile" device, check all categories, and click "Analyze page load".

## How to Monitor in Production
- **Vercel Analytics**: Provides real-world Core Web Vitals data based on actual user sessions.
- **PageSpeed Insights**: Use the API to run automated tests via CI/CD pipelines (Lighthouse CI).
