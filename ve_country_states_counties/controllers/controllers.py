# from odoo import http


# class VeCountryStatesCounties(http.Controller):
#     @http.route('/ve_country_states_counties/ve_country_states_counties', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ve_country_states_counties/ve_country_states_counties/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ve_country_states_counties.listing', {
#             'root': '/ve_country_states_counties/ve_country_states_counties',
#             'objects': http.request.env['ve_country_states_counties.ve_country_states_counties'].search([]),
#         })

#     @http.route('/ve_country_states_counties/ve_country_states_counties/objects/<model("ve_country_states_counties.ve_country_states_counties"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ve_country_states_counties.object', {
#             'object': obj
#         })

