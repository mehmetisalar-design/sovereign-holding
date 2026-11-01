# Atelier Home — Flask E-commerce Starter

A polished, responsive home and lifestyle storefront with a database-backed catalog, guest cart/checkout, inventory deduction, order references and tracking, manual bank-transfer evidence upload, admin order review, store settings, and WhatsApp click-to-chat links.

> **Honest status:** This is a functional starter implementation, not a fully production-ready commerce platform. Sample products and locally bundled illustrative SVG images are included for development; replace them with authorized product photography before launch. Automated WhatsApp Cloud API, live card payments, email delivery, shipping carrier APIs, customer registration, password reset, refunds processing, review moderation, full return workflows, migrations, and production monitoring are not implemented/live. See `INTEGRATION_STATUS.md` and `SECURITY_CHECKLIST.md`.

## Requirements

- Python 3.11+ recommended (compatible with Python 3.12)
- Internet connection for first-time dependency installation and remote sample imagery

## Windows quick start

1. Install Python from <https://www.python.org/downloads/> and enable **Add Python to PATH**.
2. Extract the project ZIP to a folder such as `C:\AtelierHome`.
3. Double-click `start_windows.bat`, or use the manual steps below.
4. Open <http://127.0.0.1:5000>.

The startup script creates a virtual environment, installs dependencies, copies `.env.example` to `.env` if needed, and starts the development server. Change `SECRET_KEY` in `.env` before using the app beyond local development.

### Manual setup

```powershell
cd C:\AtelierHome
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
python -m flask --app run.py run --host 127.0.0.1 --port 5000
```

The database tables and clearly marked sample catalog are initialized automatically on first app start. Stop the local server with `Ctrl+C`.

## Create the first administrator

Open a second terminal in the project folder, activate the virtual environment, then run:

```powershell
python -m flask --app run.py create-admin
# or: python create_admin.py
```

Enter an email, name, and a password of at least 12 characters. There is no default admin account or hard-coded admin password. Sign in at `/login`; the admin area is at `/admin`.

## Configure bank transfer safely

1. Sign in as an administrator.
2. Open **Store settings** from the admin navigation.
3. Enter the real beneficiary, bank name, account/transfer details, currency, and reference instructions. Save only details that belong to your business and are correct for your customers.
4. Do not accept transfers while payment details remain “Not configured”.
5. Customer evidence uploads remain private in the `uploads` directory and are served through an admin-authorized route. Verify the funds in the actual bank account before approving evidence. A screenshot alone is not confirmation.
6. Back up the database and private upload directory securely.

## WhatsApp

Basic click-to-chat uses the configured international phone digits, defaulting to `447352794862`. A floating **Need help? Chat on WhatsApp** customer-support button appears across storefront pages, and product pages include a prefilled product enquiry. Customers must click the link and send the prefilled message themselves. This project does not send automatic WhatsApp messages. Official Cloud API automation requires a Meta business setup, approved templates as applicable, access token, phone number ID, webhook verification, privacy/consent handling, and end-to-end tests; it is not enabled by this build.

## Live card payments

Card payments are not enabled. Configure an eligible payment provider only after confirming business and country eligibility. Use hosted checkout or the provider's approved secure components; implement signed webhook verification and idempotency before marking orders paid. Never collect or store raw card numbers or CVV. Do not treat screenshots as card-payment proof.

## Tests

The suite is included. Source compilation passed, but in the build environment Flask dependencies could not be installed because network/DNS access was unavailable, so the pytest suite did not pass or complete. See `TEST_REPORT.md` for the exact verification status. After installing dependencies on a machine with package access, run:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pytest -q
```

## Deployment

Do not deploy the Flask development server as production. For production, use a supported WSGI server behind HTTPS, PostgreSQL or another managed database, strong environment secrets, secure private object storage for payment evidence, backups and restore tests, error monitoring, log rotation, rate limiting, and reviewed policies. See `DEPLOYMENT.md` and `SECURITY_CHECKLIST.md`.

## Main routes

- `/` storefront
- `/shop` catalog/search/category filters
- `/cart` and `/checkout`
- `/track` order lookup using reference + checkout email
- `/payment-instructions`
- `/login` and `/account` (account area for existing users)
- `/admin`, `/admin/products`, `/admin/orders`, `/admin/settings`

## Sample data warning

Eight development sample products are seeded on a new database and marked “Sample product”. Replace their images, descriptions, stock, and pricing with authorized, accurate product information. Do not use sample listings as proof of real inventory, supplier relationships, ratings, or sales.
## Product-page direct checkout and USD currency

- Every product detail page has a prominent **Buy now — Checkout** button directly beside the quantity selector. It sends only that product and the selected quantity to checkout, replacing the current session cart for a clean direct-buy flow.
- The product page also has **Add to bag** for customers who want to continue shopping.
- Product, cart, checkout, order confirmation, tracking and admin order totals display USD (`$`) and new orders are stored with currency code `USD`. Sample product illustrations are bundled locally so catalog pages do not depend on external image URLs. Store currency is locked to USD in the admin settings to prevent accidental mixed-currency totals.
- Checkout collects contact details and delivery address including optional state/province. Prices and totals are recalculated on the server.
- Card payments are not activated; checkout records an order for the manual bank-transfer workflow. The order is not paid until the bank transfer is independently verified.


## Private product listings (drafts)

New products are saved as **Private draft** by default. Drafts appear in the signed-in admin product list only; they do not appear in the public shop, home page, search results, cart, or direct product URL. To make a listing visible, open **Admin → Products**, review/edit it, then use **Publish** (or tick **Published in store** on the edit page). Use **Unpublish** to hide it again. The first-run privacy migration also unpublishes legacy sample/demo products once, so the store owner can review them before showing them to customers.

## New order notifications (email + WhatsApp)

The checkout route now attempts notifications **after** the order is saved. Notification failures do not cancel the order. Set the following values in your private `.env` file (never commit/share that file):

- Email: `ORDER_NOTIFY_EMAIL`, `SMTP_HOST`, `SMTP_PORT`, `SMTP_USERNAME`, `SMTP_PASSWORD`, and optional `SMTP_FROM`. For Gmail, use an App Password where supported, not your normal account password. Other mail providers have different SMTP settings.
- WhatsApp: `ORDER_NOTIFY_WHATSAPP` (your recipient phone number in international digits, no `+`), `WHATSAPP_ACCESS_TOKEN`, `WHATSAPP_PHONE_NUMBER_ID`, `WHATSAPP_ORDER_TEMPLATE`, and `WHATSAPP_TEMPLATE_LANGUAGE`.

For WhatsApp automation, set up Meta WhatsApp Cloud API and create/approve a Utility template named to match `WHATSAPP_ORDER_TEMPLATE`, with one BODY placeholder `{{1}}` (for example: `New order notification: {{1}}`). The configured template language must match the approved template. Meta approval, token permissions, a valid sender phone number, and testing are required; the regular WhatsApp click-to-chat number alone cannot send automatic messages. Long order summaries may be split into multiple template messages. Keep access tokens and SMTP passwords secret.

After setting `.env`, restart the Flask app and place a test order with a non-sensitive test address. Check the app logs and both inboxes. Email/WhatsApp delivery is best-effort; if credentials are missing or a provider rejects a message, the order remains saved and the failure is logged. Customer delivery addresses are personal data: restrict admin access and do not use real customer details for tests without permission.


## Product gallery images and videos

In Admin → Products, add a cover image, select multiple additional JPG/PNG/WEBP images, and optionally upload one MP4/WEBM/MOV product video (up to 100 MB). On the product page, customers can click image thumbnails and play the video. In Edit Listing, tick media items marked Remove and save to delete them; uploading a new video replaces the current video. The additional media table is created automatically on startup, so the existing Product table does not need a destructive migration. Ensure your hosting plan permits request bodies up to 110 MB and enough disk space; some hosting proxies impose a lower upload limit.
