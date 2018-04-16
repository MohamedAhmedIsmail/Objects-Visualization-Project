import tkinter
import tkinter as tk
from tkinter import *
import vtk
class Design:
    def __init__(self):
        self.root=tkinter.Tk()
        self.root.geometry("500x300")
        self.items()
        self.iren=vtk.vtkRenderWindowInteractor()
        self.x=0.05
        self.y=1
        self.red=0.05
        self.green=0.05
        self.blue=0.05
        self.arry1=[]
        self.arry2=[]
        self.irenn
        self.changeSetting
        self.tooth=vtk.vtkActor()
        self.heart=vtk.vtkActor()
        self.posx=0
        self.posy=0
        self.root.mainloop()
    def items(self):
        labl1=Label(self.root,text="GUI VTK",font=(32)).grid(row=0,column=15)
        btn1=tkinter.Button(self.root,text="Load Project",command=self.irenn).grid(row=1,column=15)
        labl2=Label(self.root,text="Settings:",font=(28)).grid(row=2,column=10)
        labl3=Label(self.root,text="1-Increase Opacity Of the tooth press up button",font=(28)).grid(row=3,column=15)
        labl4=Label(self.root,text="2-Decrease Opacity of the tooth press down button",font=(28)).grid(row=4,column=15)
        labl5=Label(self.root,text="3-Increase Opacity of the heart press left button",font=(28)).grid(row=5,column=15)
        labl6=Label(self.root,text="4-Decrease Opacity of the heart press right button",font=(28)).grid(row=6,column=15)
        
    def changeSetting(self,obj,ev):
        key=obj.GetKeySym()
        if key=="Up":    
            self.tooth.GetProperty().SetOpacity(self.x)
            self.arry1.append(self.x)
            print("The Value of Opacity in tooth: ",self.x)
            self.x+=0.05
        elif key=='Down' and self.x>=0.05:
            self.tooth.GetProperty().SetOpacity(self.x)
            self.arry1.append(self.x)
            print("The Value of Opacity in tooth: ",self.x)
            self.x-=0.05
        elif key=="Right":
            self.heart.GetProperty().SetOpacity(self.y)
            self.arry2.append(self.y)
            print("The Value of Opacity in heart: ",self.y)
            self.y+=0.05
        elif key=="Left" and self.y>=0.05:
            self.heart.GetProperty().SetOpacity(self.y)
            self.arry2.append(self.y)
            print("The Value of Opacity in heart: ",self.y)
            self.y-=0.05
        elif key=="j":
            self.tooth.GetProperty().SetColor(self.red,self.green,self.blue)
            self.heart.GetProperty().SetColor(self.red,self.green,self.blue)
            self.red+=0.05
        elif key=="u":
            self.tooth.GetProperty().SetColor(self.red,self.green,self.blue)
            self.heart.GetProperty().SetColor(self.red,self.green,self.blue)
            self.red-=0.05
        elif key=="k":
            self.tooth.GetProperty().SetColor(self.red,self.green,self.blue)
            self.heart.GetProperty().SetColor(self.red,self.green,self.blue)
            self.green+=0.05
        elif key=="i":
            self.tooth.GetProperty().SetColor(self.red,self.green,self.blue)
            self.heart.GetProperty().SetColor(self.red,self.green,self.blue)
            self.green-=0.05
        elif key=="l":
            self.tooth.GetProperty().SetColor(self.red,self.green,self.blue)
            self.heart.GetProperty().SetColor(self.red,self.green,self.blue)
            self.blue+=0.05
        elif key=="o":
            self.tooth.GetProperty().SetColor(self.red,self.green,self.blue)
            self.heart.GetProperty().SetColor(self.red,self.green,self.blue)
            self.blue-=0.05
        elif key=="a":
            self.tooth.SetPosition(self.posx,0,0)
            self.heart.SetPosition(self.posx,0,0)
            self.posx+=0.01
            self.iren.Render()
        elif key=="d":
            self.tooth.SetPosition(self.posx,0,0)
            self.heart.SetPosition(self.posx,0,0)
            self.posx-=0.01
            self.iren.Render()
        elif key=="t":
            self.tooth.SetPosition(0,self.posx,0)
            self.heart.SetPosition(0,self.posy,0)
            self.posy+=0.01
            self.iren.Render()
        elif key=="g":
            self.tooth.SetPosition(0,self.posy,0)
            self.heart.SetPosition(0,self.posy,0)
            self.posy-=0.01
            self.iren.Render()
            
        self.iren.Render() 
    def irenn(self):
        inputFileName = "C:/Users/MohamedIsmail/Desktop/tooth.vtk"
        inputFileName2= "C:/Users/MohamedIsmail/Desktop/heart.vtk"
        reader1 = vtk.vtkStructuredPointsReader()
        reader1.SetFileName(inputFileName)
        reader1.Update()
        reader2=vtk.vtkStructuredPointsReader()
        reader2.SetFileName(inputFileName2)
        reader2.Update()
        isoLevel = 126
        
        transform=vtk.vtkTransform()
        transform.Scale(3,3,3)
        transform.Translate(40,2,2)
        transformFilter=vtk.vtkTransformFilter()
        transformFilter.SetInputConnection(reader2.GetOutputPort())
        transformFilter.SetTransform(transform)
        heartExtractor=vtk.vtkContourFilter()
        heartExtractor.SetInputConnection(transformFilter.GetOutputPort())
        heartExtractor.SetValue(0,isoLevel)
        heartNormals=vtk.vtkPolyDataNormals()
        heartNormals.SetInputConnection(heartExtractor.GetOutputPort())
        #heartNormals.SetFeatureAngle(30.0)
        heartStripper=vtk.vtkStripper()
        heartStripper.SetInputConnection(heartNormals.GetOutputPort())
        heartMapper = vtk.vtkPolyDataMapper()
        heartMapper.SetInputConnection(heartStripper.GetOutputPort())
        heartMapper.ScalarVisibilityOff()
        #heart=vtk.vtkActor()
        self.heart.GetProperty().SetOpacity(1)
        self.heart.SetMapper(heartMapper)
        self.heart.GetProperty()
        
        outlineDataHeart=vtk.vtkOutlineFilter()
    
        outlineDataHeart.SetInputConnection(transformFilter.GetOutputPort())
        mapOutlineHeart=vtk.vtkPolyDataMapper()
        mapOutlineHeart.SetInputConnection(outlineDataHeart.GetOutputPort())
        outlineHeart = vtk.vtkActor()
        outlineHeart.SetMapper(mapOutlineHeart)
        outlineHeart.GetProperty().SetColor(1, 1, 1)
        
        toothExtractor = vtk.vtkContourFilter()
        toothExtractor.SetInputConnection(reader1.GetOutputPort())
        toothExtractor.SetValue(0, isoLevel)
        toothNormals = vtk.vtkPolyDataNormals()
        toothNormals.SetInputConnection(toothExtractor.GetOutputPort())
        #toothNormals.SetFeatureAngle(60.0)
        toothStripper = vtk.vtkStripper()
        toothStripper.SetInputConnection(toothNormals.GetOutputPort())
        toothMapper = vtk.vtkPolyDataMapper()
        toothMapper.SetInputConnection(toothStripper.GetOutputPort())
        toothMapper.ScalarVisibilityOff()
        #tooth = vtk.vtkActor()
        self.tooth.GetProperty().SetOpacity(0.1)
        self.tooth.SetMapper(toothMapper)
        
        outlineDataTooth=vtk.vtkOutlineFilter()
        outlineDataTooth.SetInputConnection(reader1.GetOutputPort())
        mapOutlineTooth=vtk.vtkPolyDataMapper()
        mapOutlineTooth.SetInputConnection(outlineDataTooth.GetOutputPort())
        outlineTooth = vtk.vtkActor()
        outlineTooth.SetMapper(mapOutlineTooth)
        outlineTooth.GetProperty().SetColor(0, 0, 0)
        
        aCamera = vtk.vtkCamera()
        aCamera.SetViewUp(0, 0, 1)
        aCamera.SetPosition(0, 1, 0)
        
        ren1 = vtk.vtkRenderer()
        ren1.AddActor(outlineTooth)
        ren1.AddActor(outlineHeart)
        ren1.AddActor(self.tooth)
        ren1.AddActor(self.heart)
        ren1.SetActiveCamera(aCamera)
        ren1.ResetCamera()
        ren1.SetBackground(0.2,0.3, 1)
        ren1.SetGradientBackground(0)
        
        renWin = vtk.vtkRenderWindow()
        renWin.AddRenderer(ren1)
        renWin.SetSize(640, 480)
        
        iren = vtk.vtkRenderWindowInteractor()
        iren.SetRenderWindow(renWin)
        iren.AddObserver("KeyPressEvent",self.changeSetting)
        renWin.Render()
        iren.Initialize()    
        iren.Start()
        print("The Values of The Opacity in Tooth:")
        print(self.arry1)
        print("The Values of the Opacity in Heart:")
        print(self.arry2)
run=Design()