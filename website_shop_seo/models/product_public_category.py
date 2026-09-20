import logging
from odoo import api, models

_logger = logging.getLogger(__name__)


class ProductPublicCategory(models.Model):
    _inherit = 'product.public.category'

    def _seo_company_bits(self):
        """Return (store_name, location_suffix) taken from the company, so the
        generated copy is correct for ANY company/country (no hardcoding)."""
        store = 'our store'
        loc = ''
        try:
            company = self.env.company
            store = company.name or store
            country = company.country_id.name or ''
            if country:
                loc = ' in %s' % country
        except Exception:
            pass
        return store, loc

    def _seo_autofill(self):
        """Fill category meta title/description + intro text from the category
        name, only where empty. Keeps new categories SEO-ready automatically."""
        store, loc = self._seo_company_bits()
        for cat in self:
            name = (cat.name or '').strip()
            if not name:
                continue
            vals = {}
            if not cat.website_meta_title:
                vals['website_meta_title'] = ('%s%s | %s' % (name, loc, store))[:70]
            if not cat.website_meta_description:
                vals['website_meta_description'] = (
                    'Buy %s%s from %s — genuine products, competitive pricing, warranty '
                    'and reliable support.' % (name, loc, store))[:300]
            if not cat.website_description:
                vals['website_description'] = (
                    '<p>Explore our range of %s%s. %s supplies genuine %s with competitive '
                    'pricing, warranty and reliable support.</p>' % (name, loc, store, name))
                vals['show_category_description'] = True
            if vals:
                cat.write(vals)

    @api.model_create_multi
    def create(self, vals_list):
        categories = super().create(vals_list)
        try:
            categories._seo_autofill()
        except Exception:
            _logger.exception('website_shop_seo: category SEO autofill failed')
        return categories
