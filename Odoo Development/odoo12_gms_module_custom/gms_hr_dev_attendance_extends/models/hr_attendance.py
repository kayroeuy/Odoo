from odoo import api, fields, models,_

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    total_late = fields.Float('Total Late', compute='get_total_late')
    check_in_hour = fields.Float('Check In Hour')
    check_out_hour = fields.Float('Check Out Hour')

    @api.depends('check_in_hour','check_out_hour')
    def get_total_late(self):
        self.total_late = 0.0
        if self.check_in_hour and self.check_out_hour:
            self.total_late = self.check_in_hour + self.check_out_hour
            print('----------- total ', self.total_late)


