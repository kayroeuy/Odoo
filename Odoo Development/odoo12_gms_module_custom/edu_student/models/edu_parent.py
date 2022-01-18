from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class EduParent(models.Model):
	_name = 'edu.parent'
	_description = 'EduParent'

	name = fields.Char('ParentID')
	remark = fields.Text('Remark')
	parent_contact_ids = fields.One2many('edu.parent.contact','parent_id', string="Parent Contact")

	@api.constrains('name')
	def _check_name(self):
		parent_rec = self.env['edu.parent'].search(
				[('name', '=', self.name), ('id', '!=', self.id)])
		if parent_rec:
			raise ValidationError(_('Exists ! parentID Already  exists' ) )
