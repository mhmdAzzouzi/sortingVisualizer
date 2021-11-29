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

    def partition(self, data, head, tail, darwData, timeTick ,frame):
        border = head
        pivot = data[tail]
        darwData(data, frame, self.getColorArray(len(data)  , head, tail ,border, border))
        time.sleep(.025)
        for j in range(head, tail):
            if data[j] < pivot:
                # darwData(data,  frame,self.getColorArray(len(data) , head, tail ,border, j , True) )
                # time.sleep(.025)
                data[border], data[j] = data[j] , data[border]
                border+=1
            darwData(data,  frame,self.getColorArray(len(data)  , head, tail ,border, j) )
            time.sleep(.025)

        # darwData(data,  frame,self.getColorArray(len(data) , head, tail ,border, tail, True) )
        # time.sleep(.025)
        data[border], data[tail] = data[tail], data[border]
        darwData(data,  frame,self.getColorArray(len(data) , head, tail ,border, tail, True) )
        time.sleep(.025)
        return border

    def quick_sort(self,data, head, tail, drawData, timeTick ,frame):
        if head< tail:
            partitionIdx = self.partition(data, head, tail, drawData, timeTick, frame);
            self.quick_sort(data, head, partitionIdx-1 ,drawData, timeTick ,frame)
            self.quick_sort(data, partitionIdx+1, tail, drawData, timeTick , frame)
        drawData(data, frame, ["#ffff00" for x in range(len(data))])

    
    def getColorArray( self, dataLen , head, tail , border, currentIdx , isSwapping=False):
            colorArray=[]
            for i in range(dataLen):
                    if i >= head and i<=tail:
                        colorArray.append('yellow')
                    else:
                        colorArray.append('purple')

                    if i == tail:
                        colorArray[i] = 'teal'
                    elif i== border:
                        colorArray[i]='grey'
                    elif i == currentIdx:
                        colorArray[i] = 'white'
                    if isSwapping:
                        if i == border or i==currentIdx:
                            colorArray[i] = 'white'

            return colorArray
