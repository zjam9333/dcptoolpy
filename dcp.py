import os
import xml.etree.ElementTree as ElementTree
import argparse

class DcpTool:
    def replaceStrSpaces(self, s):
        return s.replace("\ ", " ").replace(" ", "\ ")
    
    def dcpToXml(self, input: str, output: str):
        print("Decompile from dcp file", input)
        input = self.replaceStrSpaces(input)
        output = self.replaceStrSpaces(output)
        os.system("./dcpTool -d {} {}".format(input, output))

    def xmlToDcp(self, input: str, output: str):
        print("Compile back dcp file", output)
        input = self.replaceStrSpaces(input)
        output = self.replaceStrSpaces(output)
        os.system("./dcpTool -c {} {}".format(input, output))

    def modifyXmlCameraModel(self, xmlfile: str, camera: str):
        root = ElementTree.parse(xmlfile)
        key = "UniqueCameraModelRestriction"
        print("Modify key", key)
        node = root.find(key)
        if node == None:
            return
        print("before", node.text)
        node.text = camera
        print("after", node.text)
        root.write(xmlfile)
        print("rewrite temp xml file", xmlfile)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-input", help="input dcp file", type=str, required=True)
    parser.add_argument("-deleteTmp", help="delete temp file, default true", default=True, type=bool)
    parser.add_argument("-model", help="camera model specified", type=str, required=True)
    parser.add_argument("-output", help="ouput dcp file", type=str, required=False)

    parser.parse_args()
    
    args = parser.parse_args()

    inputdcp = args.input
    pa, filename = os.path.split(inputdcp)
    tmpxml = "dcptool_tmp.xml"
    cameraModel = args.model
    outputdcp = args.output
    if outputdcp == None:
        outputdcp = "{} fixed - {}".format(cameraModel, filename)
    deleteTmp = args.deleteTmp

    c = DcpTool()
    c.dcpToXml(input=inputdcp, output=tmpxml)
    c.modifyXmlCameraModel(xmlfile=tmpxml, camera=cameraModel)
    c.xmlToDcp(input=tmpxml, output=outputdcp)
    if deleteTmp and os.path.exists(tmpxml):
        print("Delete temp file", tmpxml)
        os.remove(tmpxml)
    # os.system("rm -rf {}".format(tmpxml))



