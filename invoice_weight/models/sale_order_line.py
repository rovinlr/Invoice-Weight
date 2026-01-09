from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    peso_neto = fields.Float(string="Peso neto")
    peso_total = fields.Float(string="Peso total")

    def _prepare_invoice_line(self, **optional_values):
        res = super()._prepare_invoice_line(**optional_values)
        res.update(
            {
                "peso_neto": self.peso_neto,
                "peso_total": self.peso_total,
            }
        )
        return res
