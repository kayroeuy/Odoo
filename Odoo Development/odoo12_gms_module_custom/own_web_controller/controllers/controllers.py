# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request


class MyController(http.Controller):
    @http.route('/helloworld', website=True, auth='public')
    def hello(self, **kw):
        # return "HelloWorld"
        # Call template ID (/views/template.xml)
        customers = request.env['res.partner'].sudo().search([])
        return request.render("own_web_controller.controller_template", {
            'partners': customers
        })
