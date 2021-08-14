# -*- coding: utf-8 -*-
from odoo import fields, models


class Customer(models.Model):
    _name = 'supermarket.customer'
    _description = 'Customer'

    name = fields.Char('Name', required=True)
    email = fields.Char('Email')
    city = fields.Char('City')
    street = fields.Char('Street')
