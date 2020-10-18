def sumIntervals(intervals):
    summation = 0
    for j in range(len(intervals)):
        try:
            if any(intervals[j: ] < intervals[j][0]:
                summation += intervals[j][1] - intervals[i][0]
                intervals.pop(i)
                intervals.pop(j)
            else:
                summation += intervals[i][1] - intervals[i][0]
        except:
            summation += intervals[i][1] - intervals[i][0]
    return summation

s = sumIntervals( [
   [1,4],
   [7, 10],
   [3, 5]
] )

print(s)
