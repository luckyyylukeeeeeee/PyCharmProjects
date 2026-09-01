from array import array #Vi ska importera integers
class ArrayQ:
    def __init__(self):
        self.__arrayq = array("u",[])

    def enqueue(self,data):
            return self.__arrayq.append(data)

    def dequeue(self):
        while True:
            if not self.isEmpty():
                return self.__arrayq.pop(0)
            else:
                break

    def isEmpty(self):
        if len(self.__arrayq) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.__arrayq)


q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
y = q.dequeue()
if (x == 1 and y == 2):
    print("OK")
else:
    print("FAILED")
