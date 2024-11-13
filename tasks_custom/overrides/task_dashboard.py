from frappe import _

def get_data(data=None):
    return {
        "fieldname": "task",
        "transactions": [
            {"label": _("Activity"), "items": ["Timesheet"]},
            {"label": _("Sales"), "items": ["Sales Invoice"]},
        ],
    }