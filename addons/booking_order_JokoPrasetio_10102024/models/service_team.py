from odoo import models, fields

class ServiceTeam(models.Model):
    _name = 'service.team'
    _description = 'Service Team'

    name = fields.Char(string='Team Name', required=True)
    leader_id = fields.Many2one('res.users', string='Team Leader', required=True)
    member_ids = fields.Many2many('res.users', string='Team Members')
    active = fields.Boolean(string="Active", default=True)


