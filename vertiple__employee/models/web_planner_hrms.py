from odoo import api, models


class PlannerHrms(models.Model):

    _inherit = 'web.planner'

    @api.model
    def _get_planner_application(self):
        planner = super(PlannerHrms, self)._get_planner_application()
        planner.append(['planner_hrms', 'Hrms Planner'])
        return planner