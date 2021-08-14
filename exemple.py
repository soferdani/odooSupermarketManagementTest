
from odoo import models, fields, api

class ComputedModel(models.Model):

    _name = 'test.computed'

    name = fields.Char(compute='_compute_name')

    value = fields.Integer()



    @api.depends('value')

    def _compute_name(self):

        for record in self:

            record.name = "Record with value %s" % record.value



