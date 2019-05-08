# Will parse the XML file generate by CREATE_APE into a CSV file.
# USAGE:
# python convertApeXmlCsv.py input.xml output.csv

import sys
import csv 
import xml.etree.ElementTree as ET 
  
  
def parseXML(xmlfile): 
  
    # create element tree object 
    tree = ET.parse(xmlfile) 
  
    # get root element 
    root = tree.getroot() 
  
    # create empty list for chambers 
    chambers = [] 
  
    # iterate news items 
    for item in root.findall('./operation'): 
        chamber_ape = {} 
  
        # iterate child elements of item 
        for child in item: 
  
            # special checking for namespace object content:media
            if child.tag == 'segments':
                chamber_ape['NSegments'] = child.attrib['n']
            if child.tag == 'DTChamber':
                chamber_ape['wheel'] = child.attrib['wheel'] 
                chamber_ape['station'] = child.attrib['station'] 
                chamber_ape['sector'] = child.attrib['sector']
            elif child.tag == 'CSCChamber':
                chamber_ape['endcap'] = child.attrib['endcap']
                chamber_ape['station'] = child.attrib['station']
                chamber_ape['ring'] = child.attrib['ring']
                chamber_ape['chamber'] = child.attrib['chamber']
            elif child.tag == 'setape':
                chamber_ape['xx'] = child.attrib['xx']
                chamber_ape['yy'] = child.attrib['yy']
                chamber_ape['zz'] = child.attrib['zz']
                chamber_ape['aa'] = child.attrib['aa']
                chamber_ape['bb'] = child.attrib['bb']
                chamber_ape['cc'] = child.attrib['cc']
  
        # append news dictionary to news items list 
        chambers.append(chamber_ape) 
      
    # return news items list 
    return chambers 
  
  
def savetoCSV(chamber_info, detector, filename): 
  
    # specifying the fields for csv file
    if detector == "DT":
      fields = ['NSegments','wheel', 'station', 'sector', 'xx', 'yy', 'zz', 'aa',
                'bb',  'cc']
    if detector == "CSC":
      fields = ['NSegments', 'endcap', 'station', 'ring', 'chamber', 'xx', 'yy', 'zz',
                'aa', 'bb', 'cc']
  
    # writing to csv file 
    with open(filename, 'w') as csvfile: 
  
        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
  
        # writing headers (field names) 
        writer.writeheader() 
  
        # writing data rows 
        writer.writerows(chamber_info) 
  
      
def main(input, detector, output): 
    # input: input.xml
    # detector = DT or CSC
    # output: output.csv
  
    # parse xml file 
    chamber_info = parseXML(input) 
    # store APEs for all chambers in a csv file 
    savetoCSV(chamber_info, detector, output) 


if __name__ == "__main__": 
  
    # calling main function 
    if len(sys.argv)>2:
        input_xml = sys.argv[1]
        det = sys.argv[2]
        output_csv = sys.argv[3]
    else:
        print("usage: python convertApeXmlCsv.py input.xml output.csv") 

    main(input_xml, det, output_csv)

