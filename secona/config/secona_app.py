from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Setup Identification",
					"description": _("Setup Identification For Secona"),
				},
				{
					"type": "doctype",
					"name": "Asset Distribution",
					"description": _("Asset Distribution For Secona."),
				},
				{
					"type": "doctype",
					"name": "Physical Zone Criticality",
					"description": _("Create Physical Zone Criticality."),
				},
			]
		},
		{
			"label": _("Tools"),
			"icon": "icon-wrench",
			"items": [
				{
					"type": "doctype",
					"name": "Facility Type",
					"description":_("Facility Type Details"),
				},
				{
					"type": "doctype",
					"name": "Type of Organisation",
					"description": _("All Type of Organisation"),
				},
			]
		},
	]
