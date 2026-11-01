# Production deployment outline

1. Choose a host that supports Python/Flask and a production WSGI server. Do not use `flask run` as the public production server.
2. Point DNS records to the host and enable HTTPS with automatic certificate renewal.
3. Set `FLASK_ENV=production`, a long random `SECRET_KEY`, a managed `DATABASE_URL` (PostgreSQL recommended), and actual store configuration using the host's secret manager.
4. Run database migrations as part of a controlled release. This starter initializes tables with `create_all`; introduce Alembic/Flask-Migrate before schema changes in production.
5. Use Gunicorn or another supported WSGI server behind a reverse proxy. Configure worker count and timeouts for the host.
6. Move payment evidence to private object storage with least-privilege access, encryption, retention limits and audit access. Never serve the upload directory as static public files.
7. Configure backups for database and files, enable monitoring/error reporting, rotate logs, and rehearse restores.
8. Configure email, payment, WhatsApp and shipping providers only after eligibility checks and test-mode end-to-end verification.
9. Add rate limiting, malware scanning, security headers, dependency scanning and a security review.
10. Replace sample products/images and finalize all policy copy with legal review before taking real orders.

No domain, email, payment provider, WhatsApp Cloud API, carrier, or production database credentials were supplied, so no live integration is claimed.
