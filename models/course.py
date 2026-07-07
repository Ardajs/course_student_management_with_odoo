from odoo import models, fields, api


class Course(models.Model):
    _name = 'course.student_management'
    _description = 'Course Management'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')
    session_ids = fields.One2many(
        comodel_name='session.student_management',
        inverse_name='course_id',
        string='Sessions'
    )
    session_count = fields.Integer(
        string='Session Count',
        compute='_compute_session_count'
    )

    @api.depends('session_ids')
    def _compute_session_count(self):
        for course in self:
            course.session_count = len(course.session_ids)