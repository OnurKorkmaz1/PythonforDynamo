"""
Create a simple Wall objects using python

"""
__author__ = 'Onur Korkmaz'

"""
Sample on how to create a Wall.
Use this sample along with the Video on Youtube.
"""
import clr

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

clr.AddReference('System')
from System.Collections.Generic import List

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.GeometryConversion)
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
uidoc=DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
##########################################################################


element = UnwrapElement(IN[0])

name = []
value= []


#elem_param = elem.get_Parameter(BuiltInParameter.ALL_MODEL_INSTANCE_COMMENTS)
el_param = element.LookupParameter("Base Offset")
el_param_value = el_param.AsDouble()


def convert_internal_units(value, get_internal =True , units= "m"):

	if units == "m": units = UnitTypeId.Meters
	elif units == "m2": units = UnitTypeId.SquareMeters
	elif units == "cm": units = UnitTypeId.Centimeters
	
	
	if get_internal:
		return UnitUtils.ConvertToInternalUnits(value,units)
	return UnitUtils.ConvertFromInternalUnits(value,units)
	
real_values = convert_internal_units(el_param_value)
	
	

TransactionManager.Instance.EnsureInTransaction(doc)
deger = convert_internal_units(0.2)
el_param.Set(deger)
TransactionManager.Instance.TransactionTaskDone()



OUT = el_param, el_param_value, real_values