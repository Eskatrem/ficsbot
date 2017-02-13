from threading import Timer
from time import time


class VoteTimer:
    def __init__(self, duration, callback):
        self.running = False
        self.paused = False
        self.ended = False

        self.timeStarted = None
        self.timePaused = None

        self.duration = duration
        self.callback = callback
        self.timer = Timer(self.duration, self.callback)

    def start(self):
        if not self.running:
            self.running = True
            self.paused = False

            self.timeStarted = time()
            self.timer.start()

    def pause(self):
        if not self.paused and self.running:
            self.running = False
            self.paused = True

            self.timePaused = time()
            self.timer.cancel()

            self.duration -= self.timePaused - self.timeStarted
            self.timer = Timer(self.duration, self.callback)

    def resume(self):
        if self.paused and not self.running:
            self.start()

    def stop(self):
        if self.running or self.paused:
            self.timer.cancel()
            self.running = False
            self.paused = False
            self.ended = True
        else:
            self.running = False
            self.paused = False
            self.ended = True
            self.callback()

    def gettimeleft(self):
        if self.running:
            return self.duration - (time() - self.timeStarted)
        elif self.ended:
            return 0
        else:
            return self.duration

    def settime(self, time):
        if self.running:
            self.pause()

            self.duration = time
            self.timer = Timer(self.duration, self.callback)

            self.resume()
        elif not self.ended:
            self.duration = time
            self.timer = Timer(self.duration, self.callback)

    def addtime(self, time):
        self.settime(self.gettimeleft() + time)

    def removetime(self, time):
        self.addtime(-time)

    def isrunning(self):
        return self.running

    def ispaused(self):
        return self.paused

    def hasended(self):
        return self.ended
