from odoo import api, fields, models ,_
import logging
_logger = logging.getLogger(__name__)
from odoo.exceptions import ValidationError

class EduGenerateClassName(models.TransientModel):
	_name = 'edu.generate.classname'
	_description = 'Generate ClassName'

	grade_ids = fields.Many2many('edu.grade', string='Grades')
	grade_group_ids = fields.Many2many('edu.grade.group', string="Grade Group")
	class_type_id = fields.Many2one('edu.class.type', string="Class Type")

	def button_generate_classname( self ):
		className = ''
		vals = []
		for rec in self:
			student_obj = self.env['edu.student'].browse(self.env.context.get('active_id'))
			_logger.info("----------- student {}".format(student_obj))
			for grade in rec.grade_ids:
				for group in rec.grade_group_ids:
					for classType in rec.class_type_id:
						className = '%s %s %s' %(grade.name, group.name, classType.name)
						check_exist_class = student_obj.class_name_ids.filtered(lambda l: l.name == className)
						if check_exist_class:
							raise ValidationError('ClassName Already Exist!!!')
						else:
							vals.append((0, 0, {
									'name': className,
									}))

			student_obj.write({'class_name_ids': vals})
