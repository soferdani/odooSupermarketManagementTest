from oddo import models, fields


class Cart (models.Model):
    _name = 'supermarket.cart'
    _inherit = 'supermarket.customer'
    _description = 'Cart'

    dateOfCreation = fields.Date(context_today='current time')
