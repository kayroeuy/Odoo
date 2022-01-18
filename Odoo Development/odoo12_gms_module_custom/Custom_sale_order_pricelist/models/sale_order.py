from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_check = fields.Boolean('Is Check', compute='_compute_is_check')

    @api.depends('order_line.product_id', 'pricelist_id')
    def _compute_is_check(self):
        is_product_pricelist = []
        is_product_line = []
        for rec in self:
            pricelist_items = self.env['product.pricelist.item'].search([('pricelist_id', '=', rec.pricelist_id.id)])
            for line in rec.order_line:
                if line.product_id.product_tmpl_id.id in pricelist_items.mapped('product_tmpl_id').ids:
                    is_product_pricelist.append(line.product_id.id)
                else:
                    is_product_line.append(line.product_id.id)
            if is_product_pricelist and not is_product_line:
                print('--------- check tru')
                rec.is_check = True
            else:
                print('---------- check false')
                rec.is_check = False
            print('------is_product_pricelist ', is_product_pricelist)
            print('------ is_product_line ', is_product_line)