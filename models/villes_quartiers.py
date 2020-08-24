# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.tools import float_compare, pycompat
from odoo.exceptions import ValidationError
from odoo.osv import expression



class Ville(models.Model):
    _name = 'lb.ville'
    _rec_name = 'nom'

    nom = fields.Char(string="Ville")


class Quartier(models.Model):
    _name = 'lb.quartier'
    _rec_name = 'nom_quartier'

    nom_quartier = fields.Char(string="Quartier")
    ville_associée = fields.Many2one('lb.ville')

