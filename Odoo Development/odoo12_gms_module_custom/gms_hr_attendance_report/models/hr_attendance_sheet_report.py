from odoo import api, fields, models


class AttendanceReport(models.Model):
    _name = 'hr.attendance.sheet.report'
    _description = 'Attendance Report'

    name = fields.Char('Name')
    employee_id = fields.Many2one('hr.employee', 'Employee')
    from_date = fields.Date('From Date')
    to_date = fields.Date('To Date')
    attendance_sheet_ids = fields.One2many('hr.attendance.sheet.report.line', 'attendance_sheet_id',
                                           string="Attendance Line")

    def generate_attendance_sheet(self):
        return {
            'type': 'ir.actions.act_window',
            'views': [(self.env.ref('gms_hr_attendance_report.hr_attendance_generate_sheet_form_view').id, 'form')],
            'view_mode': 'form',
            'res_model': 'hr.attendance.generate.sheet',
            'target': 'new'
        }


class AttendanceReportLine(models.Model):
    _name = 'hr.attendance.sheet.report.line'
    _description = 'Attendance Report'

    date = fields.Date("Date")
    weekdays = fields.Selection([(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (5, 'Friday')],
                                string='Day Of Week')
    planed_signIn = fields.Float('Planed Sign In')
    planed_signOut = fields.Float('Planed Sign Out')
    actual_singIn = fields.Float('Actual Sign In')
    actual_singOut = fields.Float('Actual Sign Out')
    lateIn = fields.Float('Late In')
    overtime = fields.Float('Overtime')
    early_leave = fields.Float('Early Leave')
    attendance_sheet_id = fields.Many2one('hr.attendance.sheet.report', string="Attendance Sheet")
