import time
class Algorithms:


    def  __init__(self):
             pass
    

    def bubble_sort(self, drawData, data , timetick , frame ):
          print(timetick)
          for _ in range(len(data) -1):
              for j in range(len(data)-1):
                  if data[j] > data[j+1]:
                      data[j] , data[j+1] = data[j+1], data[j]
                      drawData(data ,frame, ["#ffff00" if element == j or element == j+1 else "#8f3cb5" for element in range(len(data))] )
                      time.sleep(timetick)

          drawData(data, frame , ["#ffff00" for x in range(len(data))])


