

# -*- coding: utf-8 -*-

from odoo import models, fields


class CreateAppointment(models.TransientModel):
    _name = 'create.contrat'


    locataires = fields.Many2one('res.partner', ondelete='cascade', string="Locataire")

    date_debut = fields.Date(string="Date Début")
    date_expiration = fields.Date(string="Date D'expiration")



    def create_contrat(self):
        vals = {
            'locataires': self.locataires.id,
            'date_debut': self.date_debut,
            'date_expiration': self.date_expiration,
        }
        self.env['lb.location'].create(vals)


