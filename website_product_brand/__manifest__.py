{
    'name': 'Website Product Brand Schema',
    'version': '19.0.1.0.0',
    'summary': 'Adds schema.org brand to product JSON-LD, derived from the product name (any company)',
    'description': 'Generic, reusable add-on for Odoo Website/eCommerce. Non-destructively '
                   'post-processes each product page JSON-LD (product_markup_data) to add a '
                   'schema.org brand derived from the product name, using a configurable list '
                   'of common brands. Helps Google rich results and AI answer engines identify '
                   'the brand. Fully defensive: returns the original markup unchanged on any '
                   'error. No hardcoded company data — works for any store.',
    'author': 'Kangaroo Tools',
    'website': 'https://www.kangarootools.com',
    'category': 'Website/eCommerce',
    'depends': ['website_sale'],
    'data': ['views/product_markup_inherit.xml'],
    'images': ['static/description/icon.png'],
    'support': 'info@kangarootools.com',
    'price': 39.00,
    'currency': 'USD',
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'OPL-1',
}
