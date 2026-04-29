# Roadmap

## Vision: From Portfolio to Product
The goal is to transition FlowAI from a static, highly-polished frontend portfolio piece into a fully functional, revenue-generating SaaS product utilizing AI APIs.

### Phase 1: Portfolio Piece ✅
- Static HTML/CSS/JS architecture.
- High-end bento grid UI, glassmorphism, and scroll animations.
- Accessibility (WCAG 2.1 AA) and performance optimizations.
- Responsive design across all major device breakpoints.
- Essential secondary pages (Privacy, Terms, Contact, About, 404).

### Phase 2: Polish & Multi-page (Next 30 days)
- Convert pure HTML/CSS into reusable component fragments.
- Expand the blog and case studies sections with static Markdown generation.
- Implement advanced Canvas/WebGL background animations.
- Refine copywriting and finalize all SEO metadata.

### Phase 3: Backend & Auth (60-90 days)
- **Tech Stack**: Next.js 14 (App Router), Supabase (Auth & DB), Resend (Emails), Stripe (Billing).
- Migrate UI to React/TailwindCSS (or maintain pure CSS Modules).
- **Features**: User authentication (Google, Github, Magic Link).
- **Database Schema**: Users, Workspaces, AI_Prompts, API_Usage_Logs.
- Setup protected routes and basic dashboard shell.

### Phase 4: MVP Launch (90-180 days)
- **User Dashboard**: Real data visualization, prompt management, and API key generation.
- **AI Integration**: Connect to OpenAI/Anthropic APIs for core product features.
- **Pricing Tiers**: Connect Stripe, setup webhooks for subscription management.
- **Onboarding Flow**: Interactive product tour for new signups.

### Phase 5: Scale (180+ days)
- **Team Workspaces**: Role-based access control (RBAC), multi-user billing.
- **Integrations**: Zapier, Slack, Discord webhook integrations.
- **Mobile App**: Evaluate React Native / Expo for companion app.
- Enterprise SSO and advanced compliance features.

## Feature Wishlist
- **Must-have**: AI Prompt templates, Usage analytics, Secure API key vault.
- **Nice-to-have**: Dark/Light mode toggle, Custom dashboard layouts.
- **Dream**: Custom LLM fine-tuning per user workspace.

## Tech Debt to Address
- Current vanilla JS lacks type safety.
- CSS variables could be formalized into a strict CSS-in-JS or Tailwind config during Next.js migration.
- Manual DOM manipulation needs to be phased out in favor of declarative React state.

## Inspiration & Competitors
- **Vercel**: Dashboard UX, typography, and edge network speed.
- **Linear**: Dark mode execution, keyboard shortcuts, and micro-interactions.
- **Stripe**: API documentation quality and checkout experience.

## Success Metrics
- 90+ Lighthouse scores across all metrics.
- < 1s Largest Contentful Paint (LCP).
- 5% Conversion rate from Landing Page to Signup.
