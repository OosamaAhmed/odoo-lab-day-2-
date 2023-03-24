from odoo import models, fields, api,exceptions


class customer(models.Model):
    _inherit = 'res.partner'
    vat=fields.Char(required=True)
    related_patient_id = fields.Many2one('hms.patient')
    email = fields.Char()
# ===============================================(check email,) ===============================
    @api.constrains('related_patient_id')
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
 