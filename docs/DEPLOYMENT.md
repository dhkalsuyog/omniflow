# Deployment Strategy

## Hosting Comparison
- **Vercel**: Best-in-class for Next.js, Edge network, zero-config CI/CD. Ideal for our stack.
- **Netlify**: Excellent alternative, strong edge functions, but slightly less optimized for the bleeding-edge Next.js App Router features.
- **Cloudflare Pages**: Great for purely static sites, but backend API routes require careful adaptation to Cloudflare Workers.

**Recommended Platform:** Vercel (Aligns perfectly with the Next.js migration plan).

## Step-by-Step Vercel Deployment
1. **Create GitHub Repo**: Push the local codebase to a new public/private GitHub repository.
2. **Connect Vercel to Repo**: Log into Vercel, click "Add New Project", and import the GitHub repository.
3. **Configure Build Settings**:
   - Framework Preset: Vercel will auto-detect HTML (for current phase) or Next.js (future).
   - Build Command: `npm run build` (Next.js phase).
   - Output Directory: `.next` (Next.js phase) or root (current).
4. **Add Environment Variables**: Paste production keys for Supabase, Stripe, etc., into the Vercel dashboard.
5. **Deploy**: Click Deploy and wait for the build to finish.

## Custom Domain Setup
- **Buying a Domain**: Namecheap or Cloudflare Registrar recommended for low renewal costs.
- **DNS Configuration**: In Vercel, go to Settings -> Domains. Add your domain. Vercel provides A Records and CNAME records to add to your DNS provider.
- **HTTPS Setup**: Vercel automatically provisions and renews SSL certificates via Let's Encrypt. No manual setup required.

## CI/CD with GitHub Actions
Create automated workflows in `.github/workflows/`:
- **Lint Check Workflow**: Runs `npm run lint` on every Pull Request to main.
- **Lighthouse CI Workflow**: Runs performance audits against preview deployments to prevent regressions.

## Preview Deployments
Vercel automatically creates a unique Preview URL for every Pull Request. This allows for staging tests and stakeholder reviews before merging to production.

## Rollback Strategy
If a bad deploy hits production, go to Vercel Deployments dashboard, select the previous successful deployment, and click **"Promote to Production"**. This process is instantaneous.

## Monitoring Setup
- **Vercel Analytics**: Enable in dashboard for real-time traffic and Web Vitals tracking.
- **Sentry**: (Future) Integrate for error tracking and exception monitoring in Next.js APIs.

## Cost Breakdown
- **Free Tier (Hobby)**: Sufficient for the portfolio phase and early SaaS MVP. Includes 100GB bandwidth and Edge network caching.
- **When to Upgrade ($20/mo Pro Tier)**: 
  - Need more team members to access Vercel dashboard.
  - Hitting Serverless Function execution limits.
  - Require concurrent builds.
