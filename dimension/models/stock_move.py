from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = 'stock.move'
    dimension = fields.Char(string='Dimension')

    def _get_invoice_line_vals(self, line, taxes_vals):
        ret = super(StockMove, self)._get_invoice_line_vals(line, taxes_vals)
        if taxes_vals.date_expected:
            ret['dimension'] = line.date_expected
        return ret


class StockRuleInherit(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id,
                               values):
        res = super(StockRuleInherit, self)._get_stock_move_values(product_id, product_qty, product_uom, location_id,
                                                                   name, origin, company_id, values)
        res['dimension'] = values.get('dimension', False)
        return res
