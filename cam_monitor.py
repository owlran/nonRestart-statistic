#!/usr/bin/python
import camera
from os import listdir
from os.path import isfile, join
from datetime import datetime

def readAllFilesInDir(dirpath):
    onlyfiles = [f for f in listdir(dirpath) if isfile(join(dirpath, f))]
    return onlyfiles

if __name__=='__main__':
    #print 'time_monitor.py'

    dirpath = './camdata'
    allFiles = readAllFilesInDir(dirpath)
    #print allFiles

    fmt = '%Y-%m-%d %H:%M:%S'
    startTime = datetime.strptime('2016-01-22 18:28:00', fmt)

    for eachModel in allFiles:
        modelName = eachModel.split('.')[0]
        cam = camera.Camera(modelName)
        #print datetime.strptime('2016-01-22 18:28:00', fmt)

        cam.setStartStatTime(startTime)
        cam.loadTimeSliceData(dirpath + '/' + eachModel)
        cam.countNonRestartTimes()

        cam.printInfo()
