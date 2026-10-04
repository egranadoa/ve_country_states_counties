from odoo import models, fields

class ResParish(models.Model):
    _name = 'res.country.state.municipality.parish'
    _description = 'Parroquias de Venezuela'
    _order = 'name'

    name = fields.Char(string='Parroquia', required=True)
    municipality_id = fields.Many2one(
        'res.country.state.municipality', 
        string='Municipio', 
        required=True, 
        ondelete='cascade'
    )
    code = fields.Char(string='Código', help='Código opcional de la parroquia')