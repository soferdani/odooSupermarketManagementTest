from models.productCategory import ProductCategory
from oddo import models, fields


class Product (models.Model):
    _name = 'supermarket.product'
    _inherit = 'supermarket.productCategory'
    _description = 'Product'

    unitPrice = fields.Float('Unit Price', required=True,
                             related='supermarket.cart', store=True)
    productName = fields.Char('Product Name', required=True)
