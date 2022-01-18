from odoo import api, fields, models, _
class edu_vaccine(models.Model):
	_name = 'edu.vaccine'
	_description = 'edu_vaccine'

	name = fields.Char('Name')
	inject_date = fields.Date('Inject Date')
	remark = fields.Text('Remark')
	vaccine_id = fields.Many2one('edu.vaccine.type', string='Vaccine Type')

