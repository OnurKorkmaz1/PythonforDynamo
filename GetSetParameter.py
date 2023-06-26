"""
Create a simple Wall objects using python

"""
__author__ = 'Onur Korkmaz'

"""
Sample on how to create a Wall.
Use this sample along with the Video on Youtube.
"""


doorCat = UnwrapElement(IN[0])
result = []
#FilteredElementCollector
Collector = FilteredElementCollector(doc,doc.ActiveView.Id)
filter = ElementCategoryFilter(BuiltInCategory.OST_Doors)
doors = Collector.OfCategoryId(doorCat.Id).FirstElement()

parameters = doors.GetOrderedParameters()

for i in parameters:
	result.append(i.Definition.BuiltInParameter)

doorlvlp = doors.get_Parameter(BuiltInParameter.DOOR_FRAME_MATERIAL)

## storage type AsString() , AsDouble()

parameter_strogetype = doorlvlp.StorageType
parameter_value = doorlvlp.AsString()

TransactionManager.Instance.EnsureInTransaction(doc)


doorlvlp.Set("WOOD")

TransactionManager.Instance.TransactionTaskDone()

OUT = wall , doors , parameters , result ,doorlvlp ,parameter_strogetype , parameter_value