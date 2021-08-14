from oddo import models, fields


class CartItem (models.Model):
    _name = 'supermarket.cartItem'
    _inherits = {
        'supermarket.cart': 'cart',
        'supermarket.product': 'product',
    }
    _description = 'CartItem'

    cart = fields.Many2one('supermarket.cart')
    product = fields.Many2one('supermarket.product')
    quantity = fields.Float('Quantity')
