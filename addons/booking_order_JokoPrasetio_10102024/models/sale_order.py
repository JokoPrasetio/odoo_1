from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_booking_order = fields.Boolean(string='Is Booking Order', default=False)
    team_id = fields.Many2one('service.team', string='Team', ondelete='set null')
    team_leader_id = fields.Many2one('res.users', string='Team Leader')
    team_member_ids = fields.Many2many('res.users', string='Team Members')
    booking_start = fields.Datetime(string='Booking Start')
    booking_end = fields.Datetime(string='Booking End')
