import time


class Algorithms:

    def __init__(self):
        pass

    def bubble_sort(self, drawData, data, timetick, frame):
        print(timetick)
        for _ in range(len(data) - 1):
            for j in range(len(data)-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    drawData(data, frame, ["#ffff00" if element == j or element ==
                             j+1 else "#8f3cb5" for element in range(len(data))])
                    time.sleep(timetick)

        drawData(data, frame, ["#ffff00" for x in range(len(data))])

    def merge_sort(self, drawData, data, timetick, frame):
        print(timetick)
        self.merge_sort_alg(drawData, 0, len(data)-1, data, timetick, frame)

    def merge_sort_alg(self, drawData, left, right, data, timetick, frame):
        if left < right:
            middle = (left + right) // 2
            self.merge_sort_alg(drawData, left, middle, data, timetick, frame)
            self.merge_sort_alg(drawData, middle+1, right,
                                data, timetick, frame)
            self.merge(drawData, left, middle, right, data, timetick, frame)
            

    def merge(self, drawData, left, middle, right, data, timetick, frame):
        left_part = data[left:middle+1]
        right_part = data[middle+1: right+1]

        left_index = right_index = data_index = 0

        for data_index in range(left, right+1):
            if left_index < len(left_part) and right_index < len(right_part):
                if left_part[left_index] <= right_part[right_index]:
                    data[data_index] = left_part[left_index]
                    left_index += 1
                else:
                    data[data_index] = right_part[right_index]
                    right_index += 1

            elif left_index < len(left_part):
                data[data_index] = left_part[left_index]
                left_index += 1
            else:
                data[data_index] = right_part[right_index]
                right_index += 1

        drawData(data, frame, ["#ffff00" if x >= left and x <=
                 right else "#8f3cb5" for x in range(len(data))])
        time.sleep(timetick)
