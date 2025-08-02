import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.custom.doctype.property_setter.property_setter import make_property_setter
# from frappe.core.doctype.client_script.client_script import create_client_script
from frappe.core.doctype.print_format.print_format import create_print_format
from frappe.modules.import_file import import_file_by_path
from pathlib import Path
import os

def after_app_install(app_name):
    if app_name != "qutell_modification":
        return

    secho("Running after_app_install for Qutell Modification...", fg="green")

    base_path = Path(frappe.get_app_path("qutell_modification")) / "qutell_modification" / "fixtures"

    # 1️⃣ Load Custom Fields
    load_json_fixtures(base_path / "custom_field.json", "Custom Field")

    # 2️⃣ Load Property Setters
    load_json_fixtures(base_path / "property_setter.json", "Property Setter")

    # 3️⃣ Load Client Scripts
    load_json_fixtures(base_path / "client_script.json", "Client Script")

    # 4️⃣ Load Print Formats
    load_json_fixtures(base_path / "print_format.json", "Print Format")

    # 5️⃣ Load Reports
    load_json_fixtures(base_path / "report.json", "Report")

    # 6️⃣ Load Server Scripts
    load_json_fixtures(base_path / "server_script.json", "Server Script")

    # 7️⃣ Load Workspaces
    load_json_fixtures(base_path / "workspace.json", "Workspace")

    frappe.db.commit()
    secho("✅ All customizations installed successfully.", fg="cyan")


def load_json_fixtures(path, doctype):
    import json

    if not path.exists():
        print(f"⚠️ File not found: {path}")
        return

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for d in data:
        docname = d.get("name")
        existing = frappe.db.exists(doctype, docname)
        if not existing:
            doc = frappe.get_doc(d)
            doc.insert(ignore_permissions=True)
            print(f"✔️ Inserted: {doctype} - {docname}")
        else:
            print(f"⏭️ Skipped (exists): {doctype} - {docname}")
