from odoo import api, fields, models, _
from datetime import datetime, timezone
from time import gmtime, strftime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
import pytz


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    first_check_in = fields.Char('First Check In', compute='_compute_check_in_out')
    last_check_out = fields.Char('Last Check Out', compute='_compute_check_in_out')
    late_hour = fields.Char('Late Hour', compute='_compute_check_in_out')

    @api.depends('check_in')
    def _compute_check_in_out(self):
        for rec in self:

            # for rec in self:
            local_tz = pytz.timezone(self.env.user.tz)
            dt = datetime.now()
            today = local_tz.localize(dt, is_dst=None).astimezone(pytz.utc).replace(tzinfo=None)
            print("------------- today", today)
            emp = self.env['hr.employee'].search([('user_id', '=', self.env.user.id)])
            attendances = self.env['hr.attendance'].search([('check_in', '<=', today.strftime('%Y-%m-%d 23:59:59')),
                                                            ('check_in', '>=', today.strftime('%Y-%m-%d 00:00:00'))])
            if attendances:
                test = attendances.sorted(key=lambda l: l.check_in)
                print("---------- test[0].check_in", test[0].check_in)
                dt_check_in = local_tz.localize(test[0].check_in, is_dst=None).astimezone(pytz.utc).replace(tzinfo=None)
                dt_last_check_out = local_tz.localize(test[-1].check_in, is_dst=None).astimezone(pytz.utc).replace(tzinfo=None)
                print('------------ test2', dt_last_check_out)
                check_current_user = attendances.filtered(
                    lambda l: l.employee_id.id == emp.id and l.check_in == test[-1].check_in)
                if check_current_user:
                    print('---------- check_current_user', check_current_user)
                    first_check_in = dt_check_in.strftime("%H:%M")
                    print("-------------- first check in", dt_check_in)
                    print("-------------- dt_last_check_out", dt_last_check_out)
                    last_check_out = dt_last_check_out.strftime("%H:%M")
                    FMT = '%H:%M'
                    late_hour = datetime.strptime(last_check_out, FMT) - datetime.strptime(first_check_in, FMT)
                    check_current_user.update({'late_hour': late_hour, 'last_check_out': "%s %s" % (last_check_out, 'AM'),
                                               'first_check_in': "%s %s" % (first_check_in, 'AM')})
