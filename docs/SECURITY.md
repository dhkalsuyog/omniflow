# Security

This document outlines the planned security posture for FlowAI's transition to a SaaS product. Currently, as a static site, the attack surface is minimal.

## Security Headers Explained
Once deployed (or migrated to Next.js), the following HTTP headers must be enforced:
- `Strict-Transport-Security`: Enforces HTTPS.
- `X-Frame-Options: DENY`: Prevents clickjacking by disabling embedding in iframes.
- `X-Content-Type-Options: nosniff`: Prevents MIME-sniffing attacks.
- `Referrer-Policy: strict-origin-when-cross-origin`: Protects referral information.
- `Content-Security-Policy (CSP)`: Restricts where scripts, images, and styles can be loaded from.

## Form Security
Future dynamic forms must implement:
- **CSRF Protection**: Tokens to prevent Cross-Site Request Forgery.
- **Rate Limiting**: On login, signup, and contact endpoints to prevent brute force and spam.
- **Input Validation**: Strict server-side validation and sanitization of all user inputs before database insertion.

## API Security Plans
- **Authentication**: JWT-based session management via Supabase.
- **Authorization**: Row Level Security (RLS) policies in PostgreSQL ensuring users only access their own tenant data.
- **API Keys**: User-generated API keys must be hashed in the database and only shown once to the user upon creation.

## Data Handling Principles
- We do not store sensitive payment information directly; it is vaulted with Stripe.
- Passwords are never stored in plaintext (handled securely by Supabase Auth).
- AI Prompts processed through external APIs (OpenAI) must adhere to their data privacy agreements (e.g., zero retention for training).

## Vulnerability Reporting
We take security seriously. If you discover a vulnerability, please do not disclose it publicly.
Instead, email `security@flowai.com` with a detailed description. We will acknowledge receipt within 48 hours and work to issue a fix promptly.
