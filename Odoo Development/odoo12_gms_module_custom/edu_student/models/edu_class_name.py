from odoo.exceptions import ValidationError
from odoo import api, fields, models ,_
class EduClassName(models.Model):
	_name = 'edu.class.name'
	_description = 'EduClassName'

	name = fields.Char('ClassName')
	student_id = fields.Many2one('edu.student',string="Student")
	remark = fields.Text('Remark')
	

