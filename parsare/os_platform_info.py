from xml.dom import minidom

#load xml file
xmldoc = minidom.parse('menu.xml')

#returns  Document object, a descendant of the Node class
#print(xmldoc.toxml())

#A Document always has only one child node, the root element of the XML document
print(xmldoc.childNodes)

itemlist = xmldoc.getElementsByTagName('name')
print(len(itemlist))
