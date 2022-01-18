from odoo import api, fields, models
from datetime import datetime, timedelta, time
import pytz

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    late_check_in = fields.Float('Late', compute='_compute_checkIn_late')
    first_checkin = fields.Datetime(string="Last Check In", compute="get_check_in_time_check_out_time")
    last_check_out = fields.Datetime(string="Last Check Out", compute="get_check_in_time_check_out_time")

    def _compute_checkIn_late(self):
        for rec in self:
            rec.late_check_in = 5.0
            # fmt = '%Y-%m-%d'
            # start_date = emp.first_checkin
            # end_date = emp.last_check_out
            # d1 = datetime.strptime(start_date, fmt).date()
            # d2 = datetime.strptime(end_date, fmt).date()
            # date_difference = d2 - d1
            # print(date_difference)
            # emp.late_check_in = date_difference

    def get_check_in_time_check_out_time(self):
        for rec in self:
            print("------------- Check in", rec.check_in)
            user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz)
            date_today = user_tz.localize(datetime.combine(datetime.today(), time(0, 0, 0)), is_dst=None).astimezone(pytz.utc).replace(tzinfo=None)
            print("------------- date_today", date_today)

            attendance_check_in_time = self.env['hr.attendance'].search([('check_in', '>=', '2021-12-04 08:00:00'), ('check_in', '<=', '2022-01-04 12:00:00')])
            min_time = time(11, 59, 59)
            max_time = time(12, 0, 0)

            print("------------- attendance_check_in_time", attendance_check_in_time)
            for a in attendance_check_in_time:
                min_date = user_tz.localize(datetime.combine(a.check_in, min_time)).astimezone(pytz.utc).replace(tzinfo=None)
                max_date = user_tz.localize(datetime.combine(a.check_in, max_time)).astimezone(pytz.utc).replace(tzinfo=None)
                rec.first_checkin = min_date
                rec.last_check_out = max_date
                print("------------- min_date", rec.first_checkin)
                print("------------- max_date", rec.last_check_out)
