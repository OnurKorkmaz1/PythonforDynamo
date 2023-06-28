"""
---> GET LINK DOCUMENTS <---

__author__ = 'Onur Korkmaz';

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


Link_Instances = FilteredElementCollector(doc).OfClass(RevitLinkInstance)

Link_Document  = []
Link_Name      = []
Link_Path      = []

for i in Link_Instances:
	Link_Document.append(i.GetLinkDocument())
	Link_Name.append(i.Name)
	Link_Path.append(i.GetLinkDocument().PathName)	
   	
OUT = Link_Document,Link_Name ,Link_Instances ,Link_Path