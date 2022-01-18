from odoo import api, fields, models, _


class ResGMS(models.Model):
    _inherit = 'res.gms'

    phone = fields.Char('Phone Number')
    email = fields.Char('Email')
    street = fields.Text('Company Street')
    is_check = fields.Boolean('Is Check')

    @api.onchange('name', 'cmp_address')
    def _onchange_company_street(self):
        print('-------- name', self.name)
        print('-------- cmp address', self.cmp_address)
        self.street = "%s %s" %(self.name or '', self.cmp_address or '')
