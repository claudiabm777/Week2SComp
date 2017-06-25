# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 21:19:23 2017

@author: Asus
"""
import vtk

def test():
    
    reader =  vtk.vtkXMLImageDataReader()
    reader.SetFileName("C:/Users/Asus/Dropbox/2017-18/ScientificCompAndVisualization/Semana2/SS_2017-master/SS_2017-master/data/wind_image.vti")

    volume = vtk.vtkVolume()
    #mapper = vtk.vtkFixedPointVolumeRayCastMapper()
    mapper = vtk.vtkGPUVolumeRayCastMapper()
    mapper.SetBlendModeToMinimumIntensity();
    mapper.SetSampleDistance(0.1)
    mapper.SetAutoAdjustSampleDistances(0)
    ren = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    iRen = vtk.vtkRenderWindowInteractor()

    # Set connections
    mapper.SetInputConnection(reader.GetOutputPort());
    volume.SetMapper(mapper)
    ren.AddViewProp(volume)
    renWin.AddRenderer(ren)
    iRen.SetRenderWindow(renWin)

    # Define opacity transfer function and color functions
   

    opacityTransferFunction = vtk.vtkPiecewiseFunction()
    opacityTransferFunction.AddPoint(0.1, 1.0)
    opacityTransferFunction.AddPoint(14, 0.5)
    
    # Create transfer mapping scalar value to color
    colorTransferFunction = vtk.vtkColorTransferFunction()
    colorTransferFunction.AddRGBPoint(1.5, 1.0, 1.0, 0.0)
    colorTransferFunction.AddRGBPoint(0.5, 1.0, 0.0, 0.0)
    colorTransferFunction.AddRGBPoint(3.0, 0.0, 1.0, 0.0)
    colorTransferFunction.AddRGBPoint(6.0, 0.0, 1.0, 1.0)
    colorTransferFunction.AddRGBPoint(14.0, 0.0, 0.0, 1.0)
    # Now set the opacity and the color
    
    
    volumeProperty = vtk.vtkVolumeProperty()
    volumeProperty.SetColor(colorTransferFunction)
    volumeProperty.SetScalarOpacity(opacityTransferFunction)
    volumeProperty.ShadeOff()
    volumeProperty.SetInterpolationTypeToLinear()
    
    volume.SetProperty(volumeProperty)
    
    renderer = vtk.vtkRenderer()
    renderer.SetBackground(0.5, 0.5, 0.5)
    renderer.AddVolume(volume)
    renderer.ResetCamera()
    
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetSize(500, 500)
    renderWindow.Render()
    
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renderWindow)
    iren.Start()

    #iRen.Start()
test()