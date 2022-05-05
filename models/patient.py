from odoo import models, fields, api
from datetime import datetime

class Patient(models.Model):
    _name = "patient.patient"
    _description = "Patient"
    _order = "id desc"
    
    name = fields.Char(string='Name', required=True)
    dob = fields.Date(string='Date of Birth', required=True)
    age = fields.Float(string='Age', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ], string='Gender', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone', required=True)
    permanent_address = fields.Char(string='Permanent Address', required=True)
    current_address = fields.Char(string='Current Address', required=True)
    state = fields.Selection([
        ('opd', 'OPD'),
        ('admit', 'Admit'),
        ('discharge', 'Discharge'),
    ], string='Status', required=True, default='opd')
    opd_date = fields.Date(string='OPD Date', readonly=True, default=datetime.today())
    admit_date = fields.Date(String='Admit Date', readonly=True)
    discharge_date = fields.Date(String='Discharge Date', readonly=True)
    doctor_ids = fields.Many2many('doctor.doctor', string='Doctor')
    emergency_contact_ids = fields.One2many('patient.emergency.contact', 'patient_id', string='Emergency Contact')
    
    def admit_patient(self):
        self.write({
            'state': 'admit',
            'admit_date': datetime.today()
        })
        
    def discharge_patient(self):
        self.write({
            'state': 'discharge',
            'discharge_date': datetime.today()
        })
    
 
class EmergencyContact(models.Model):
    _name = "patient.emergency.contact"
    _description = "Patient Emergency Contact"
    _order = "id desc"
    
    patient_id = fields.Many2one('patient.patient')
    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone', required=True)
    reln = fields.Char(string='Relation', required=True)