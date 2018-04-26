# -*- coding: utf-8 -*-
from odoo import http
from odoo import models, fields, api
from odoo.http import request

# class Academy(http.Controller):
#     @http.route('/academy/academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/academy/academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy.listing', {
#             'root': '/academy/academy',
#             'objects': http.request.env['academy.academy'].search([]),
#         })

#     @http.route('/academy/academy/objects/<model("academy.academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy.object', {
#             'object': obj
#         })


class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        print 'method calllllllllll'
        users = http.request.env['res.users'].search([])
        return http.request.render('academy.index', {'users': users})

    @http.route(['/user/created/'], auth="public", website=True)
    def user_creatd(self, **kw):
        if kw.get('name') and kw.get('login'):
            users = http.request.env['res.users'].sudo().create({'name':kw.get('name'),'login':kw.get('login'),'email':kw.get('login'),'boolian':kw.get('boolian')})
        conf = http.request.env['base.config.settings'].search([])
        print conf.auth_signup_template_user_id,"**template render***"
        return http.request.render('website_crm.contactus_thanks')


    
