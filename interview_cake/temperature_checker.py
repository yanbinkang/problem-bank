class TempTracker:
    def __init__(self):
        self.occurances = [0] * (111)
        self.max_occurances = 0
        self.mode = None

        self.total_numbers = 0
        self.total_sum = 0.0
        self.mean = None

        self.min_temp = None
        self.max_temp = None

    def insert(self, temperature):
        # mode
        self.occurances[temperature] += 1
        if self.occurances[temperature] > self.max_occurances:
            self.mode = temperature
            self.max_occurances = self.occurances[temperature]

        # mean
        self.total_numbers += 1
        self.total_sum += temperature
        self.mean = self.total_sum / self.total_numbers

        # min and max
        if not self.max_temp or temperature > self.max_temp:
            self.max_temp = temperature
        if not self.min_temp or temperature < self.min_temp:
            self.min_temp = temperature

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode
