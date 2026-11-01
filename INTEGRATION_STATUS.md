# Implementation and integration status

## Implemented in this starter
- Responsive storefront, home page, shop listing, product detail pages, category filtering, search, sorting, pagination.
- Product catalog and categories stored in SQLAlchemy models; sample products explicitly marked.
- Session cart with server-side price calculation and stock validation.
- Guest checkout; unique random order references; order items persisted; stock deducted when order is created.
- Order confirmation and tracking with reference + checkout email.
- Manual bank transfer instructions configurable in admin settings; no real bank details supplied.
- Payment evidence upload with extension and basic file-signature checks, random server-side filename, size limit, private directory and admin-only download route.
- Admin authentication, product creation/editing/deletion or safe unpublishing, stock editing, validated product image uploads, order status transitions, evidence review and audit events.
- WhatsApp click-to-chat links with prefilled product details and a persistent floating customer-support button; configured default number +44 7352 794862. A click-to-chat link does not send a message automatically.
- Editable starter policy pages, Windows startup script, `.env.example`, automated tests.

## Tests
The automated suite is included in `tests/test_store.py`. Source compilation and archive integrity were checked for this package. A regression test was added for the persistent WhatsApp support button. The test suite could not be executed in the build environment because Flask and the required packages were not installed and package installation failed due to unavailable network/DNS. Run `python -m pytest -q` after installing `requirements.txt` on a machine with package access; do not treat unexecuted tests as passing.

## Not implemented or not live
- Customer registration, email verification, password reset and account deletion.
- Full product variants, category CRUD, coupons, tax engine, shipping zones/rates, shipping carrier APIs and tracking webhooks.
- Live card payments, payment provider SDK, signed payment webhooks and refunds through a payment provider.
- Official WhatsApp Cloud API messaging, templates, webhook processing, delivery status and consent/opt-out management.
- Email/SMS notifications and newsletter subscription storage/provider.
- Complete returns/refund operations, product review submissions/moderation, support tickets, discount codes, notification log UI and CSV export.
- Database migration framework and concurrency-safe inventory reservation suitable for high-volume production.
- Malware scanning and robust PDF/image decoding for payment evidence.
- Production hosting, HTTPS, PostgreSQL provisioning, backups, observability and legal review.

## Before launch
Replace sample catalog data and imagery, set a strong `SECRET_KEY`, configure correct currency/shipping/tax/policy information, supply valid bank details, review privacy and consumer law, deploy behind HTTPS with a production WSGI server, use private object storage, add rate limiting and malware scanning, add migrations and concurrency-safe inventory handling, and independently test every integration.


## Product-page checkout and USD update (2026-10-28)
- Product details include a prominent **Buy now — Checkout** action and quantity selector.
- Direct checkout carries only the selected product and selected quantity.
- USD is fixed across the customer journey and new orders store USD.
- Checkout includes State / Province as an optional delivery field.
- Sample imagery is now served from local SVG assets rather than relying on third-party image URLs. Admin product create/edit forms accept validated JPG, PNG and WEBP uploads. Source compilation was checked. Automated tests were not run in this environment because Flask dependencies could not be installed without network/DNS access.
