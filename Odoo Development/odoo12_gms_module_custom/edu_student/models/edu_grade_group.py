from odoo import api, fields, models ,_
class EduGradeGroup(models.Model):
	_name = 'edu.grade.group'
	_description = 'EduGradeGroup'

	name = fields.Char('Name')
	remark = fields.Text('Remark')

