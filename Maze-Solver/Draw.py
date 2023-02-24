import os

class Create_Graph:
    def __init__(self,path,walls,dimension,properties,explored):
        self.path = path
        self.length = len(path)
        self.walls = walls
        self.dimension = dimension
        self.properties = properties
        self.seen = []
        for i in explored:
            if i not in path:
                self.seen.append(i)
        self.path_string = ""
        for i in path:
            temp = str(i)+" --> "
            self.path_string += temp
        else:
             self.path_string = self.path_string[:-3]      
        self.doc = []
        return None
    def Create_script(self):
        #doc = self.doc
        doc = [
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        "<title>Python Maze Solver</title>",
        "</head>",
        "<body>",
        "<h1>Maze solver using Python</h1>",
        "<p>Method used : ",
        self.properties["method"],
        "</p>",
        "<p>Execution Time : ",
        self.properties["speed"],
        "</p>",
        "<p>Total Cells explored : ",
        self.properties["cost"],
        "</p>",
        "<p>Distance : ",
        str(self.length),  # type: ignore
        "</p>",
        "<table border = 1>"
        ]
        for i in range(self.dimension[0]):
            doc.append("<tr>")
            for j in range(self.dimension[1]):
                if ([i,j] in self.path) or ((i,j) in self.path):
                    doc.append("<td style='height:10px;width:10px;background-color:green;'></td>")
                elif ([i,j] in self.seen) or ((i,j) in self.seen):
                    doc.append("<td style='height:10px;width:10px;background-color:lightblue;'></td>")
                elif ([i,j] in self.walls) or ((i,j) in self.walls):
                    doc.append("<td style='height:10px;width:10px;background-color:black;'></td>")
                else:
                    doc.append("<td style='height:10px;width:10px;background-color:white;'></td>")
            doc.append("</tr>")

        doc.append("</table>")
        doc.append("<p>")
        doc.append(str("Path : "+self.path_string))
        doc.append("</p>")
        doc.append("</body></html>")

        return doc
    def get_absolute_path(self):
        current = os.getcwd()
        return current

    def writefile(self):
        docc = self.Create_script()
        #print(docc)
        method = self.properties["method"]
        
        filename = self.get_absolute_path()+"\\"+"Maze_Solution"+method+".html"
        with open(filename, "w") as file:
            file.writelines(docc)
            file.close()
        os.startfile(filename)

    def graph(self):
        self.writefile()