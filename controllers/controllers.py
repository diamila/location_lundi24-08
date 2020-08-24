# -*- coding: utf-8 -*-
from odoo import http

# class LocationBiens(http.Controller):
#     @http.route('/location_biens/location_biens/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/location_biens/location_biens/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('location_biens.listing', {
#             'root': '/location_biens/location_biens',
#             'objects': http.request.env['location_biens.location_biens'].search([]),
#         })

#     @http.route('/location_biens/location_biens/objects/<model("location_biens.location_biens"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('location_biens.object', {
#             'object': obj
#         })