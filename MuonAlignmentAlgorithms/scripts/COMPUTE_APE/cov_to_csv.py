#Python code to illustrate parsing of XML files 
# importing the required modules 
import csv 
#import requests 
import xml.etree.ElementTree as ET 
  
  
def parseXML(xmlfile): 
  
    # create element tree object 
    tree = ET.parse(xmlfile) 
  
    # get root element 
    root = tree.getroot() 
  
    # create empty list for news items 
    newsitems = [] 
  
    # iterate news items 
    for item in root.findall('./operation'): 
       # print("Getting operation...")
        # empty news dictionary 
        news = {} 
  
        # iterate child elements of item 
        for child in item: 
  
            # special checking for namespace object content:media 
            if child.tag == 'DTChamber':
        #        print('getting DTChamber')
                news['wheel'] = child.attrib['wheel'] 
                news['station'] = child.attrib['station'] 
                news['sector'] = child.attrib['sector'] 
            elif child.tag == 'setape':
         #       print('getting ape')
                news['xx'] = child.attrib['xx']
                news['yy'] = child.attrib['yy']
                news['zz'] = child.attrib['zz']
                news['aa'] = child.attrib['aa']
                news['bb'] = child.attrib['bb']
                news['cc'] = child.attrib['cc']
  
        # append news dictionary to news items list 
        newsitems.append(news) 
      
    # return news items list 
    return newsitems 
  
  
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
  
      
def main(): 
    # load rss from web to update existing xml file 
    #loadRSS() 
  
    # parse xml file 
    newsitems = parseXML('APEs_COVall_DT_2018Av3_TEST_COV_MATR.xml') 
    print('parsing XML')
    # store news items in a csv file 
    savetoCSV(newsitems, 'topnews.csv') 
      
      
if __name__ == "__main__": 
  
    # calling main function 
    main()
