from xml.etree import ElementTree as ET

def main():
    _appendXML()

def _createXML():
    root = ET.Element('lab')
    person1 = ET.SubElement(root, 'person', {'name':'Brown'})
    age1 = ET.SubElement(person1, 'age')
    age1.text = '21'
    gender1 = ET.SubElement(person1, 'gender')
    gender1.text = 'male'
    person2 = ET.SubElement(root, 'person', {'name':'Red'})
    age2 = ET.SubElement(person2, 'age')
    age2.text = '23'
    gender2 = ET.SubElement(person2, 'gender')
    gender2.text = 'female'
    tree = ET.ElementTree(root)
    tree.write('G:/pythonStudy/xml/sample.xml', encoding="utf-8", xml_declaration=True)

def _appendXML():
    tree = ET.parse('G:/pythonStudy/xml/sample.xml')
    root = tree.getroot()
    person3 = ET.Element('person', {'name':'Brown'})
    age3 = ET.SubElement(person3, 'age')
    age3.text = '20'
    gender3 = ET.SubElement(person3, 'gender')
    gender3.text = 'male'
    root.append(person3)
    tree.write('G:/pythonStudy/xml/sample.xml', encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    main()
