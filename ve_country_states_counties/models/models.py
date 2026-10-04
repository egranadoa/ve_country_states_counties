# from odoo import models, fields, api


# class ve_country_states_counties(models.Model):
#     _name = 've_country_states_counties.ve_country_states_counties'
#     _description = 've_country_states_counties.ve_country_states_counties'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

