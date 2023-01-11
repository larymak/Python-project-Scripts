import time

class Path_Finder:
    def __init__(self):
        self.routes = {}
        
    def Add_element(self, From, To):
        if (From and To) is not None:
            self.routes[tuple(From)] = (list(To))

    def Print(self):
        print(self.routes)

    def get_key(self, val):
        for key, value in self.routes.items():
            #print("To find :",val,"in -->",key, "-->", value)
            if val in value:
                return key

    def Trace(self,start,destination):
        Path,current = [],0
        end,start = tuple(destination),tuple(start)
        
        while current != start:
           # time.sleep(2)
            #print("start : ",start,"To : ",destination)
            current  = self.get_key(destination)
            #print(current)
            Path.insert(0,current)
            if current == None:
                break
            destination = list(current)

        else:
            Path.append(end)
            return Path
