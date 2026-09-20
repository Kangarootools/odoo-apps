import json
import logging
from markupsafe import Markup
from odoo import models

_logger = logging.getLogger(__name__)

# Common IT / office / electronics brands, longest-first so multi-word names win.
# Extend this list per deployment if needed.
KNOWN_BRANDS = [
    'Western Digital', 'Microsoft', 'Fortinet', 'Logitech', 'Kingston',
    'Hikvision', 'Grandstream', 'Panasonic', 'Schneider', 'Ubiquiti',
    'Huawei', 'Lenovo', 'Xerox', 'Cisco', 'Canon', 'Epson', 'Seagate',
    'Samsung', 'Anker', 'Yealink', 'Aruba', 'Netgear', 'Brother',
    'Philips', 'Toshiba', 'Dell', 'Sony', 'Asus', 'Acer', 'APC', 'HP',
    'LG', '3M',
]


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _seo_add_brand(self, markup_data):
        """Add a schema.org ``brand`` to the product JSON-LD, derived from the
        product name. Non-destructive: parses Odoo's own product_markup_data,
        adds a brand to any Product node that has none, and returns raw Markup.
        Returns the original data unchanged on any error."""
        if not markup_data:
            return markup_data
        try:
            data = json.loads(markup_data)
        except Exception:
            return markup_data

        def brand_from_name(name):
            low = (name or '').lower()
            for brand in KNOWN_BRANDS:
                if brand.lower() in low:
                    return brand
            return None

        def walk(node):
            if isinstance(node, dict):
                if node.get('@type') == 'Product' and not node.get('brand'):
                    brand = brand_from_name(node.get('name'))
                    if brand:
                        node['brand'] = {'@type': 'Brand', 'name': brand}
                for value in node.values():
                    walk(value)
            elif isinstance(node, list):
                for value in node:
                    walk(value)

        try:
            walk(data)
            return Markup(json.dumps(data, ensure_ascii=False))
        except Exception:
            _logger.exception('website_product_brand: failed to add brand to markup')
            return markup_data
