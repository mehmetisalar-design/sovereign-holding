# Security checklist

- [x] Password hashing through Werkzeug; no default admin account/password.
- [x] CSRF protection via Flask-WTF for state-changing forms.
- [x] Admin-only access to admin pages and private evidence downloads.
- [x] ORM parameterization for database operations; Jinja autoescaping for template output.
- [x] Secure, random filenames for payment evidence; extension and basic signature validation; upload size cap.
- [x] Server recalculates cart prices and checks stock at checkout.
- [x] No raw card data or live provider secrets in the repository.
- [x] Audit records for key admin actions and payment evidence submission/review.
- [ ] Add login rate limiting and stronger abuse controls before production.
- [ ] Add database-backed idempotency and concurrency-safe stock reservation/rollback for concurrent checkouts.
- [ ] Add malware scanning and hardened content parsing for uploads; use private object storage in production.
- [ ] Add password reset with signed expiring tokens, email verification, and account recovery safeguards.
- [ ] Configure HTTPS, HSTS and additional security headers at the production edge.
- [ ] Use PostgreSQL, migrations, backups and tested restore procedures.
- [ ] Review data retention, privacy notices, cookie practices and jurisdiction-specific consumer rights.
- [ ] Run dependency scanning, static analysis and penetration testing before accepting live customers.
