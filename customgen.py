from custom import CHARSLIST
import multiprocessing as mp
from contextlib import closing
import time
from itertools import product

def fcb(s):
    print("Current Process: ---  %s" % mp.current_process().name)
    ret = ""
    for chr in s:
        ret += chr
    with open("temp.txt", 'a') as f:
        f.write("\n\r%s" % ret)
    return

class CustomGen:

    tempPasswds = []
    outputFile = ""
    startTime = 0
    intrmdTime = 0
    totalPrinted = 0

    def __init_(self):
        self.tempPasswds = []
        self.outputFile = "tmp%d.txt" % int(time.time())

    def writePasswordsToFile(self):
        with open(self.outputFile, 'a') as f:
            f.write('\n\r'.join(self.tempPasswds))
        print '%s passwords written to %s' % (self.getCount(), self.outputFile)
        f.close()

    def getCount(self):
        return len(self.tempPasswds)

    def joinResults(self, caseStr):
        print("Currently active threads:")
        print(mp.active_children())
        ret = ""
        for chr in caseStr:
            ret += chr
        self.tempPasswds.append(ret)
        if self.getCount() > 10:
            self.writePasswordsToFile(self.outputFile, self.tempPasswds)
            print "Performance Tracking:"
            print("--- %s seconds ---" % (round(time.time() - self.intrmdTime)))
            self.intrmdTime = time.time()
            self.totalPrinted += self.getCount()
            print("Total Passwords Generated: %d" % self.totalPrinted)
            self.tempPasswds = []
        return

    # same as full but replaces ? only
    # @author Mustafa Qamar-ud-Din <m.qamaruddin@mQuBits.com>
    def replaceQuestionMarks(self, password):
        letters = []
        # place substitution sets into the letters array
        for val in password:
            if val == '?':
                letters.append(CHARSLIST)
            else:
                letters.append(val)
        print "Multiprocessing Initialized"
        print "# of CPUs: %d" % mp.cpu_count()
        print "Intermediate Pause Activated"

        self.startTime = time.time()
        self.intrmdTime = self.startTime
        with closing(mp.Pool()) as pool:
            pool.map(fcb, product(*letters))
            pool.terminate()
            print "Performance Tracking:"
            print("--- %s seconds ---" % (round(time.time() - self.startTime)))
            return