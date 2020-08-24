# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.tools import float_compare, pycompat
from odoo.exceptions import ValidationError
from odoo.osv import expression

from odoo.addons import decimal_precision as dp



class Locataire_potenciel(models.Model):
    _inherit = 'res.partner'

    quartier_souhaitee = fields.Many2one('lb.quartier', string="Quartier souhaité")
    budget = fields.Float(string="Budget", default=0.0, digits=dp.get_precision('Budget'))
    #type_id = fields.Many2one('lb.type', string="Type Biens souhaitee")
    active_potenctiel = fields.Boolean('Peut étre un locataire potenciel', default=False)

    reclamation = fields.One2many('lb.reclamation', 'reclamation_id',
                                             string="Fiche de réclamation", required=True)

    origine_prospect = fields.Selection(
        [('pub_journal', 'Pub journal'), ('site_web', 'Site web CPI'), ('linkedIn', 'LinkedIn'),
         ('facebook', 'Facebook'), ('agent_cpi', 'Agent CPI'), ('eecommandé', 'Recommandé')],
        string="ORIGINE DU PROSPECT")

    user_id = fields.Many2one('res.users', string='Agent-Guide', track_visibility='onchange',
                              default=lambda self: self.env.user)

    # user_id = fields.Many2one('res.users', string='Agent-cpi')



class reclamation(models.Model):
    _name = 'lb.reclamation'

    reclamation_id = fields.Many2one('res.partner', ondelete='cascade', string="Réclamation")
    type_reclamation = fields.Selection(
        [('reparataion', 'demande de réparation'), ('payement', 'payement'),
         ('voisin', 'Vie locative'),('amenagement', 'autorisatio de faire des travaux'),('resiliation', 'Résiliation du bail et Sortie')], string="Type Réclamation")
    date_reclamation = fields.Date('Date Réclamation')

    resume_reclamation = fields.Char(string="Résumé")
    notes = fields.Html('Description', sanitize_style=True)
    fichier = fields.Binary(string="fichier", attachment=True)

    @api.multi
    def action_close_dialog(self):
        return {'type': 'ir.actions.act_window_close'}

    @api.multi
    def action_done(self):
        """ Wrapper without feedback because web button add context as
        parameter, therefore setting context to feedback """
        return self.action_feedback()

    def action_feedback(self, feedback=False):
        message = self.env['mail.message']
        if feedback:
            self.write(dict(feedback=feedback))



