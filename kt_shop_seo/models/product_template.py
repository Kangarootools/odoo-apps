import json
import logging
from markupsafe import Markup
from odoo import models

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _seo_collection_markup(self, products, category=None):
        """Build schema.org CollectionPage + ItemList JSON-LD for a shop/category
        listing page, from the products shown on the page. Defensive: returns ''
        on any error so a listing page is never broken by this add-on."""
        try:
            try:
                base = self.env['website'].get_current_website().get_base_url().rstrip('/')
            except Exception:
                base = ''
            items = []
            pos = 0
            for p in products:
                try:
                    url = p.website_url or ''
                except Exception:
                    url = ''
                if not url:
                    continue
                pos += 1
                items.append({
                    '@type': 'ListItem',
                    'position': pos,
                    'url': (base + url) if base else url,
                    'name': p.name,
                })
            if not items:
                return ''
            name = 'Shop'
            try:
                if category and category.name:
                    name = category.name
            except Exception:
                pass
            data = {
                '@context': 'https://schema.org',
                '@type': 'CollectionPage',
                'name': name,
                'mainEntity': {
                    '@type': 'ItemList',
                    'numberOfItems': len(items),
                    'itemListElement': items,
                },
            }
            return Markup(json.dumps(data, ensure_ascii=False))
        except Exception:
            _logger.exception('website_shop_seo: failed to build collection markup')
            return ''
