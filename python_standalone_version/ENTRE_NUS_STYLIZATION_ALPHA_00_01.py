# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ENTRE_NUS_STYLIZATION_ALPHA_00_01.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

# BACKEND
import cv2
import numpy as np 
import matplotlib.pyplot as plt 
from random import seed
from random import randint

# IMPORT FUNCTION
from exrSequenceBathcProcessing import sequenceBatch as seqBatch
from ENTRE_NUS_STYLIZATION_backend import entreNusStylization as enStylize


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 531)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1011, 511))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.exrTitle = QtWidgets.QLabel(self.tab_1)
        self.exrTitle.setGeometry(QtCore.QRect(10, 10, 241, 21))

        # EXR Render section
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.exrTitle.setFont(font)
        self.exrTitle.setObjectName("exrTitle")
        self.exrPick = QtWidgets.QPushButton(self.tab_1)
        self.exrPick.setGeometry(QtCore.QRect(10, 30, 181, 23))
        self.exrPick.setObjectName("exrPick")
        self.exrPath = QtWidgets.QLabel(self.tab_1)
        self.exrPath.setGeometry(QtCore.QRect(210, 30, 781, 21))
        self.exrPath.setObjectName("exrPath")
        self.brushTitle = QtWidgets.QLabel(self.tab_1)
        self.brushTitle.setGeometry(QtCore.QRect(10, 70, 331, 21))

        # Brush exr section
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.brushTitle.setFont(font)
        self.brushTitle.setObjectName("brushTitle")
        self.brushPick = QtWidgets.QPushButton(self.tab_1)
        self.brushPick.setGeometry(QtCore.QRect(10, 90, 181, 23))
        self.brushPick.setObjectName("brushPick")
        self.brushPath = QtWidgets.QLabel(self.tab_1)
        self.brushPath.setGeometry(QtCore.QRect(220, 90, 781, 21))
        self.brushPath.setObjectName("brushPath")
        

        # Adding the brush size input
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.brushSize_Title = QtWidgets.QLabel(self.tab_1)
        self.brushSize_Title.setGeometry(QtCore.QRect(250, 210, 61, 21))
        self.brushSize_Title.setObjectName("brushSize_Title")
        self.brushSize_Box = QtWidgets.QSpinBox(self.tab_1)
        self.brushSize_Box.setGeometry(QtCore.QRect(310, 210, 51, 22))
        self.brushSize_Box.setMinimum(2)
        self.brushSize_Box.setMaximum(2000)
        self.brushSize_Box.setProperty("value", 8)
        self.brushSize_Box.setObjectName("brushSize_Box")
        self.tabWidget.addTab(self.tab_1, "")
        

        # Grid density section
        self.gridTitle = QtWidgets.QLabel(self.tab_1)
        self.gridTitle.setGeometry(QtCore.QRect(10, 130, 331, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gridTitle.setFont(font)
        self.gridTitle.setObjectName("gridTitle")
        self.grid_density_box = QtWidgets.QSpinBox(self.tab_1)
        self.grid_density_box.setGeometry(QtCore.QRect(10, 150, 201, 22))
        self.grid_density_box.setMinimum(4)
        self.grid_density_box.setMaximum(500)
        self.grid_density_box.setObjectName("grid_density_box")
        self.offset_box = QtWidgets.QSpinBox(self.tab_1)
        self.offset_box.setGeometry(QtCore.QRect(10, 210, 201, 22))
        self.offset_box.setMinimum(0)
        self.offset_box.setMaximum(500)
        self.offset_box.setProperty("value", 0)
        self.offset_box.setObjectName("offset_box")
        self.offsetTitle = QtWidgets.QLabel(self.tab_1)
        self.offsetTitle.setGeometry(QtCore.QRect(10, 190, 331, 21))

        # brush position offset section
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.offsetTitle.setFont(font)
        self.offsetTitle.setObjectName("offsetTitle")
        self.pushButton = QtWidgets.QPushButton(self.tab_1)
        self.pushButton.setGeometry(QtCore.QRect(20, 450, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 450, 141, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.sequenceTitle = QtWidgets.QLabel(self.tab_1)
        self.sequenceTitle.setGeometry(QtCore.QRect(10, 250, 581, 21))

        # Image Sequence option - not working at all for the moment
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sequenceTitle.setFont(font)
        self.sequenceTitle.setObjectName("sequenceTitle")
        self.checkBox = QtWidgets.QCheckBox(self.tab_1)
        self.checkBox.setGeometry(QtCore.QRect(20, 280, 161, 17))
        self.checkBox.setObjectName("checkBox")
        
        # Sequence min and max
        self.spinBox = QtWidgets.QSpinBox(self.tab_1)
        self.spinBox.setEnabled(False)
        self.spinBox.setGeometry(QtCore.QRect(90, 340, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(500000)
        self.spinBox.setProperty("value", 100)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_1)
        self.spinBox_2.setEnabled(False)
        self.spinBox_2.setGeometry(QtCore.QRect(90, 310, 42, 22))
        self.spinBox_2.setMinimum(0)
        self.spinBox_2.setMaximum(499999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.sequenceTitle_2 = QtWidgets.QLabel(self.tab_1)
        self.sequenceTitle_2.setGeometry(QtCore.QRect(20, 310, 71, 21))
        
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sequenceTitle_2.setFont(font)
        self.sequenceTitle_2.setObjectName("sequenceTitle_2")
        self.sequenceTitle_3 = QtWidgets.QLabel(self.tab_1)
        self.sequenceTitle_3.setGeometry(QtCore.QRect(20, 340, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sequenceTitle_3.setFont(font)
        self.sequenceTitle_3.setObjectName("sequenceTitle_3")
        self.tabWidget.addTab(self.tab_1, "")
        

        # Help section
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setAutoFillBackground(False)
        self.tab_2.setObjectName("tab_2")
        self.help_title_header = QtWidgets.QLabel(self.tab_2)
        self.help_title_header.setGeometry(QtCore.QRect(30, 30, 931, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.help_title_header.setFont(font)
        self.help_title_header.setObjectName("help_title_header")
        self.help_title_footer = QtWidgets.QLabel(self.tab_2)
        self.help_title_footer.setGeometry(QtCore.QRect(10, 460, 481, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.help_title_footer.setFont(font)
        self.help_title_footer.setObjectName("help_title_footer")
        self.help_title_1 = QtWidgets.QLabel(self.tab_2)
        self.help_title_1.setGeometry(QtCore.QRect(60, 70, 651, 31))
        self.help_title_1.setObjectName("help_title_1")
        self.help_title_3 = QtWidgets.QLabel(self.tab_2)
        self.help_title_3.setGeometry(QtCore.QRect(60, 190, 651, 31))
        self.help_title_3.setObjectName("help_title_3")
        self.help_title_4 = QtWidgets.QLabel(self.tab_2)
        self.help_title_4.setGeometry(QtCore.QRect(140, 250, 191, 31))
        self.help_title_4.setObjectName("help_title_4")
        self.help_title_5 = QtWidgets.QLabel(self.tab_2)
        self.help_title_5.setGeometry(QtCore.QRect(140, 220, 191, 31))
        self.help_title_5.setObjectName("help_title_5")
        self.help_title_2 = QtWidgets.QLabel(self.tab_2)
        self.help_title_2.setGeometry(QtCore.QRect(60, 110, 651, 31))
        self.help_title_2.setObjectName("help_title_2")
        self.help_title_2_complement = QtWidgets.QLabel(self.tab_2)
        self.help_title_2_complement.setGeometry(QtCore.QRect(140, 140, 391, 31))
        self.help_title_2_complement.setObjectName("help_title_2_complement")
        self.help_title_6 = QtWidgets.QLabel(self.tab_2)
        self.help_title_6.setGeometry(QtCore.QRect(60, 290, 731, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.help_title_6.setFont(font)
        self.help_title_6.setObjectName("help_title_6")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHow_this_works = QtWidgets.QAction(MainWindow)
        self.actionHow_this_works.setObjectName("actionHow_this_works")
        self.actionFile_requisites = QtWidgets.QAction(MainWindow)
        self.actionFile_requisites.setObjectName("actionFile_requisites")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ####     Defining what happens exactly when you click
        
        # Updating Exr path when clicking on exr pick button
        self.exrPick.clicked.connect(self.exrPicking)
        
        # Updating brush path when clicking on brush pick button
        self.brushPick.clicked.connect(self.brushPicking)
        
        # Updating the brush size value on change
        self.grid_density_box.valueChanged.connect(self.updateGridDensity)
        
        # Updating the brush offset value on value change
        self.offset_box.valueChanged.connect(self.updateBrushOffset)
        
        # Updating the brush size
        self.brushSize_Box.valueChanged.connect(self.updateBrushSize)
        
        # Clicking on the preview button
        self.pushButton.clicked.connect(self.previewButton)

        # Clicking on the computeAll button
        self.pushButton_2.clicked.connect(self.computeButton)
        
        # Activating the sequence start and end toggles on the image sequence click
        self.checkBox.stateChanged.connect(self.sequenceChecked)
        
        # Updating the min sequence
        self.spinBox_2.valueChanged.connect(self.sequenceMin)
        
        # Updating the max sequence
        self.spinBox.valueChanged.connect(self.sequenceMax)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exrTitle.setText(_translate("MainWindow", "1 - Pick the .exr you want to customize:"))
        self.exrPick.setText(_translate("MainWindow", "Pick render pass.exr"))
        self.exrPath.setText(_translate("MainWindow", "Path to your rendered exr"))
        self.brushTitle.setText(_translate("MainWindow", "2 - Pick the brush.exr you want to use for customization:"))
        self.brushPick.setText(_translate("MainWindow", "Pick brush.exr"))
        self.brushPath.setText(_translate("MainWindow", "Path to your brush exr"))
        #### Adding the brush size settings
        self.brushSize_Title.setText(_translate("MainWindow", "Brush Size:"))
        self.gridTitle.setText(_translate("MainWindow", "3 - Input the grid density you want (Brush spacing)"))
        self.offsetTitle.setText(_translate("MainWindow", "4 - Input the brush position randomness you want"))
        self.pushButton.setText(_translate("MainWindow", "Preview"))
        self.pushButton_2.setText(_translate("MainWindow", "Compute All Frames"))
        self.sequenceTitle.setText(_translate("MainWindow", "4 - If you are working with an image sequence check the box and indicate the min and max frames:"))
        self.checkBox.setText(_translate("MainWindow", "Image Sequence Toggle"))
        self.sequenceTitle_2.setText(_translate("MainWindow", "first frame :"))
        self.sequenceTitle_3.setText(_translate("MainWindow", "last frame :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Exr_Customization"))
        self.tab_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Infos</p></body></html>"))
        self.help_title_header.setText(_translate("MainWindow", "Tool developped by Teillet Martin"))
        self.help_title_footer.setText(_translate("MainWindow", "If you need additionnal help - contact martin.teillet@hotmail.fr"))
        self.help_title_1.setText(_translate("MainWindow", "- In order for the stylization computation to work, you absolutely need to have 32 bits exrs in both the render and the brush inputs"))
        self.help_title_3.setText(_translate("MainWindow", "- If you are working with an image sequence - make sure the filenames follow this convention :"))
        self.help_title_4.setText(_translate("MainWindow", "Example: rawRender.0001.exr"))
        self.help_title_5.setText(_translate("MainWindow", "exrName.<f4>.exr"))
        self.help_title_2.setText(_translate("MainWindow", "- Sometimes errors can occur if the offset value is set too high and causes brushes to try to be drawn outside of the image borders"))
        self.help_title_2_complement.setText(_translate("MainWindow", "In this case try to either lower the brush draw size or the offset value"))
        self.help_title_6.setText(_translate("MainWindow", "It is recommended you use the PREVIEW option before launching the computation on all frames !"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Infos"))
        self.actionHow_this_works.setText(_translate("MainWindow", "How this works"))
        self.actionFile_requisites.setText(_translate("MainWindow", "File requisites"))

    # Picking the EXR file
    def exrPicking(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.updateExrFile(fileName)
            exrPathString = (fileName)
            return(exrPathString)

    # Updating the EXR path
    def updateExrFile(self, fileName):
        self.exrPath.setText(fileName)
        self.exrPath.adjustSize()
        print("Updated the original exr to :")
        print(fileName)
        # Writing the path to the exr in a text file for later referencing
        outExr = open("00_ChosenExr.json", "w")
        outExr.write(fileName)
        outExr.close
        

    # Picking the brush file
    def brushPicking(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.updateBrushFile(fileName)
            return(fileName)

    # Updating the brush path
    def updateBrushFile(self, fileName):
        self.brushPath.setText(fileName)
        self.brushPath.adjustSize()
        print("Updated the brush exr to:")
        print(fileName)
        # Writing the path to the brush in a text file for later referencing
        outBrush = open("01_ChosenBrush.json", "w")
        outBrush.write(fileName)
        outBrush.close

    def updateGridDensity(self):
        gridSize = str(self.grid_density_box.value())
        print("Updated the brush size to", gridSize)
        outGridSize = open("02_GridSpacing.json", "w")
        outGridSize.write(gridSize)
        outGridSize.close
        
    
    def updateBrushOffset(self):
        brushOffset = str(self.offset_box.value())
        print("Updated the brush offset to", brushOffset)
        outBrushOffset = open("04_BrushOffset.json", "w")
        outBrushOffset.write(brushOffset)
        outBrushOffset.close

    def updateBrushSize(self):
        brushSizeValue = str(self.brushSize_Box.value())
        print("Updated the brush size to", brushSizeValue)
        outBrushSize = open("03_BrushSize.json", "w")
        outBrushSize.write(brushSizeValue)
        outBrushSize.close
        
        
    def sequenceChecked(self):
        if self.checkBox.isChecked() == True:
            print("Image Sequence")
            self.spinBox.setEnabled(True)
            self.spinBox_2.setEnabled(True)
            outSeqCheck = open("07_seqSwitch.json", "w")
            outSeqCheck.write("YES")
            outSeqCheck.close
        else:
            print("No sequence")
            self.spinBox.setEnabled(False)
            self.spinBox_2.setEnabled(False)
            outSeqCheck = open("07_seqSwitch.json", "w")
            outSeqCheck.write("NO")
            outSeqCheck.close
            
    def sequenceMin(self):
        seqMin = str(self.spinBox_2.value())
        print("Changed sequence starting frame to:", seqMin)
        outSeqMin = open("05_seqMin.json", "w")
        outSeqMin.write(seqMin)
        outSeqMin.close
        
        
    def sequenceMax(self):
        print("Changed sequence ending frame")
        seqMax = str(self.spinBox.value())
        print("Changed sequence starting frame to:", seqMax)
        outSeqMax = open("06_seqMax.json", "w")
        outSeqMax.write(seqMax)
        outSeqMax.close
        


    def previewButton(self):
        print("Clicked preview button")
        functionPreview()
        
    
    def computeButton(self):
        print("Clicked compute all button")
        computeAllFunction()


####    BACKEND CODE    ####
    

def functionPreview():
    # Opening the data contained in the json files
    exrJson = open("00_ChosenExr.json", "r")
    exrJson = (exrJson.readline())
    brushJson = open("01_ChosenBrush.json", "r")
    brushJson = (brushJson.readline())
    gridDensityJson = open("02_GridSpacing.json", "r")
    gridDensityJson = (gridDensityJson.readline())
    brushSizeJson = open("03_BrushSize.json", "r")
    brushSizeJson = (brushSizeJson.readline())
    brushOffsetJson = open("04_BrushOffset.json", "r")
    brushOffsetJson = (brushOffsetJson.readline())
    seqMinJson = open("05_seqMin.json", "r")
    seqMinJson = (seqMinJson.readline())
    seqMaxJson = open("06_seqMax.json", "r")
    seqMaxJson = (seqMaxJson.readline())
    
    # Resuming the data before execution
    print("The chosen exr is:")
    print(exrJson)
    print("The chosen brush file is:")
    print(brushJson)
    print("The chosen brush size is:")
    print(brushSizeJson)
    print("The chosen brush offset is:")
    print(brushOffsetJson)
    print("The chosen grid size is:")
    print(gridDensityJson)
    
    previewFunction(exrJson, brushJson, brushSizeJson, brushOffsetJson, gridDensityJson)

def previewFunction(exrJson, brushJson, brushSizeJson, brushOffsetJson, gridDensityJson):
    print("Previewing the image based on your settings...")
    # Need to send the inputs to the renderPass_Stylization_backend.py
    computedIMG = enStylize(exrJson, brushJson, brushSizeJson, brushOffsetJson, gridDensityJson)
    # Display the result of the enStylize function for previewing the files
    displayIMG(computedIMG)
    # Saving the result to a file
    #writeIMGout(exrJson, computedIMG)

def computeAllFunction():
    # Opening the data contained in the json files
    exrJson = open("00_ChosenExr.json", "r")
    exrJson = (exrJson.readline())
    brushJson = open("01_ChosenBrush.json", "r")
    brushJson = (brushJson.readline())
    gridDensityJson = open("02_GridSpacing.json", "r")
    gridDensityJson = (gridDensityJson.readline())
    brushSizeJson = open("03_BrushSize.json", "r")
    brushSizeJson = (brushSizeJson.readline())
    brushOffsetJson = open("04_BrushOffset.json", "r")
    brushOffsetJson = (brushOffsetJson.readline())
    seqMinJson = open("05_seqMin.json", "r")
    seqMinJson = (seqMinJson.readline())
    seqMaxJson = open("06_seqMax.json", "r")
    seqMaxJson = (seqMaxJson.readline())
    
    # Checking if the image sequence box is ticked or not
    outSeqJson = open("07_seqSwitch.json", "r")
    outSeqJson = (outSeqJson.readline())
    
    if outSeqJson == "YES":
        seqBatch(exrJson, seqMinJson, seqMaxJson)
        exrNumber = open("00_ChosenExr.json", "r")
        count = 0
        with open("00_ChosenExr.json", 'r') as f:
            for line in f:
                count += 1
    else:
        print("No img sequence")
        count = 1
    
    #print("CALCULATING ALL OF THE IMAGES")
    computeAllImages(exrJson, brushJson, brushSizeJson, brushOffsetJson, gridDensityJson, count)
    
def computeAllImages(exrJson, brushJson, brushSizeJson, brushOffsetJson, gridDensityJson, count):
    exrJson = open("00_ChosenExr.json", "r")
    exrList = (exrJson.readlines())
    exrList = [x.strip() for x in exrList]
    print(exrList) 
    
    current = 0
    
    for i in exrList:
        exrJson = exrList[current]
        computedIMG = enStylize(exrJson, brushJson, brushSizeJson, brushOffsetJson, gridDensityJson)
        writeIMGout(exrJson, computedIMG)
        print("Saved :", exrJson)
        current += 1
    
    print("PROCCESS FINISHED")
    
    
    

# Displaying an image
def displayIMG(computedIMG):
    cv2.imshow('PREVIEW', computedIMG)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Save an image
def writeIMGout(exrJson, computedIMG):
    splittedExrPath = exrJson.split("/")
    
    current = 0
    outImgPath = []
    while current < (len(splittedExrPath)-1):
        outImgPath.append(splittedExrPath[current] + "/")
        current+=1
    # Adding the last item + Stylized in front of it to the list
    outImgPath.append("ENS_" + str(splittedExrPath[current]))
    STYLIZEDIMGPATH = ("".join(outImgPath))
    
    print("Saving file...")
    print(STYLIZEDIMGPATH)
    cv2.imwrite(str(STYLIZEDIMGPATH), computedIMG)
    

# Main execution
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
