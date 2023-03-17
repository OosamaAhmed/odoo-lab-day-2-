from odoo import models, fields


class Doctors(models.Model):
    _name='hms.doctors'
    firstname=fields.Char()
    lastname=fields.Char()
    images=fields.Image()
