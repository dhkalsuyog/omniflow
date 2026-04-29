# Migration to Next.js

This document serves as the master blueprint for migrating FlowAI from a static HTML/CSS/JS architecture to a modern Next.js SaaS product.

## Why Migrate
While static files are perfect for a portfolio, a SaaS product requires:
- User authentication and session management.
- Dynamic data fetching and database interactions.
- Protected routes and customized dashboards.
- Server-side API integration (Stripe webhooks, AI endpoints).

## Pre-migration Checklist
- [ ] Audit all current vanilla CSS variables and animations.
- [ ] Ensure all assets (images, icons) are optimized and ready for Next.js `Image` component.
- [ ] Finalize the static HTML structure to ease the React JSX conversion.

## Step-by-Step Migration

### 1. Initialize Next.js 14 Project
```bash
npx create-next-app@latest flowai-saas
# Options: TypeScript (Yes), ESLint (Yes), App Router (Yes), Tailwind (No - keep CSS custom)
```

### 2. Move Existing CSS
Copy `css/style.css` and `css/components.css` to `app/globals.css`. Ensure the CSS variables are preserved perfectly on the `:root`.

### 3. Convert HTML Pages to React Server Components
Map each static page to a route in the App Router:
- `index.html` -> `app/page.tsx`
- `about.html` -> `app/about/page.tsx`
- `contact.html` -> `app/contact/page.tsx`

*Template for converting page types:*
Convert `class` to `className`, `for` to `htmlFor`, and ensure all tags are self-closing where necessary (`<img>`, `<input>`).

### 4. Component Extraction Strategy
Break down the monolith into reusable React components in `/components`:
- `components/Nav.tsx`: Client component for mobile toggle.
- `components/Footer.tsx`: Server component.
- `components/HeroCanvas.tsx`: Client component for canvas particles.
- `components/BentoGrid.tsx`: Server component mapping over data.
- `components/PricingCard.tsx`: Client component for toggle state.
- `components/FAQItem.tsx`: Client component for accordion logic.
- `components/EmailForm.tsx`: Client component handling form state.

### 5. Convert JS to React Hooks
Replace `main.js` and `animations.js` logic with custom hooks:
- `useScrollReveal()`: Wraps IntersectionObserver logic using `useEffect` and `useRef`.
- `useCountUp()`: Handles number animations on scroll.
- `useTypewriter()`: Replaces typing effects in the hero section.
- `useScrollProgress()`: For the top progress bar.

### 6. Backend Setup (Supabase)
- Create a new Supabase project.
- **Database schema**:
  - `users`: ID, email, created_at, subscription_status.
  - `workspaces`: ID, name, owner_id.
  - `projects`: ID, workspace_id, name, settings.
  - `ai_actions`: ID, user_id, prompt, response, tokens_used.
- **RLS Policies**: Restrict access so users only see their own workspace data.
- **Auth Setup**: Configure Email/Password, Google OAuth, and Magic Links.

### 7. API Routes Structure
Create Next.js Route Handlers (`app/api/...`):
- `/api/auth/[...supabase]/route.ts`
- `/api/ai/generate/route.ts`
- `/api/stripe/webhook/route.ts`

### 8. Stripe Integration
- Create Products in Stripe Dashboard (Free, Pro, Enterprise).
- Implement webhook handling in Next.js to update Supabase `users.subscription_status`.
- Integrate Stripe Checkout and Customer Portal.

### 9. Email Setup (Resend)
- Define transactional templates using React Email.
- **Flows**: Welcome Email, Password Reset, Subscription confirmation.

### 10. Environment Variables Checklist
Ensure `.env.local` is set up. See `.env.example` for the required keys.

### 11. Testing Strategy
- Unit tests for custom hooks (`useScrollReveal`, etc.).
- Integration tests for Auth flows and Stripe Webhooks.
- E2E testing with Cypress or Playwright for critical paths.

## Migration Timeline Estimate
- **Phase 1 (Setup & UI Port)**: 15-20 hours
- **Phase 2 (Supabase Auth & DB)**: 15 hours
- **Phase 3 (Dashboard & AI APIs)**: 20-25 hours
- **Phase 4 (Stripe & Resend)**: 10-15 hours
- **Total**: ~60-75 hours of dedicated engineering time.
