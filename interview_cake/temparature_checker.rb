class TempTracker

  def initialize
    @total_sum = 0
    @num_temperatures = 0.0
    @max_temp = nil
    @min_temp = nil
    @max_occurances = 0
    @occurances = [0] * 111
    @mode = nil
    @mean = nil
  end

  def insert(temperature)
    @num_temperatures += 1
    @total_sum += temperature
    @mean = @total_sum / @num_temperatures

    if not @max_temp or temperature > @max_temp
      @max_temp = temperature
    end

    if not @min_temp or temperature < @min_temp
      @min_temp = temperature
    end

    @occurances[temperature] += 1
    if @occurances[temperature] > @max_occurances
      @mode = temperature
      @max_occurances = @occurances[temperature]
    end
  end


  def get_min
    @min_temp
  end

  def get_max
    @max_temp
  end

  def get_mean
    @mean
  end

  def get_mode
    @mode
  end
end



t = TempTracker.new
t.insert(1)
t.insert(6)
t.insert(3)
t.insert(1)
t.insert(3)
t.insert(3)
p t.get_max
p t.get_mean
p t.get_mode
