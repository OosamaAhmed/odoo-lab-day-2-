
from odoo import models,fields ,api,exceptions,tools
from datetime import datetime


class Hospitals(models.Model):
    _name ='hms.patient'
    
    FirsName=fields.Char()
    LastName=fields.Char()
    BirthDate=fields.Date()
    CRRatio=fields.Float()
    Bloodtype=fields.Selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')])
    PCR=fields.Boolean()
    Image=fields.Image()
    Address=fields.Text()
    Age=fields.Integer()

    # ========================()=====================

    state = fields.Selection([ ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious')],string='State', default='undetermined')
        # ========================(email)=====================
    Email = fields.Char(string='Email', required=True)
    _sql_constraints = [
            ('email_unique', 'unique(Email)', 'Email already exists'),
        ]

    departemnt_id=fields.Many2one('hms.department', string='Department')
    doctors_id=fields.Many2many('hms.doctors', string='Doctors')
    History=fields.Char(string='History')
#=========================(on change birthdate)=======================================
    @api.onchange('BirthDate')
    def onchange_birthdate(self):
        if self.BirthDate :
             self.Age=datetime.now().year - self.BirthDate.year
# =============================================================================
 
    @api.constrains('Email')
    def check_email_Valid(self):
        for record in self:
            if self.Email and not tools.email_re.match(record.Email):
                raise exceptions.ValidationError(" Email address not valid")