from odoo import models, fields

class ResMunicipality(models.Model):
    _name = 'res.country.state.municipality'
    _description = 'Municipios de Venezuela'
    _order = 'name'

    name = fields.Char(string='Municipio', required=True)
    state_id = fields.Many2one('res.country.state', string='Estado', required=True, ondelete='cascade')
    code = fields.Char(string='Código', help='Código opcional del municipio')