import frappe

def execute(filters=None):
    columns = [
        {"label": "Lines", "fieldname": "lines", "fieldtype": "Data", "width": 300},
        {"label": "Task Type", "fieldname": "task_type", "fieldtype": "Data", "width": 150},
        {"label": "Cost", "fieldname": "cost", "fieldtype": "Currency", "width": 120},
        {"label": "Qty", "fieldname": "qty", "fieldtype": "Float", "width": 80},
        {"label": "Margin", "fieldname": "margin", "fieldtype": "Percent", "width": 100},
        {"label": "Indent", "fieldname": "indent", "fieldtype": "Int", "hidden": 1},
    ]

    data = []

    project_budgets = frappe.get_all("Project Budget", filters={"docstatus": ["<", 2]}, fields=["name", "project_name"])

    for pb in project_budgets:
        # استرجع كل المهام لهذا المشروع مرة واحدة
        all_tasks = frappe.get_all("Project Tasks",
            filters={"parent": pb.name},
            fields=["cost_estimated", "qty", "margin"])

        # ✅ حساب مجاميع المشروع بالكامل
        total_cost = sum(t.cost_estimated or 0 for t in all_tasks)
        total_qty = sum(t.qty or 0 for t in all_tasks)
        try:
            total_margin = round(sum((t.margin or 0) * (t.qty or 1) for t in all_tasks) / total_qty, 2)
        except ZeroDivisionError:
            total_margin = 0

        # 🟩 السطر الرئيسي = Project Budget + المجاميع
        data.append({
            "lines": f"{pb.name} - {pb.project_name}",
            "task_type": "",
            "cost": total_cost,
            "qty": total_qty,
            "margin": total_margin,
            "indent": 0
        })

        task_types = frappe.db.get_all("Project Tasks", filters={"parent": pb.name}, fields=["DISTINCT task_type"])

        for ttype in task_types:
            tasks = frappe.get_all("Project Tasks",
                                filters={"parent": pb.name, "task_type": ttype.task_type},
                                fields=["task", "cost_estimated", "qty", "margin"])

            # ✅ حساب المجاميع لهذا النوع
            total_cost = sum(t.cost_estimated or 0 for t in tasks)
            total_qty = sum(t.qty or 0 for t in tasks)
            try:
                total_margin = round(sum((t.margin or 0) * (t.qty or 1) for t in tasks) / total_qty, 2)
            except ZeroDivisionError:
                total_margin = 0

            # 🟨 الصف التجميعي (Type)
            data.append({
                "lines": f"Type: {ttype.task_type}",
                "task_type": ttype.task_type,
                "cost": total_cost,
                "qty": total_qty,
                "margin": total_margin,
                "indent": 1
            })

            # السطور الفرعية (المهام)
            for task in tasks:
                data.append({
                    "lines": task.task,
                    "task_type": ttype.task_type,
                    "cost": task.cost_estimated,
                    "qty": task.qty,
                    "margin": task.margin,
                    "indent": 2
                })

    return columns, data
