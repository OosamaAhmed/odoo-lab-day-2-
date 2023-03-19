from odoo import models, fields, api,exceptions
from odoo.extensions import ValidationError


class customer(models.Model):

    _inherit = 'res.partner'
    related_patient_id = fields.Many2one('hms.patient', string='Related Patient')
    
    vat=fields.Char(required=True)
    email = fields.Char()
# ===============================================(check email,) ===============================
    @api.constrains('email')
    def check_email_Valid(self):
        for field in self:

            if field.email:
                isemailexist = self.env['hms.patient'].search([('Email', '=', field.email)], limit=1)
                if isemailexist:
                    raise exceptions.ValidationError('email already in use in patient')
# ===================================(delete validation linked to patient in hms)===============
#   no decerator on at and write 
    def unlink(self):
        for record in self:
            if record.related_patient_id:
                raise exceptions.ValidationError('you cannot delete')
        return super().unlink()
 