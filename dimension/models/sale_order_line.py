from odoo import models, fields, api


class SalOrderLine(models.Model):
    _inherit = 'sale.order.line'

    dimension = fields.Char(string='Dimension')

    def _prepare_procurement_values(self, group_id=False):
        values = super(SalOrderLine, self)._prepare_procurement_values(group_id)
        values['dimension'] = self.dimension
        return values

    def _prepare_invoice_values(self, order, name, amount, so_line):
        values = super(SalOrderLine, self)._prepare_invoice_values(order, name, amount, so_line)
        values.update({'dimension': self.dimension})
        print('res# ', values)
        return values
