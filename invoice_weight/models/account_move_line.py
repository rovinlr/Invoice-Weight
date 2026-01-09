from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    peso_neto = fields.Float(string="Peso neto")
    peso_total = fields.Float(string="Peso total")
