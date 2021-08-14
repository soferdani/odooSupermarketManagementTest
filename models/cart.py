from oddo import models, fields, api


class Cart (models.Model):
    _name = 'supermarket.cart'
    _inherit = 'supermarket.customer'
    _description = 'Cart'

    dateOfCreation = fields.Date(context_today='current time')
    totalAmount = fields.Float(compute='_compute_total_amount')

    @api.depends('quantity', "unitPrice")
    def _compute_total_amount(self):
        for record in self:
            total = record.quantity * record.unitPrice
            record.totalAmount = total
