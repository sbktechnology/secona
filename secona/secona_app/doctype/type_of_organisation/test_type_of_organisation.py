# Copyright (c) 2013, mipl and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Type of Organisation')

class TestTypeofOrganisation(unittest.TestCase):
	pass
