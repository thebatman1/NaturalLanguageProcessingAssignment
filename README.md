# NLP Assignment

## System information
The codes have been written mostly using the formatting and syntax of python3.6. So whenever I mention python, I'm referring to python3.6.
Operating System: Ubuntu 16.04

### 1. Corpus stuff
The code is pretty easy to understand I hope. The corpus was taken from <a href="https://lindat.mff.cuni.cz/repository/xmlui/handle/11858/00-097C-0000-0001-BD17-1?show=full&fbclid=IwAR0OwHxfXLUag76IDiEFYkxT7-acj7j0OD4z_TPFMEx0xNE1fxBmyHo5TqE">here</a>. You can look for another corpus if you want to.
Bear in mind though that Hindi symbols are a part of utf-8(one of the many utfs). That's why in line 8, I've used codecs.open rather than simple open.

**Usage: python playCorpus.py**

### 2. Remove stopwords
The file stopwordsEnglish.txt contains a list of stopwords taken from <a href="https://www.ranks.nl/stopwords">here</a>. What the code does is pretty simple:
1. Load the stopwords in a set.
2. Read the input file word by word.
3. Copy the non-stopwords(?) from the input file to an output file.

**Usage: python removeStopwords.py inputfile.txt outputfile.txt**

### 3. Implement Porter Stemmer Algorithm
The class is implemented in PorterStemmer.py. You can run the code from there or can get a little fancy like I did and write a separate file which I conveniently called **stemwords.py** and import the Porter Stemmer class.(Modularity! :P)
Credits for the code goes to <a href="https://github.com/jedijulia/porter-stemmer">this</a> repository.

**Usage: python stemWord.py word**

### 4. POS Tagger
Haven't done it yet. But sir has asked us to implement using HMM tagging.

### 5. Search Engine using Apache Nutch
Now if you have a Windows system, this is probably not for you. Although you could always install virtualbox. So in the following lines I'll walk you through what changes you have to make to make it work for you in an **Ubuntu** system.

1. Download Nutch and Apache Tomcat from <a href="https://drive.google.com/drive/folders/1PJZP69iF51V5MhyEWVm8OUwJkeiNstv7?usp=sharing">here</a>. Nutch is mostly configured here apart from the other steps in the report AND mentioned below.
2. Extract the files in a convenient place.
3. In the home directory(/home/your-username) open the file .bashrc and add the given line at the end.<br>
export CATALINA\_HOME=path\_to\_where\_you\_extracted/apache-tomcat-6.0.53<br>
4. Go in the Nutch folder and in line 59 of ReadDirRecursevly.java, specify the source path from which the crawling data has to be taken. Similary in line 60, specify the destination of the text file generated list of urls. To get the directory, what I did was download a website using the command <i>wget -mk -p -r website-address</i> and specify the directory in which it was saved in.  
5. Run ReadDirRecursevly.java like any java program. The destination that you specified earlier will now have a list of urls and stuff.
6. Run the crawl.
**./bin/nutch crawl path(eg. urls/urls.txt)**
7. After the crawl is performed, a folder named **crawl-XXXXXXXXXXX** will be generated. Go to **conf/nutch-default.xml, Line 586** and specify the crawl path,ie the path of the generated folder there.
8. Run **ant; ant war;**
9. Run **cp build/nutch-0.9.war apache-version/webapps/**
10. Finally run **apache-version/bin/catalina.sh start** and go to **localhost:8080/nutch-0.9** to access your search engine.
11. Remember to stop the server before making any changes to the files.

### 6. Neural Translation using OpenNMT.
Sandeep has done it. Sir said just train the model and perform the translation. BEWARE: Training takes several days :P
