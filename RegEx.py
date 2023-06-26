"""
Create a simple Wall objects using python

"""
__author__ = 'Onur Korkmaz'

"""
Sample on how to create a Wall.
Use this sample along with the Video on Youtube.
"""

import clr
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

#Preparing input

walls = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()


names = []
for i in walls:
	names.append(i.Name)


def check_family_name(family_name):
    pattern = r'^[A-Z]{1}[0-9]{4}\.[0-9]{2}_\w+$'
    if re.search(pattern, family_name) == None:
        return "İsimlendirme kuralına uygun."
    else:
        return "İsimlendirme kuralına uymuyor."

list = []
for i in names:
	list.append(check_family_name(i))

	
#result = check_family_name(names)

OUT = names , list