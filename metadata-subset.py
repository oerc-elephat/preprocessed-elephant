import glob
import os
from lxml import etree


def save_biblio ( author, pubplace, publisher, date, idno0, idno1, idno2, idno3, idno4, idno5, title0, title1, title2):
    file = open ("eebo_records_raw.xls", "a")
    
    outputstring=(author + "%" + pubplace +"%" + publisher + "%" + date +"%" + idno0 +"%" + idno1+"%" + idno2+"%" + idno3+"%" + idno4+"%" + idno5+"%" + title0.replace("\n","")+"%" + title1.replace("\n","")+"%" + title2.replace("\n","") +"\n")
    
    file.write(strip_non_ascii(outputstring))
    file.close ()

#def create_new_output():
#    file = open ("eebo_records_raw.xls", "w")
#    file.write("author%pubplace%publisher%date%idno0%idno1%idno2%idno3%idno4%idno5%title0%title1%title2\n" )
#    file.close ()

def strip_non_ascii(string):
    # Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

# Required module


# Function for getting files from a folder
def fetchFiles(pathToFolder, flag, keyWord):
    ''' fetchFiles() requires three arguments: pathToFolder, flag and keyWord
        
    flag must be 'STARTS_WITH' or 'ENDS_WITH'
    keyWord is a string to search the file's name
    
    Be careful, the keyWord is case sensitive and must be exact
    
    Example: fetchFiles('/Documents/Photos/','ENDS_WITH','.jpg')
        
    returns: _pathToFiles and _fileNames '''
    
    _pathToFiles = []
    _fileNames = []

    for dirPath, dirNames, fileNames in os.walk(pathToFolder):
        if flag == 'ENDS_WITH':
            selectedPath = [os.path.join(dirPath,item) for item in fileNames if item.endswith(keyWord)]
            _pathToFiles.extend(selectedPath)
            
            selectedFile = [item for item in fileNames if item.endswith(keyWord)]
            _fileNames.extend(selectedPath + selectedFile)
            
        elif flag == 'STARTS_WITH':
            selectedPath = [os.path.join(dirPath,item) for item in fileNames if item.startswith(keyWord)]
            _pathToFiles.extend(selectedPath)
            
            selectedFile = [item for item in fileNames if item.startswith(keyWord)]
            _fileNames.extend(selectedPath + selectedFile) 
                
        else:
            print (fetchFiles.__doc__)
            break
                        
        # Try to remove empty entries if none of the required files are in directory
        try:
            _pathToFiles.remove('')
            _imageFiles.remove('')
        except ValueError:
            pass
            
        # Warn if nothing was found in the given path
        #if selectedFile == []: 
        #   print( 'No files with given parameters were found in:\n', dirPath, '\n')
        
    print( len(_fileNames), 'files were found is searched folder(s)')
                
    return _fileNames





#Getlist of files in folder
#for each file
#    open file
#    read file into variable
#    author = varialbe.find("author")
#    date =  variable.find("publishdate")
#    publisher = variable.find("publisher")
#    save_book (author, date, date)


#<TITLE>
#<AUTHOR>
#<IDNO TYPE="eebo citation">99850024</IDNO>
#<PUBPLACE>London :</PUBPLACE>
#<PUBLISHER>
#<DATE>



os.chdir("/Users/terhi/Documents/eebo_all/eebo_phase1/XML_with_headers_attached/")
# Not using this function -> create_new_output()
file = open ("eebo_records_raw.xls", "w")
file.write("author%pubplace%publisher%date%idno0%idno1%idno2%idno3%idno4%idno5%title0%title1%title2\n" )

allxmlfiles=fetchFiles("/Users/terhi/Documents/eebo_all/eebo_phase1/XML_with_headers_attached/",'ENDS_WITH','.xml')

for filename in allxmlfiles:
#glob.glob("*.xml"):
  if (filename.startswith('/')):
     print (filename)

     doc = etree.parse(filename)
     root = doc.getroot()
     

     authorElem = root.xpath("//AUTHOR")


     author=""
     publisher=""
     publishplace=""
     title0=""
     title1=""
     title2=""
     title3=""
     idno0=""
     idno1=""
     idno2=""
     idno3=""
     idno4=""
     idno5=""
     publishdate=""
     
     
     if authorElem is not None  and len(authorElem)>1:     # checks to make sure there is an authorElem and that there is more than 1 author
#        print(authorElem)
#        print("Author0=" + authorElem[0].text)
         print("Author1=" + authorElem[1].text)
         author= authorElem[1].text
     else:
         print("Author1= Anonymous")
         author= "Anonymous"
# Both Author 0 and 1 always seem to give the same name. I've opted for Author1 rather than 0 to keep in line with historical publisher, place, date (see below).
# What to do when there is no author? 


     publisherElem = root.xpath("//PUBLISHER")
#    print(publisherElem)
#    print("Publisher0=" + publisherElem[0].text)
     print("Publisher1=" + publisherElem[1].text)
     publisher= publisherElem[1].text
# Publisher0 is the Text Creation Partnership. Thus kept Publisher1 as is the historical one.


     pubplaceElem = root.xpath("//PUBPLACE")
#    print(pubplaceElem)
#    print("PublishPlace0=" + pubplaceElem[0].text)
     print("PublishPlace1=" + pubplaceElem[1].text)
     publishplace= pubplaceElem[1].text
     titleElem = root.xpath("//TITLE")
#    print(titleElem)
     print("title0=" + titleElem[0].text)
     print("title1=" + titleElem[1].text)
     print("title2=" + titleElem[2].text)

     title0= titleElem[0].text
     title1= titleElem[1].text
     title2= titleElem[2].text
# Unfortunately have to keep all 3 titles because in some cases the Early English Books Online is title1, in others title2. Will have to tidy up manually later.


     IDNOElem = root.xpath("//IDNO")
#    print(IDNOElem)
     print("IDNO0=" + IDNOElem[0].text)
     print("IDNO1=" + IDNOElem[1].text)
     print("IDNO2=" + IDNOElem[2].text)
     print("IDNO3=" + IDNOElem[3].text)
     print("IDNO4=" + IDNOElem[4].text)
#     
     
     idno0= IDNOElem[0].text
     idno1= IDNOElem[1].text
     idno2= IDNOElem[2].text
     idno3= IDNOElem[3].text
     idno4= IDNOElem[4].text


     if IDNOElem is not None  and len(IDNOElem)>5: 
         idno5= IDNOElem[5].text
         print("IDNO5=" + IDNOElem[5].text)



     
     
#IDNO3 and IDNO4 seem to be the same but I think it's worth keeping both of them (is it EEBO and Proquest ids?)           

     dateElem = root.xpath("//DATE")


     
#    print(dateElem)
#    print("date0=" + dateElem[0].text)
     print("date1=" + dateElem[1].text)

     publishdate=dateElem[1].text


    
#    print("date2=" + dateElem[2].text)
#    print("date3=" + dateElem[3].text)
#    print("date4=" + dateElem[4].text)
#    print("date5=" + dateElem[5].text)
#    print("date6=" + dateElem[6].text)


#     date1 seems to be the original publication date. Makes sense, in line with Publisher1 and Pubplace1 as well.But not Author, as the first author in the record is the original writer and not the person who wrote the EEBO record.



     # Now Save this line to the excel export file
     # not using this function anymore  - we write the data now without closing the output file      save_biblio ( author, publishplace, publisher, publishdate, idno0, idno1, idno2, idno3, idno4, idno5, title0, title1, title2)
     outputstring=(author + "%" + publishplace +"%" + publisher + "%" + publishdate +"%" + idno0 +"%" + idno1+"%" + idno2+"%" + idno3+"%" + idno4+"%" + idno5+"%" + title0.replace("\n","")+"%" + title1.replace("\n","")+"%" + title2.replace("\n","") +"\n")
     file.write(strip_non_ascii(outputstring))

           
file.close     


