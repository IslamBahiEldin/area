class Node :
    def __init__ (self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class slinkedlist :
    def __init__(self):
        self.headval=None
    def Listprint (self) :
        printval=self.headval
        while printval is not None :
            print(printval.dataval)
            printval=printval.nextval
List=slinkedlist()
List.headval=Node('MONDAY')
e2=Node('TUE.')
e3=Node('WED.')
List.headval.nextval=e2
e2.nextval=e3
List.Listprint()