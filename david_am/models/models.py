# -*- coding: utf-8 -*-

from odoo import models, fields

class david_am(models.Model):
    _name = 'david_am.test'
    _description = 'david_am.test'

    name = fields.Char()
    fecha = fields.Date() 
    description = fields.Char()

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
