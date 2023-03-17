
from odoo import models,fields

class Hospitals(models.Model):
    _name ='hms.patient'
    FirsName=fields.Char()
    LastName=fields.Char()
    BirthDate=fields.Char()
    CRRatio=fields.Float()
    Bloodtype=fields.Selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')])
    PCR=fields.Boolean()
    Image=fields.Image()
    Address=fields.Text()
    Age=fields.Integer()

    state = fields.Selection([ ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious')],string='State', default='undetermined')
    departemnt_id=fields.Many2one('hms.department', string='Department')
    doctors_id=fields.Many2many('hms.doctors', string='Doctors')
    History=fields.Char(string='History')
