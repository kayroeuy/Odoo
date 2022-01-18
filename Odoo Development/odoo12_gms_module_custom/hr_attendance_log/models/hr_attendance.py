from odoo import api, fields, models, _
from datetime import datetime, timezone, date, time
from time import gmtime, strftime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
import pytz


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    first_check_in = fields.Char(string='CheckIn Time', compute="_compute_check_in_out")
    late = fields.Char('Late', compute='_compute_check_in_out', store=True)
    date = fields.Char('Date', compute='_compute_check_in_out')

    @api.depends('check_in')
    def _compute_check_in_out(self):
        user_tz = self.env.user.tz or pytz.utc
        local = pytz.timezone(user_tz)
        late = ''
        for rec in self:
            date = rec.check_in
            emp_id = rec.employee_id.ids[0]
            attendances = self.env['hr.attendance'].search(
                [('employee_id', '=', emp_id), ('check_in', '>=', date.strftime('%Y-%m-%d 00:00:00')),
                 ('check_in', '<=', date.strftime('%Y-%m-%d 23:23:59'))])
            if attendances:
                attendances.sorted(key=lambda l: l.check_in)

                first_attendance = attendances[-1]
                time_checkin = pytz.utc.localize(first_attendance.check_in).astimezone(local)
                first_attendance.update({'first_check_in': datetime.strftime(time_checkin, "%H:%M")})

                dt1 = datetime.strptime(datetime.strftime(time_checkin, "%Y-%m-%d %H:%M:%S"), '%Y-%m-%d %H:%M:%S')
                dt2 = datetime.strptime(datetime.strftime(time_checkin, "%Y-%m-%d 15:00:00"), '%Y-%m-%d %H:%M:%S')

                if dt2 < dt1:
                    timedelta = dt1 - dt2
                    date_diff_in_seconds = timedelta.days * 24 * 3600 + timedelta.seconds
                    minutes, seconds = divmod(date_diff_in_seconds, 60)
                    hours, minutes = divmod(minutes, 60)
                    days, hours = divmod(hours, 24)
                    late = str(hours) + "h " + str(minutes) + 'm'
                if first_attendance:
                    rec.late = late
                # first_attendance.write({'late': late})
                first_attendance.update({'date': datetime.strftime(time_checkin, "%Y-%m-%d")})
