from voteTimer import VoteTimer
from util.log import Log


class Vote:
    def __init__(self, duration, changeable, priority, callback, log=Log()):
        self._id = "id"

        self.votes = {}
        self.playerVotes = {}

        self.running = False
        self.paused = False
        self.ended = False

        self.duration = duration
        self.changeable = changeable
        self.priority = priority
        self.callback = callback
        self.timer = VoteTimer(self.duration, self.end)

        self.log=log

    def start(self):
        self.timer.start()

    def pause(self):
        self.timer.pause()

    def resume(self):
        self.timer.resume()

    def stop(self):
        self.timer.stop()

    def gettimeleft(self):
        return self.timer.gettimeleft()

    def settime(self, time):
        self.timer.settime(time)

    def addtime(self, time):
        self.timer.addtime(time)

    def removetime(self, time):
        self.timer.removetime(time)

    def addvote(self, vote, player):
        if not self.timer.isrunning(): return

        if player in self.playerVotes:
            if self.playerVotes[player] == vote:
                # No need to update
                print("[VOTE]: Player {0} already voted for this option".format(player))
                return
            if self.changeable:
                # Delete users old vote & continue
                _oldVote = self.playerVotes[player]
                self.removevote(_oldVote, player)
            else:
                # User can not update vote
                print("[VOTE]: Player {0} already voted".format(player))
                return

        # Register new vote
        if vote in self.votes:
            self.votes[vote] += 1
        else:
            self.votes[vote] = 1

        if player not in self.playerVotes:
            self.playerVotes[player] = vote

        print("[VOTE]: Added 1 vote to {0}".format(vote))

    def removevote(self, vote, player):
        if not self.timer.isrunning(): return

        if player in self.playerVotes:
            if self.playerVotes[player] == vote:
                if vote in self.votes:
                    if self.votes[vote] > 1:
                        # decrement vote
                        self.votes[vote] -= 1
                    else:
                        # completly remove vote
                        del self.votes[vote]

                print("[VOTE]: Removed 1 vote from {0}".format(vote))

                # delete player from voterlist
                del self.playerVotes[player]
                print("[VOTE]: Removed {0} from list".format(player))

    def clearvotes(self):
        # del self.votes
        # del self.playerVotes
        self.votes = {}
        self.playerVotes = {}

    def get_best(self):
        if not bool(self.votes): return

        _sortedList = sorted(self.votes, key=self.votes.get, reverse=True)
        _highest = self.votes[_sortedList[0]]
        _voteResult = {}

        # check for highest options with same number of votes
        for vote in _sortedList:
            _result = self.votes[vote]
            if _result == _highest:
                _voteResult[vote] = _result
            else:
                return _voteResult

        return _voteResult

    def end(self):
        self.callback(self.get_best())
