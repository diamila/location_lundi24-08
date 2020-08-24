from odoo import models, fields, api, tools, exceptions, _
from datetime import datetime, timedelta

# Heritage Vente/Quittance
class Quittance(models.Model):
    _inherit = 'sale.order'  #

    #bailleur_id = fields.Many2one(related='bien_loue.bailleur_id', ondelete='cascade', string="Bailleur")


    #bien_loue = fields.Many2many('product.template', ondelete='cascade', string="Bien Loué", required=True)
    #bailleur_id = fields.Many2one(related='bien_loue.bailleur_id', ondelete='cascade', string="Bailleur")

    #list_price = fields.Float(related='bien_loue.list_price', ondelete='cascade', string="montant")
    #total = fields.Float(related='bien_loue.list_price', ondelete='cascade', string="Total")

    #periode_debut = fields.Date(string="Période Payée Début")
    #periode_fin = fields.Date(string="Période Payée Fin")

class order_line(models.Model):
    _inherit = 'sale.order.line'

    #periode_fin =  fields.Date(string='Date payement',default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    mois_payee_c = fields.Selection([('janvier', 'janvier'),
                                   ('fevrier', 'février'),
                                   ('mars', 'mars'),
                                   ('avril', 'avril'),
                                   ('mai', 'mai'),
                                   ('juin', 'juin'),
                                   ('juillet', 'juillet'),
                                   ('aout', 'août'),
                                   ('septembre', 'septembre'),
                                   ('octobre', 'octobre'),
                                   ('novembre', 'novembre'),
                                   ('decembre', 'décembre')],
                                  string="paiement du mois", required=True)



#heritage pour la facture
class facture(models.Model):
    _inherit = 'account.invoice'

    #mois = fields.Char(string="paiement du mois", required=True)
    #nom = fields.Char(string="Nom du Bien")

    mois_payee = fields.Selection([('janvier', 'janvier'),
                                   ('fevrier', 'février'),
                                    ('mars', 'mars'),
                                   ('mai', 'mai'),
                                   ('avril', 'avril'),
                                   ('mai', 'mai'),
                                   ('juin', 'juin'),
                                   ('juillet', 'juillet'),
                                   ('aout', 'août'),
                                   ('septembre', 'septembre'),
                                   ('octobre', 'octobre'),
                                   ('novembre', 'novembre'),
                                   ('decembre', 'décembre')],
                                  string="paiement du mois")




    objet_payement = fields.Selection([('avance', 'Avance'), ('loyer', 'Loyer du mois'), ('pénalité', 'Pénalités'),
                                       ('autre paiements', 'Autres Paiements')], string="Objet du Paiement")


class order(models.Model):
    _inherit = 'account.invoice.line'

    date_payement =  fields.Date(string='Date payement', required=True,default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))



#heritage pour la facture
class facture_suite(models.Model):
    _inherit = 'account.invoice'

    objet = fields.Selection([('avance', 'Avance'), ('loyer', 'Loyer du mois'), ('pénalité', 'Pénalités'),
                                       ('autre paiements', 'Autres Paiements')], string="Objet du Paiement", required=True)






