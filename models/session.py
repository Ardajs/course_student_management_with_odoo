from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Session(models.Model):
    _name = 'session.student_management'
    _description = 'Course Session Management'

    _sql_constraints = [
        (
            'unique_session_name_per_course',
            'unique(name, course_id)',
            'Session name must be unique per course.'
        )
    ]

    name = fields.Char(string='Session Name', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    course_id = fields.Many2one(
        comodel_name='course.student_management',
        string='Course',
        required=True
    )
    student_id = fields.Many2one(
        comodel_name='student.student_management',
        string='Student'
    )

    @api.onchange('start_date', 'end_date')
    def _onchange_dates(self):
        if self.start_date and self.end_date and self.end_date < self.start_date:
            return {
                'warning': {
                    'title': 'Invalid Date',
                    'message': 'End date cannot be earlier than start date.'
                }
            }

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for session in self:
            if session.start_date and session.end_date and session.end_date < session.start_date:
                raise ValidationError('End date cannot be earlier than start date.')