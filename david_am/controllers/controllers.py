# -*- coding: utf-8 -*-
# from odoo import http


# class DavidAm(http.Controller):
#     @http.route('/david_am/david_am', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/david_am/david_am/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('david_am.listing', {
#             'root': '/david_am/david_am',
#             'objects': http.request.env['david_am.david_am'].search([]),
#         })

#     @http.route('/david_am/david_am/objects/<model("david_am.david_am"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('david_am.object', {
#             'object': obj
#         })
