import frappe
from frappe.modules.export_file import export_to_files

def export_docs_by_module(module_name):
    # أنواع العناصر التي سيتم تصديرها
    doctypes = [
        "DocType",
        "Client Script",
        "Custom Field",
        "Print Format",
        "Report",
        "Property Setter",
        "Server Script",
        "Workspace",
        "Custom DocPerm"
    ]

    for doctype in doctypes:
        records = frappe.get_all(doctype, filters={"module": module_name})
        for record in records:
            print(f"Exporting {doctype}: {record.name}")
            try:
                export_to_files(record_list=[[record.name, doctype]], record_module=module_name)
            except Exception as e:
                print(f"❌ Failed to export {doctype} '{record.name}': {e}")

def run():
    export_docs_by_module("Qutell Modification")
