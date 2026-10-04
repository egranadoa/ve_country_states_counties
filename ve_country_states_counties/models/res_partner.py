from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    municipality_id = fields.Many2one(
        'res.country.state.municipality', 
        string='Municipio',
        domain="[('state_id', '=', state_id)]",
        help="Municipio perteneciente al estado seleccionado."
    )

    parish_id = fields.Many2one(
        'res.country.state.municipality.parish',
        string='Parroquia',
        domain="[('municipality_id', '=', municipality_id)]",
        help="Parroquia perteneciente al municipio seleccionado."
    )

    @api.onchange('state_id')
    def _onchange_state_id_municipality(self):
        """Limpia el campo municipio si se cambia el estado y el municipio actual no pertenece a ese nuevo estado."""
        if self.municipality_id and self.municipality_id.state_id != self.state_id:
            self.municipality_id = False

    @api.onchange('municipality_id')
    def _onchange_municipality_id_ve(self):
        """Limpia la parroquia si se cambia el municipio."""
        if self.parish_id and self.parish_id.municipality_id != self.municipality_id:
            self.parish_id = False