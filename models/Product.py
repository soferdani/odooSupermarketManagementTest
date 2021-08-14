from models.ProductCategory import ProductCategory
from oddo import models, fields


class Product (models.Model):
    _name = 'supermarket.Product'
    _inherit = 'supermarket.ProductCategory'
    _description = 'Product'

    unitPrice = fields.Float('Unit Price')
    productName = fields.Char('Product Name')
