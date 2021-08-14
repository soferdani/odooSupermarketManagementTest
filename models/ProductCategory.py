from oddo import models, fields


class ProductCategory (models.Model):
    _name = 'supermarket.productCategory'
    _description = 'ProductCategory'

    categoryName = fields.Char('Category Name')
