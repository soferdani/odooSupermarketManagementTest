from oddo import models, fields


class ProductCategory (models.Model):
    _name = 'supermarket.ProductCategory'
    _description = 'ProductCategory'

    categoryName = fields.Char('Category Name')
