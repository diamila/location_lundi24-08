# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.tools import float_compare, pycompat
from odoo.exceptions import ValidationError
from odoo.osv import expression

from odoo.addons import decimal_precision as dp


class Bailleur(models.Model):
    _name = 'lb.bailleur'
    _rec_name = 'nom'

	        # Get default country
    @api.model
    def _get_default_country(self):
        country = self.env['res.country'].search([('code', '=', 'MA')], limit=1)
        return country

    image = fields.Binary(string="Image", attachment=True)

    nom = fields.Char(string="Nom", required=True)
    civilite = fields.Selection([('m.', 'M.'),('mme', 'Mme'),('mlle', 'Mlle'),('m. et mme','M. et Mme')], string="Civilité")
    email = fields.Char(string="E-mail", required=True)
    telephone = fields.Char(string="Téléphone", required=True)
    mobile = fields.Char(string="Téléphone", required=True)
    street = fields.Char(string="Adresse1")
    street2 = fields.Char(string="Adresse1")
    code_postale = fields.Char(string="Code Postal")
    ville = fields.Char(string="Ville")
    pays_id = fields.Many2one('res.country', string='Pays', default=_get_default_country, ondelete='restrict')
    poste_occupe = fields.Char(string="Poste occupé", help="Activité professionelle du propriétaire")
    website = fields.Char()

    type_piece_identite = fields.Selection([('cni', 'Carte national d\'identité'), ('carte_sejour', 'Carte de séjour'), ('passport', 'Passport')],
        string='Type de la pièce d\'identité')
    num_piece_identite = fields.Char(string='Numéro de la pièce d\'identité')
    enregistrement_contact = fields.One2many('lb.contact_bailleur', 'contact_id', string="Contact")

    bien_count = fields.Integer(string='Biens', compute='get_bien_count')

    @api.multi
    def open_bailleur_bien(self):
        return {
            'name': _('Biens'),
            'domain': [('bailleur_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'product.template',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def get_bien_count(self):
        count = self.env['product.template'].search_count([('bailleur_id', '=', self.id)])
        self.bien_count = count


class Contact(models.Model):
    _name = 'lb.contact_bailleur'

    contact_id = fields.Many2one('res.partner', ondelete='cascade', string="Contact")
    nom_contact = fields.Char(string="Nom du Contact", required=True)
    telephone_contact = fields.Char(string="Téléphone", required=True)
    email_contact = fields.Char(string="E-mail")
    notes_contact = fields.Text(string="Notes")
