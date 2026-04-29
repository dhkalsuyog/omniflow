import os

with open('flowai.html', 'r') as f:
    lines = f.readlines()

header = []
footer = []
in_header = True
in_footer = False

for i, line in enumerate(lines):
    if '<!-- ============ HERO ============ -->' in line:
        in_header = False
    
    if '<!-- ============ FOOTER ============ -->' in line:
        in_footer = True
        
    if in_header:
        header.append(line)
    if in_footer:
        footer.append(line)

header_str = "".join(header)
footer_str = "".join(footer)

# Now, we define the content for each page

page_404 = """
    <!-- ============ HERO 404 ============ -->
    <section class="hero" style="min-height: 80vh; padding-top: 12rem;">
        <canvas class="hero-canvas" id="heroCanvas"></canvas>
        <div class="orb orb-violet" style="width: 600px; height: 600px; top: 50%; left: 50%; transform: translate(-50%, -50%);"></div>
        <div class="orb orb-pink" style="width: 500px; height: 500px; top: 50%; left: 50%; transform: translate(-50%, -50%); animation-direction: reverse;"></div>

        <div class="container hero-content">
            <h1 style="font-size: clamp(6rem, 15vw, 12rem); margin-bottom: 0.5rem;" class="gradient-text">404</h1>
            <p class="hero-subtitle" style="font-size: 1.5rem; color: var(--text-primary); margin-bottom: 3rem;">This page took a wrong turn</p>
            <div class="hero-cta">
                <a href="flowai.html" class="btn btn-primary btn-large">Back home <span aria-hidden="true">→</span></a>
            </div>
            
            <div class="hero-mockup" style="max-width: 400px; margin-top: 3rem; transform: rotate(-5deg);">
                <div class="mockup-frame" style="padding: 2rem; text-align: center; background: rgba(13, 18, 32, 0.7);">
                    <div style="font-family: 'JetBrains Mono', monospace; color: var(--accent-secondary); font-size: 1.2rem;">Error: Page_Not_Found</div>
                    <div style="color: var(--text-muted); font-size: 0.9rem; margin-top: 1rem;">System anomaly detected. Rerouting required.</div>
                </div>
            </div>
        </div>
    </section>
"""

page_privacy = """
    <style>
        .legal-content {
            max-width: 720px;
            margin: 0 auto;
            color: var(--text-secondary);
            font-size: 1.05rem;
        }
        .legal-content h2, .legal-content h3 {
            color: var(--text-primary);
            margin-top: 3rem;
            margin-bottom: 1.5rem;
        }
        .legal-content p {
            margin-bottom: 1.5rem;
        }
        .legal-content ul {
            list-style: disc;
            margin-left: 1.5rem;
            margin-bottom: 1.5rem;
        }
        .legal-content li {
            margin-bottom: 0.5rem;
        }
    </style>
    <section class="hero" style="min-height: auto; padding-top: 10rem; padding-bottom: 2rem;">
        <div class="orb orb-violet" style="top: -10%; left: -10%;"></div>
        <div class="container hero-content">
            <span class="eyebrow">// Legal</span>
            <h1 style="font-size: clamp(2.5rem, 5vw, 4.5rem);">Privacy Policy</h1>
            <p class="hero-subtitle">Last updated: October 24, 2025</p>
        </div>
    </section>
    
    <section style="padding-top: 2rem; padding-bottom: 6rem;">
        <div class="container">
            <div class="legal-content">
                <h2>Information Collected</h2>
                <p>We collect information you provide directly to us when you create an account, update your profile, use the interactive features of our services, participate in contests, promotions or surveys, request customer support, or otherwise communicate with us.</p>
                <ul>
                    <li>Account information (name, email, password)</li>
                    <li>Profile information</li>
                    <li>Payment information</li>
                    <li>Communication data</li>
                </ul>
                
                <h2>How We Use</h2>
                <p>We use the information we collect to provide, maintain, and improve our services, such as to administer your account, process transactions, and send you related information, including confirmations and invoices.</p>
                
                <h2>Sharing</h2>
                <p>We do not share your personal information with third parties except as described in this privacy policy or in connection with the services provided.</p>
                
                <h2>Your Rights</h2>
                <p>You have the right to access, correct, or delete your personal data. You can also object to processing and request data portability.</p>
                
                <h2>Contact</h2>
                <p>If you have any questions about this Privacy Policy, please contact us at privacy@flowai.com.</p>
            </div>
        </div>
    </section>
"""

page_terms = """
    <style>
        .legal-content {
            max-width: 720px;
            margin: 0 auto;
            color: var(--text-secondary);
            font-size: 1.05rem;
        }
        .legal-content h2, .legal-content h3 {
            color: var(--text-primary);
            margin-top: 3rem;
            margin-bottom: 1.5rem;
        }
        .legal-content p {
            margin-bottom: 1.5rem;
        }
    </style>
    <section class="hero" style="min-height: auto; padding-top: 10rem; padding-bottom: 2rem;">
        <div class="orb orb-cyan" style="top: -10%; right: -10%;"></div>
        <div class="container hero-content">
            <span class="eyebrow">// Legal</span>
            <h1 style="font-size: clamp(2.5rem, 5vw, 4.5rem);">Terms of Service</h1>
            <p class="hero-subtitle">Last updated: October 24, 2025</p>
        </div>
    </section>
    
    <section style="padding-top: 2rem; padding-bottom: 6rem;">
        <div class="container">
            <div class="legal-content">
                <h2>Acceptance</h2>
                <p>By accessing or using our services, you agree to be bound by these Terms of Service. If you do not agree to these terms, you may not access or use the services.</p>
                
                <h2>Account</h2>
                <p>You are responsible for safeguarding the password that you use to access the services and for any activities or actions under your password. We encourage you to use "strong" passwords.</p>
                
                <h2>Payments</h2>
                <p>All fees are exclusive of all taxes, levies, or duties imposed by taxing authorities, and you shall be responsible for payment of all such taxes, levies, or duties.</p>
                
                <h2>Termination</h2>
                <p>We may terminate or suspend your account and bar access to the service immediately, without prior notice or liability, under our sole discretion, for any reason whatsoever and without limitation, including but not limited to a breach of the Terms.</p>
                
                <h2>Liability</h2>
                <p>In no event shall FlowAI, nor its directors, employees, partners, agents, suppliers, or affiliates, be liable for any indirect, incidental, special, consequential or punitive damages.</p>
            </div>
        </div>
    </section>
"""

page_contact = """
    <style>
        .contact-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: center;
        }
        @media (max-width: 860px) {
            .contact-grid {
                grid-template-columns: 1fr;
            }
        }
        .contact-form {
            background: rgba(13, 18, 32, 0.6);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border-subtle);
            border-radius: 24px;
            padding: 3rem;
        }
        .form-group {
            margin-bottom: 1.5rem;
        }
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            color: var(--text-secondary);
            font-size: 0.9rem;
            font-weight: 500;
        }
        .form-group input, .form-group textarea {
            width: 100%;
            background: rgba(0, 0, 0, 0.2);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            padding: 1rem;
            color: var(--text-primary);
            font-family: inherit;
            transition: border-color 0.3s;
        }
        .form-group input:focus, .form-group textarea:focus {
            outline: none;
            border-color: var(--accent-primary);
        }
        .form-group textarea {
            min-height: 150px;
            resize: vertical;
        }
        .contact-info h3 {
            font-size: 2rem;
            margin-bottom: 1rem;
        }
        .contact-info p {
            color: var(--text-secondary);
            margin-bottom: 2rem;
        }
        .info-card {
            background: rgba(13, 18, 32, 0.6);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border-subtle);
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        .info-card .icon {
            width: 48px;
            height: 48px;
            border-radius: 12px;
            background: var(--gradient-primary);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .info-card .details h4 {
            font-size: 1.1rem;
            margin-bottom: 0.2rem;
        }
        .info-card .details p {
            color: var(--text-secondary);
            margin-bottom: 0;
            font-size: 0.9rem;
        }
    </style>
    <section class="hero" style="min-height: 100vh; padding-top: 8rem; display: flex; align-items: center;">
        <div class="orb orb-violet" style="top: 20%; left: -10%;"></div>
        <div class="orb orb-pink" style="bottom: 10%; right: -10%;"></div>
        
        <div class="container">
            <div class="contact-grid">
                <div class="contact-form-wrapper">
                    <form class="contact-form" action="https://formspree.io/f/placeholder" method="POST" id="contactPageForm">
                        <h2 style="margin-bottom: 2rem; font-size: 2rem;">Get in touch</h2>
                        <div class="form-group">
                            <label for="name">Name</label>
                            <input type="text" id="name" name="name" required placeholder="Jane Doe">
                        </div>
                        <div class="form-group">
                            <label for="email">Email</label>
                            <input type="email" id="email" name="email" required placeholder="jane@company.com">
                        </div>
                        <div class="form-group">
                            <label for="subject">Subject</label>
                            <input type="text" id="subject" name="subject" required placeholder="How can we help?">
                        </div>
                        <div class="form-group">
                            <label for="message">Message</label>
                            <textarea id="message" name="message" required placeholder="Tell us more about your needs..."></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary" style="width: 100%;">
                            <span class="btn-label">Send Message</span>
                            <span class="spinner" style="display:none;"></span>
                        </button>
                        <div id="contactFormMsg" style="margin-top: 1rem; text-align: center; font-size: 0.9rem;"></div>
                    </form>
                </div>
                
                <div class="contact-info">
                    <h3>Let's build something <span class="gradient-text">incredible</span>.</h3>
                    <p>Whether you have a question about features, trials, pricing, or anything else, our team is ready to answer all your questions.</p>
                    
                    <div class="info-card">
                        <div class="icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                        </div>
                        <div class="details">
                            <h4>Email Us</h4>
                            <p>hello@flowai.com</p>
                        </div>
                    </div>
                    
                    <div class="info-card">
                        <div class="icon" style="background: linear-gradient(135deg, #06b6d4, #7c3aed);">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                        </div>
                        <div class="details">
                            <h4>Discord Community</h4>
                            <p>Join 5,000+ members</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <script>
        // Inline script for contact form handling similar to the email form
        document.addEventListener('DOMContentLoaded', () => {
            const form = document.getElementById('contactPageForm');
            const msg = document.getElementById('contactFormMsg');
            const btnLabel = form.querySelector('.btn-label');
            const spinner = form.querySelector('.spinner');
            
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                // Validate email
                const email = form.querySelector('#email').value;
                if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                    msg.textContent = 'Please enter a valid email address.';
                    msg.style.color = '#ff5f57';
                    return;
                }
                
                // Simulate loading
                btnLabel.style.display = 'none';
                spinner.style.display = 'inline-block';
                
                setTimeout(() => {
                    spinner.style.display = 'none';
                    btnLabel.style.display = 'inline-block';
                    btnLabel.textContent = 'Message Sent ✓';
                    msg.textContent = "Thanks! We'll get back to you shortly.";
                    msg.style.color = '#28c840';
                    form.reset();
                    
                    if (typeof fireConfetti === 'function') {
                        fireConfetti();
                    }
                }, 1500);
            });
        });
    </script>
"""

page_about = """
    <style>
        .about-story {
            max-width: 800px;
            margin: 0 auto 6rem;
            text-align: center;
            font-size: 1.15rem;
            color: var(--text-secondary);
        }
        .bento-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.5rem;
            margin-bottom: 6rem;
        }
        .bento-item {
            background: rgba(13, 18, 32, 0.6);
            border: 1px solid var(--border-subtle);
            border-radius: 24px;
            padding: 2.5rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            min-height: 250px;
        }
        .bento-item.large {
            grid-column: span 2;
        }
        .bento-item h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }
        .bento-item p {
            color: var(--text-secondary);
        }
        .bento-icon {
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            background: var(--gradient-primary);
            -webkit-background-clip: text;
            color: transparent;
        }
        .team-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
            margin-bottom: 6rem;
        }
        .team-card {
            text-align: center;
        }
        .team-avatar {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            margin: 0 auto 1.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.5rem;
            font-weight: 700;
            color: white;
            border: 4px solid var(--bg-surface);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
        .team-avatar.a1 { background: linear-gradient(135deg, #7c3aed, #ec4899); }
        .team-avatar.a2 { background: linear-gradient(135deg, #06b6d4, #7c3aed); }
        .team-avatar.a3 { background: linear-gradient(135deg, #ec4899, #f59e0b); }
        
        .team-card h4 {
            font-size: 1.25rem;
            margin-bottom: 0.2rem;
        }
        .team-card p {
            color: var(--accent-cyan);
            font-size: 0.9rem;
            font-family: 'JetBrains Mono', monospace;
        }
        @media (max-width: 860px) {
            .bento-grid, .team-grid {
                grid-template-columns: 1fr;
            }
            .bento-item.large {
                grid-column: span 1;
            }
        }
    </section>
    </style>
    
    <section class="hero" style="min-height: 60vh; padding-top: 10rem; display: flex; align-items: center; text-align: center;">
        <canvas class="hero-canvas" id="heroCanvas"></canvas>
        <div class="orb orb-violet" style="top: 20%; left: 20%;"></div>
        <div class="orb orb-cyan" style="bottom: 10%; right: 20%;"></div>
        <div class="container hero-content">
            <h1 style="font-size: clamp(3rem, 6vw, 5.5rem); margin-bottom: 1.5rem;">Built by makers,<br>for <span class="gradient-text">makers.</span></h1>
            <p class="hero-subtitle">We believe AI shouldn't replace human creativity, it should amplify it. That's why we built FlowAI.</p>
        </div>
    </section>

    <section style="padding-top: 0; padding-bottom: 4rem;">
        <div class="container">
            <div class="about-story reveal">
                <p>It started with a simple observation: modern teams spend more time managing work than actually doing it. Switching contexts, updating statuses, searching for docs, writing boilerplates. We set out to build a workspace that handles the busywork so you can focus on the life's work. FlowAI is the manifestation of that vision—a unified environment where your tools, your data, and your team move as one.</p>
            </div>
            
            <div class="section-head reveal" style="margin-bottom: 3rem;">
                <h2>Why <span class="gradient-text">FlowAI</span></h2>
            </div>
            
            <div class="bento-grid reveal-stagger">
                <div class="bento-item large">
                    <div class="bento-icon">⚡</div>
                    <h3>Velocity above all</h3>
                    <p>We optimize for speed in everything we do. From our lightweight client architecture to our predictive AI models, FlowAI is designed to keep you in the flow state.</p>
                </div>
                <div class="bento-item">
                    <div class="bento-icon">🔒</div>
                    <h3>Privacy by design</h3>
                    <p>Your data is yours. We use zero-knowledge encryption and never use your private workspaces to train our foundation models.</p>
                </div>
                <div class="bento-item">
                    <div class="bento-icon">🧩</div>
                    <h3>Infinitely extensible</h3>
                    <p>Every team works differently. Our open plugin ecosystem and robust API means FlowAI molds to your process, not the other way around.</p>
                </div>
                <div class="bento-item large">
                    <div class="bento-icon">🤝</div>
                    <h3>Multiplayer native</h3>
                    <p>Work is collaborative. Presence, real-time sync, and intelligent conflict resolution are built directly into the core engine, not added as afterthoughts.</p>
                </div>
            </div>
            
            <div class="section-head reveal" style="margin-top: 8rem; margin-bottom: 4rem;">
                <h2>The <span class="gradient-text">Leadership</span> Team</h2>
            </div>
            
            <div class="team-grid reveal-stagger">
                <div class="team-card">
                    <div class="team-avatar a1">SD</div>
                    <h4>Suyog Dhakal</h4>
                    <p>CEO & FOUNDER</p>
                </div>
                <div class="team-card">
                    <div class="team-avatar a2">AK</div>
                    <h4>Alex Kim</h4>
                    <p>CTO</p>
                </div>
                <div class="team-card">
                    <div class="team-avatar a3">MJ</div>
                    <h4>Maya Jenkins</h4>
                    <p>HEAD OF PRODUCT</p>
                </div>
            </div>
        </div>
    </section>

    <!-- REUSE CTA -->
    <section class="final-cta" id="cta">
        <div class="orb orb-violet"></div>
        <div class="container reveal">
            <h2>Your team's <span class="gradient-text">AI advantage</span><br>starts today</h2>
            <p>Join 12,847 teams already moving faster.</p>
            <form class="email-form" id="emailForm" novalidate>
                <input type="email" id="emailInput" placeholder="you@company.com" autocomplete="email" required>
                <button type="submit">
                    <span class="btn-label">Get Started →</span>
                    <span class="spinner"></span>
                </button>
            </form>
            <div class="form-msg" id="formMsg"></div>
            <p class="trust-line">No credit card · Free forever plan · Cancel anytime</p>
            <div class="trust-badges">
                <span class="trust-badge">🔒 SOC2 Certified</span>
                <span class="trust-badge">⭐ 4.9/5 Rating</span>
                <span class="trust-badge">🌍 50+ Countries</span>
            </div>
        </div>
    </section>
"""

pages = {
    '404.html': page_404,
    'privacy.html': page_privacy,
    'terms.html': page_terms,
    'contact.html': page_contact,
    'about.html': page_about
}

# Change title for each page based on the page name
import re
for filename, content in pages.items():
    page_header = header_str
    
    # Change title tag
    title_match = re.search(r'<title>(.*?)</title>', page_header)
    if title_match:
        original_title = title_match.group(1)
        if filename == '404.html':
            new_title = 'Page Not Found — FlowAI'
        elif filename == 'privacy.html':
            new_title = 'Privacy Policy — FlowAI'
        elif filename == 'terms.html':
            new_title = 'Terms of Service — FlowAI'
        elif filename == 'contact.html':
            new_title = 'Contact Us — FlowAI'
        elif filename == 'about.html':
            new_title = 'About Us — FlowAI'
        page_header = page_header.replace(f'<title>{original_title}</title>', f'<title>{new_title}</title>')
    
    # Write file
    with open(filename, 'w') as f:
        f.write(page_header)
        f.write(content)
        f.write(footer_str)

print("Pages generated successfully.")
