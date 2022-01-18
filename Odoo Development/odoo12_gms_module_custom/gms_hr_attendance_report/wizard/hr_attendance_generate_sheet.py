import pytz
from datetime import datetime, timedelta, time, date
from odoo import api, fields, models


class AttendanceGenerateSheet(models.TransientModel):
    _name = 'hr.attendance.generate.sheet'
    _description = 'Attendance Generate Sheet'

    employee_id = fields.Many2one('hr.employee', 'Employee')
    from_date = fields.Date('From Date')
    to_date = fields.Date('To Date')

    def daterange(self, start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    def saved_generate_sheet(self):
        for rec in self:
            employee_calendar_attendances, check_working_hour_of_employee, vals = [], [], []
            user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz)
            print('-------- context ', self.env.context)
            current_attendance_sheet = self.env['hr.attendance.sheet.report'].browse(self.env.context.get('active_id'))
            print('---------- curr', current_attendance_sheet)
            sheet_name = '%s %s %s %s %s %s' % (
                'Attendance Sheet Of', rec.employee_id.name, 'from', rec.from_date, 'to', rec.to_date)
            current_attendance_sheet.write({
                'name': sheet_name,
                'employee_id': rec.employee_id.id,
                'from_date': rec.from_date,
                'to_date': rec.to_date
            })
            if self.from_date or self.to_date:
                from_date = user_tz.localize(datetime.combine(self.from_date, time(0, 0, 0)), is_dst=None).astimezone(
                    pytz.utc).replace(tzinfo=None)
                to_date = user_tz.localize(datetime.combine(self.to_date, time(23, 59, 59)), is_dst=None).astimezone(
                    pytz.utc).replace(tzinfo=None)
                attendance_obj = self.env['hr.attendance'].search(
                    [('employee_id', '=', self.employee_id.id), ('check_in', '>=', from_date),
                     ('check_in', '<=', to_date), ])
                if self.employee_id.resource_calendar_id:
                    employee_calendar_attendances = self.employee_id.resource_calendar_id.attendance_ids
                else:
                    employee_calendar_attendances = self.employee_id.company_id.resource_calendar_id.attendance_ids

                for date in self.daterange(self.from_date, self.to_date):
                    check_working_hour_of_employee = employee_calendar_attendances.filtered(
                        lambda l: l.dayofweek == str(date.weekday()))
                    if check_working_hour_of_employee:
                        print('----------- check_working_hour_of_employee', check_working_hour_of_employee)
                        for hour in check_working_hour_of_employee:
                            print('---------  hour.hour_to', hour.hour_to)
                            print('---------  hour.dayofweek ', type(hour.dayofweek))
                            print('---------  date', date.strftime('%m/%d/%Y'))
                            vals.append((0, 0, ({
                                'date': date.strftime('%m/%d/%Y'),
                                'planed_signIn': hour.hour_from,
                                'planed_signOut': hour.hour_to
                            })))
                current_attendance_sheet.write({'attendance_sheet_ids': vals})
        pass
