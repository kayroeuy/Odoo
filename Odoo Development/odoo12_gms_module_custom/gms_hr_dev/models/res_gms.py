from odoo import api, fields, models,_

class ResGms(models.Model):
    _name = 'res.gms'
    _description = 'Res Gms'

    name = fields.Char(string='Name')
    cmp_address = fields.Text(string="Company Address")




