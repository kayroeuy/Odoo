from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # name_search()
    # @api.model
    # def name_search(self, name, args=None, operator='ilike', limit=100):
    #     args = args or []
    #     print('------- name', name)
    #     print('------- args', args)
    #     print('------- operator', operator)
    #     print('------- limit', limit)
    #     if name:
    #         records = self.search(
    #             ['|', '|', ('name', operator, name), ('phone', operator, name), ('email', operator, name)])
    #         return records.name_get()
    #     return super(ResPartner, self).name_search(name=name, args=args, operator=operator, limit=limit)

    # _name_search()
    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):

        args = args or []
        domain = []
        print('------- name', name)
        print('------- args', args)
        print('------- operator', operator)
        print('------- limit', limit)
        print('------- name_get_uid', name_get_uid)
        if name:
            domain = ['|', '|', ('name', operator, name), ('phone', operator, name), ('email', operator, name)]
        partner_ids = self.search(domain)
        return partner_ids.name_get()
