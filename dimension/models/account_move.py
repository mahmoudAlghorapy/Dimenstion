from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    dimension = fields.Char(string='Dimension')

    # def compute_dimension(self):
    #     for rec in self:
    #         compute = self.env('stock.move').search('sale_line_id', 'in', 'sale_line_ids')
    #         rec.dimension = compute.dimension
