 #!/usr/bin/python
from datetime import datetime

class Camera:
    def __init__(self, modelName):
        self.name = modelName
        self.startStatTime = ''
        self.nonRestartCount = 0
        self.timeSliceData = []


    def setStartStatTime(self, datetime):
        self.startStatTime = datetime

    def loadTimeSliceData(self, filepath):
        fmt = '%Y-%m-%d %H:%M:%S'
        with open(filepath) as text:
            for eachLine in text:
                #Mon Jan 25 08:29:13 UTC 2016
                YY = eachLine.split()[5]
                MM = eachLine.split()[1]
                if MM == 'Jan':
                    MM = '01'
                else:
                    return
                DD = eachLine.split()[2]
                time = eachLine.split()[3]

                timeFmt = datetime.strptime( YY+ '-' + MM + '-' + DD + ' ' + time, fmt)
                self.timeSliceData.append(timeFmt)


    def countNonRestartTimes(self):
        idx = 0
        prevRecord = 0

        for eachRecord in self.timeSliceData:
            if eachRecord > self.startStatTime:
                if idx != 0:
                    minDiff = (eachRecord - prevRecord ).seconds/60 #convert to mins diff
                    #print 'mindiff:' + str(minDiff)
                    if minDiff > 15:
                        self.nonRestartCount = self.nonRestartCount + 1
                prevRecord = eachRecord
                idx = idx + 1



    def printInfo(self):
        print 'name:' + self.name
        print 'start stat time:' + str(self.startStatTime)
        #print 'time slice:' 
        #for timeslice in self.timeSliceData:
        #    print timeslice
        print 'nonRestart Count:' + str(self.nonRestartCount)

        print '\n'

if __name__==' __main__':
    cam = Camera('test')
    print 'cam info:'
    cam.printInfo()
    cam.countNonRestartTimes()
