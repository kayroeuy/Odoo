from odoo import api, fields, models ,_
class EduParentContact(models.Model):
	_name = 'edu.parent.contact'
	_description = 'EduParentContact'

	name = fields.Char('Name', compute='_compute_name')
	firstName = fields.Char('FirstName')
	lastName = fields.Char('LastName')
	relation_ship_type = fields.Selection([('mother', 'Mother'), ('father', 'Father'), ('brother', 'Brother'), ('sister', 'Sister')], string="Relation Ship")
	phone_number = fields.Char('Phone Number')
	email = fields.Char('Email')
	student_id = fields.Many2one('edu.student', string="Student")
	parent_id = fields.Many2one('edu.parent', string="Parent")

	@api.depends('firstName','lastName')
	def _compute_name( self ):
		for rec in self:
			rec.name = '%s %s' % (rec.firstName or '', rec.lastName or '')

