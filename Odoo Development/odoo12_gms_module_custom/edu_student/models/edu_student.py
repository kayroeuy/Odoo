from odoo import api, fields, models, _
from datetime import date
from dateutil.relativedelta import relativedelta
import logging
_logger = logging.getLogger(__name__)
from odoo.exceptions import ValidationError
from lxml import etree


class EduStudent(models.Model):
	_name = 'edu.student'
	_description = 'EduStudent'

	name = fields.Char('Name', compute='_compute_name')
	firstName = fields.Char('FirstName')
	lastName = fields.Char('LastName')
	gender = fields.Selection([('female', 'Female'), ('male', 'Male')], string='Gender')
	dob = fields.Date('Date Of Birth')
	age = fields.Char('Age')
	vaccine_ids = fields.Many2many('edu.vaccine', string='Vaccines')
	parent_id = fields.Many2one('edu.parent', string="Parents")
	parent_contact_ids = fields.One2many('edu.parent.contact', 'student_id', string="Parent Contacts")
	class_name_ids = fields.One2many('edu.class.name','student_id', string="ClassName")

	@api.depends('firstName', 'lastName')
	def _compute_name(self):
		for rec in self:
			rec.name = '%s %s' % (rec.firstName or '', rec.lastName or '')

	@api.onchange('dob')
	def _onchange_dob(self):
		for rec in self:
			if rec.dob:
				dt = date.today()
				rd = relativedelta(dt, rec.dob )
				_logger.info("--------- Year {}".format(rd.years))
				if rd.years > 0:
					rec.age = str(rd.years) + ' years'
				else:
					raise ValidationError("Age must be bigger than 0 !!!!!!!!!!")

	@api.onchange('parent_id')
	def _onchange_parent(self):
		for rec in self:
			rec.parent_contact_ids = rec.parent_id.parent_contact_ids.ids

	def generate_class_name(self):
		return {
				'type': 'ir.actions.act_window',
				'view_mode': 'form',
				'res_model': 'edu.generate.classname',
				'target': 'new',
				}

	@api.model
	def create(self, vals):
		# print("---------- create ", vals)
		return super(EduStudent, self).create(vals)

	def write(self, vals):
		# print("------------ Write", vals)
		return super(EduStudent, self).write(vals)


	def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
		# print('------- view id', view_id)
		# print('------ view type', view_type)
		# print('------ toolbar', toolbar)
		# print('------ submenu', submenu)
		res = super(EduStudent, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
		# print('-------------- res', res)
		if view_type == "form":
			doc = etree.XML(res['arch'])
			name_field = doc.xpath("//field[@name='name']")
			if name_field:
				# Add one label in form view
				name_field[0].addnext(etree.Element('label', {'string': "Hello this custom label from field_view_get_method"}))
				res['arch'] = etree.tostring(doc, encoding='unicode')

			# Set New String to Student Gender
			gender_field = doc.xpath("//field[@name='gender']")
			if gender_field:
				gender_field[0].set("string", "Gender Of Student")
				res['arch'] = etree.tostring(doc, encoding='unicode')
		if view_type == "tree":
			# Add field parent_id after Student Name
			doc = etree.XML(res['arch'])
			parent_field = doc.xpath("//field[@name='name']")
			parent_field[0].addnext(etree.Element('field', {'name': 'parent_id', 'string': 'Parents'}))
			res['arch'] = etree.tostring(doc, encoding='unicode')



		return res




