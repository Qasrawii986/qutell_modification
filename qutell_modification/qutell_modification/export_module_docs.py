import frappe
from frappe.modules.export_file import export_to_files

def export_docs_by_module(module_name):
    doctypes = [
        "DocType",
        "Client Script",
        "Custom Field",
        "Print Format",
        "Report",
        "Property Setter",
        "Server Script",
        "Workspace"
    ]

    success = 0
    failed = 0

    for doctype in doctypes:
        try:
            # نحاول الفلترة بالموديول
            try:
                records = frappe.get_all(doctype, filters={"module": module_name})
            except Exception as e:
                print(f"⚠️ Could not filter {doctype} by module. Exporting all: {e}")
                records = frappe.get_all(doctype)

            for record in records:
                print(f"Exporting {doctype}: {record.name}")
                try:
                    export_to_files(record_list=[[record.name, doctype]], record_module=module_name)
                    success += 1
                except Exception as e:
                    print(f"❌ Failed to export {doctype} '{record.name}': {e}")
                    failed += 1

        except Exception as e:
            print(f"❌ Completely skipped {doctype} due to fatal error: {e}")
            failed += 1

    print("\n✅ Export completed!")
    print(f"✅ Success: {success}")
    print(f"❌ Failed: {failed}")

def run():
    export_docs_by_module("Qutell Modification")
