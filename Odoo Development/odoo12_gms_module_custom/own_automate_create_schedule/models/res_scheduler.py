from odoo import api, fields, models

class ScheduleDemo(models.Model):
    _name = 'schedule.demo'
    _description = 'Schedule Demo'

    employee_id = fields.Many2one('hr.employee', 'Employee')


class scheduler_demo(models.Model):
    _inherit = 'hr.employee'


    # This function is called when the scheduler goes off
    @api.multi
    def process_demo_scheduler_queue(self):
        schedule_obj = self.env['schedule.demo'].search([])
        emp_obj = self.env['hr.employee'].search([])
        for rec in emp_obj:
            print("----------- rec", rec.id)
            is_has_emp_schedule = schedule_obj.filtered(lambda l: l.employee_id.id == rec.id)
            if not is_has_emp_schedule:
                print("----------- not is_has_emp_schedule ", schedule_obj)
                schedule_obj.create({
                    'employee_id': rec.id
                })
        print("----------- heloo", schedule_obj)