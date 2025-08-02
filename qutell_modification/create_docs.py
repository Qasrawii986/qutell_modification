import frappe

def create_docs():
    if frappe.db.exists("DocType", "Informations"):
        return  # تم إنشاؤه مسبقًا

    frappe.get_doc({
        "doctype": "DocType",
        "name": "Informations",
        "module": "Qutell Modification",
        "custom": 1,
        "fields": [
            {
                "fieldname": "description",
                "label": "Description",
                "fieldtype": "Data"
            }
        ],
        "permissions": [{"role": "System Manager"}],
    }).insert()
