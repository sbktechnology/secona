# Copyright (c) 2013, mipl and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Facility Type')

class TestFacilityType(unittest.TestCase):
	pass
