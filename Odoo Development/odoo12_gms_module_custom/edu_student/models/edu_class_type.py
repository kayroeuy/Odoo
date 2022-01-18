from odoo import api, fields, models ,_
class EduClassType(models.Model):
	_name = 'edu.class.type'
	_description = 'EduClassType'

	name = fields.Char('Name')
	remark = fields.Text('Remark')

