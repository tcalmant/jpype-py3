#!/usr/bin/env python3

#*****************************************************************************
#   Copyright 2004-2008 Steve Menard
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#*****************************************************************************
import time
from jpype import javax, JProxy, JPackage, startJVM, getDefaultJVMPath, \
    shutdownJVM

import os.path
root = os.path.abspath(os.path.dirname(__file__))
classes = os.path.join(root, "classes")
startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path={0}".format(classes))

# XML test
Element = JPackage("org").w3c.dom.Element

class ContentHandler(object) :
    def characters(self, ch, start, length) :
        pass

    def endDocument(self) :
        pass

    def endElement(self, namespaceURI, localName, qName) :
        pass

    def endPrefixMapping(self, prefix) :
        pass

    def ignorableWhitespace(self, ch, start, length) :
        pass

    def processingInstruction(self, target, data) :
        pass

    def setDocumentLocator(self, locator) :
        pass

    def skippedEntity(self, name) :
        pass

    def startDocument(self,) :
        pass

    def startElement(self, namespaceURI, localName, qName, atts) :
        pass

    def startPrefixMapping(self, prefix, uri) :
        pass

# Compute the XML file path
xml_file = os.path.join(root, "sample", "big.xml")

t1 = time.time()
count = 30
for i in range(count) :
    DelegateHandler = JPackage("jpype.xml").DelegateHandler
    dh = DelegateHandler(None, None,
                         JProxy("org.xml.sax.ContentHandler",
                                inst=ContentHandler()),
                         None)

    build = javax.xml.parsers.SAXParserFactory.newInstance().newSAXParser()
    build.parse(xml_file, dh)

t2 = time.time()
print(count, "iterations in", t2 - t1, "seconds")

shutdownJVM()
