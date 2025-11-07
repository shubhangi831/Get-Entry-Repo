// Copyright (c) 2025, sk and contributors
// For license information, please see license.txt

frappe.query_reports["Get Details Report"] = {
	"filters": [
		{
			"fieldname": "name",
			"label": "ID",
			"fieldtype": "Data",
			"reqd": 0
		},
		{
            "fieldname": "vender",
            "label": "Vender",
            "fieldtype": "Data",
			"reqd": 0
        },
		{
            "fieldname": "receiver",
            "label": "Receiver",
            "fieldtype": "Data",
            "reqd": 0
        },
		{
            "fieldname": "date",
            "label": "Date",
            "fieldtype": "Date",
			"reqd": 0
        },
	]
};
