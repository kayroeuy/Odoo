from odoo import api, fields, models,_
class EduVaccineType(models.Model):
	_name = 'edu.vaccine.type'
	_description = 'EduVaccineType'

	name = fields.Char('Name')
	remark = fields.Text('Remark')

