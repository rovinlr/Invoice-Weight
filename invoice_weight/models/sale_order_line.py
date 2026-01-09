from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    peso_neto = fields.Float(string="Peso neto")
    peso_total = fields.Float(string="Peso total")
