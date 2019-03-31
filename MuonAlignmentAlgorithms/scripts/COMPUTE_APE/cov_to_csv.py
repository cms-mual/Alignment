# Will parse the XML file generate by CREATE_APE into a CSV file. 
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
            if child.tag == 'DTChamber':
                chamber_ape['wheel'] = child.attrib['wheel'] 
                chamber_ape['station'] = child.attrib['station'] 
                chamber_ape['sector'] = child.attrib['sector'] 
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
  
  
def savetoCSV(newsitems, filename): 
  
    # specifying the fields for csv file 
    fields = ['wheel', 'station', 'sector', 'xx', 'yy', 'zz', 'aa', 'bb', 'cc'] 
  
    # writing to csv file 
    with open(filename, 'w') as csvfile: 
  
        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
  
        # writing headers (field names) 
        writer.writeheader() 
  
        # writing data rows 
        writer.writerows(newsitems) 
  
      
def main(input, output): 
    # input: input.xml
    # output: output.csv
  
    # parse xml file 
    chamber_info = parseXML(input) 
    # store APEs for all chambers in a csv file 
    savetoCSV(chamber_info, output) 
      
      
if __name__ == "__main__": 
  
    # calling main function 
    main()
