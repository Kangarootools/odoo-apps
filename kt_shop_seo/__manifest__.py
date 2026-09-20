{
    'name': 'Website Shop SEO Pack',
    'version': '19.0.1.0.0',
    'summary': 'Auto category SEO (meta + intro) and CollectionPage/ItemList schema for any Odoo eCommerce site',
    'description': 'Generic, reusable SEO booster for Odoo Website/eCommerce:\n'
                   '  * Auto-generates category meta title, meta description and intro text '
                   'from the category name (using the company name and country dynamically), '
                   'only where the user has not set them.\n'
                   '  * Adds schema.org CollectionPage + ItemList JSON-LD to shop and category '
                   'listing pages, built from the products on the page.\n'
                   'Fully defensive: any error is logged, never raised, so pages never break. '
                   'Works for any company — no hardcoded brand or country.',
    'author': 'Kangaroo Tools',
    'website': 'https://www.kangarootools.com',
    'category': 'Website/eCommerce',
    'depends': ['website_sale'],
    'data': ['views/shop_schema.xml'],
    'images': ['static/description/icon.png'],
    'support': 'info@kangarootools.com',
    'price': 59.00,
    'currency': 'USD',
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'OPL-1',
}
