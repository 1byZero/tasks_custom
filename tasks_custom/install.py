import frappe

def after_install():
    # Check if custom field already exists
    if not frappe.db.exists("Custom Field", "Sales Invoice-task"):
        # Create new custom field
        new_custom_field = frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Sales Invoice",
            "fieldname": "task",
            "label": "Task",
            "fieldtype": "Link",
            "options": "Task",
            "insert_after": "project",
            "owner": "Administrator"
        })
        new_custom_field.insert(ignore_permissions=True)
        frappe.db.commit()