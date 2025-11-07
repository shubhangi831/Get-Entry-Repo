# Copyright (c) 2025, sk and contributors
# For license information, please see license.txt

# import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data


import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {"label": "ID", "fieldname": "name", "fieldtype": "Data", "width": 150},
        {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 120},
        {"label": "Time", "fieldname": "time", "fieldtype": "Time", "width": 120},
        {"label": "Vender", "fieldname": "vender", "fieldtype": "Data", "width": 200},
        {"label": "Receiver", "fieldname": "receiver", "fieldtype": "Data", "width": 200},
    ]

def get_data(filters):
    conditions = ""
    values = {}

    if filters.get("vender"):
        conditions += " AND vender = %(vender)s"
        values["vender"] = filters["vender"]

    if filters.get("receiver"):
        conditions += " AND receiver LIKE %(receiver)s"
        values["receiver"] = f"%{filters['receiver']}%"

    if filters.get("name"):
        conditions += " AND name LIKE %(name)s"
        values["name"] = f"%{filters['name']}%"

    if filters.get("date"):
        conditions += " AND date = %(date)s"
        values["date"] = filters["date"]

    data = frappe.db.sql(f"""
        SELECT
            name,
            date,
            time,
            vender,
            receiver
        FROM `tabGet Entry Doctype`
        WHERE 1=1 {conditions}
        ORDER BY creation DESC
    """, values, as_dict=True)

    return data


# def get_data(filters):
#     conditions = ""
#     values = {}

#     if filters.get("vender"):
#         conditions += " AND vender = %(vender)s"
#         values["vender"] = filters["vender"]

#     data = frappe.db.sql(f"""
#         SELECT
#             name,
#             date,
#             time,
#             vender,
#             receiver
#         FROM `tabGet Entry Doctype`
#         WHERE 1=1 {conditions}
#         ORDER BY creation DESC
#     """, values, as_dict=True)

#     return data
