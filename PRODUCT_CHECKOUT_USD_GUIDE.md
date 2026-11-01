# Product-page Checkout + USD Setup Guide

## What customers see

1. Open **Shop all** and choose a product.
2. The product detail page shows the product title, SKU, price, stock availability, description and quantity selector.
3. **Add to bag** adds the selected quantity to the shopping bag and returns to the previous page.
4. **Buy now — Checkout** sends the selected product and quantity directly to checkout. It intentionally replaces the existing bag contents for this direct-purchase flow so the customer does not accidentally order other products.
5. Checkout displays the item summary, subtotal, configured shipping charge and total in USD.
6. The customer completes contact and delivery fields, including optional State / Province, then places the order.
7. The order is saved as awaiting payment. The site does not take card payments or mark the order paid. The administrator must independently verify the bank transfer.

## USD consistency

- The store banner says that all prices are in USD ($).
- Product prices, bag, checkout, order confirmation and admin totals use `$` formatting.
- New orders store `currency='USD'`.
- Currency is no longer editable in Admin > Settings, preventing accidental mixed-currency order totals.
- Set `STORE_CURRENCY=USD` in `.env` for clarity; order calculations are hard-coded to USD in this version.

## Important before launch

- Sample product data, prices, stock and images are development examples. Replace them with real authorized product information.
- Configure your real bank details in Admin > Settings before accepting bank transfers. No bank details are prefilled.
- This build uses manual bank transfer only. Card gateway, automatic WhatsApp Cloud API notifications, email delivery, carrier integrations and production deployment are not live.
- Use HTTPS, a strong secret key, production database, backups, monitoring and a production WSGI server before public launch.

## Verification notes for this package

- Python source compilation (`compileall`) was checked after the update.
- The included pytest suite covers product page checkout visibility, USD display, direct-buy routing, cart/order totals, stock validation and access controls.
- The test suite could not be executed in the packaging environment because Flask dependencies were not installed and outbound package download failed due to DNS/network unavailability. Run `python -m pytest -q` after `start_windows.bat` has installed dependencies on your Windows computer.
