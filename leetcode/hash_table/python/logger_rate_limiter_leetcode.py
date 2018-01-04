"""
https://leetcode.com/problems/logger-rate-limiter/

Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.
"""
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log = {}


    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.log and timestamp - self.log[message] < 10:
            return False
        else:
            self.log[message] = timestamp
            return True

class Logger(object):
    def __init__(self):
        self.ok = {}

    def shouldPrintMessage(self, timestamp, message):
        if timestamp < self.ok.get(message, 0):
            return False
        self.ok[message] = timestamp + 10
        return True


class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log = {}


    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.log:
            if timestamp - self.log.get(message) >= 10:
                self.log[message] = timestamp
                return True
            else:
                return False
        else:
            self.log[message] = timestamp

        return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
if __name__ == '__main__':
    logger = Logger()

    # logging string "foo" at timestamp 1
    print logger.shouldPrintMessage(1, "foo") #  returns true;

    # logging string "bar" at timestamp 2
    print logger.shouldPrintMessage(2,"bar") # returns true;

    # logging string "foo" at timestamp 3
    print logger.shouldPrintMessage(3,"foo") # returns false;

    # logging string "bar" at timestamp 8
    print logger.shouldPrintMessage(8,"bar") # returns false;

    # logging string "foo" at timestamp 10
    print logger.shouldPrintMessage(10,"foo") # returns false;

    # logging string "foo" at timestamp 11
    print logger.shouldPrintMessage(11,"foo") # returns true;
