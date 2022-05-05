from odoo import models, fields, api
   

class Doctor(models.Model):
    _name = "doctor.doctor"
    _description = "Doctor"
    _order = "id desc"
    
    name = fields.Char(string='Name', required=True)
    dob = fields.Date(string='Date of Birth', required=True)
    phone = fields.Char(string='Phone', required=True)
    specialization = fields.Char(string='Specialization', required=True)