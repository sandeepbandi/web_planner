# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Teachers(models.Model):
    _name = 'academy.teachers'

    name = fields.Char()
    login = fields.Char()
    email=fields.Char()

    def sample_def(self):
    	print "**********&***"

class Users(models.Model):
	_inherit ="res.users"

	boolian = fields.Boolean('HRMS')

	@api.model
	def create(self, vals):
		user = super(Users, self).create(vals)
		user.partner_id.active = user.active
		if user.partner_id.company_id:
			user.partner_id.write({'company_id': user.company_id.id})
		return user