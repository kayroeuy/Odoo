from odoo import api, fields, models ,_
class EduGrade(models.Model):
	_name = 'edu.grade'
	_description = 'EduGrade'

	name = fields.Char('Name')
	remark = fields.Text('Remark')

