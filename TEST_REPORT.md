# Verification Report — 2026-10-28

## Checks actually executed

- `python -m compileall -q app config.py run.py init_db.py create_admin.py` — **PASS** (Python source compiled without syntax errors).
- SQLite `ALTER TABLE ... ADD COLUMN state_province ...` migration statement — **PASS** in an isolated SQLite check.
- ZIP archive integrity — **PASS** (`unzip -t` on the delivered archive).
- Required project files, sample SVG assets, templates, tests, and setup scripts — **PASS** (file-presence inspection).
- Persistent WhatsApp support link added to the shared storefront layout and a regression test added for storefront pages.

## Checks not completed

- Pytest suite — **BLOCKED, not passed**. Test collection fails because Flask is not installed in the provided build environment (`ModuleNotFoundError: No module named 'flask'`). Installing dependencies was not possible in this environment because package network/DNS access is unavailable.
- Fresh-install end-to-end browser run — **NOT VERIFIED**.
- Real WhatsApp Cloud API delivery, live card payments, email notifications, shipping carrier APIs, and production deployment — **NOT CONFIGURED / NOT VERIFIED**.

## Before using with real customers

1. Install the dependencies from `requirements.txt` in a clean Python 3.11 or 3.12 virtual environment.
2. Run `python -m pytest -q` and fix any failures on that machine.
3. Configure a strong secret, business-owned WhatsApp number, correct bank-transfer instructions, real product data, shipping charges and policies.
4. Test a complete sample order, payment-evidence review, stock changes, and WhatsApp click-to-chat on desktop and mobile.
5. Do not claim payment has been received until it is verified independently in the business bank account.

This report intentionally distinguishes source/static checks from tests that could not be executed. No claim of zero defects or fully production-tested operation is made.


## Private listings update (28 October 2026)
- Added explicit private-draft default for new product listings.
- Added admin-only Publish/Unpublish action and visibility status in product inventory.
- Draft product detail URLs return 404 to public visitors and drafts are excluded from storefront queries.
- Added tests for draft privacy and publish transition.
- Python source compilation verified after this update. Full pytest execution remains blocked in this environment because Flask is not installed (`ModuleNotFoundError: No module named 'flask'`); therefore these new tests are written but not claimed as passed.
