class DrawingApplication(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
        self.graphsCommands() = PyList()

    # Widgets and event handlers
    def builWindow(self):

        # root window
        self.master.title("Draw")

        #Menu Bar. Tearoff=0 means inseparable form the window
        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar, tearoff=0)

        def newWindow():
            theTurtle.clear()
            theTurtle.penup()
            theTurtle.goto(0,0)
            theTurtle.pendown()
            screen.update()
            self.graphicsCommands = PyList()

        fileMenu.add_command(label = "New", command = newWindow)

        # The parse function adds the content of an XML file to the sequence
        def parse(filename):
            xmldoc = xml.dom.minidom.parse(filename)

            graphicsCommandsElement = xmldoc.getElementsByTagName("GraphicsCommands")[0]

            graphicCommands = graphicsCommandsElement.getElementByTagName("Command")

            for commandElement in graphicCommands:
                print(type(commandElement))
                command = commandElement.firstChild.data.strip()
                attr = commandElement.attributes
                if command == "GoTo":
                    x = float(attr["x"].value)
                    y = float(attr["y"].value)
                    width = float(attr["width"].value)
                    color = attr["color"].value.strip()
                    cmd = GoTOCommand(x,y,width,color)

                elif command == "Circle":
                    radius = float(attr["radius"].value)
                    width = float(attr["width"].value)
                    color = att["color"].value.strip()
                    cmd = CircleCommands(radius, width, color)

                elif command == "BeginFill":
                    color = attr["color"].value.strip()
                    cmd = BeginFillCommand(color)

                elif command =="EndFill":
                    cmd = EndFillCommand()

                elif command == "PenUp":
                    cmd = PenUpCommand()

                elif command == "PenDown":
                    cmd = PenDownCommand()

                else:
                    raise RuntimeError("Unkown Command: " + command)

                self.graphicsCommands.append(cmd)

        def loadFile():

            filename = tkinter.filedialog.askopenfilename(title= "Select a Graphics File")

            newWindow()

            #
            self.graphicsCommands = PyList()

            parse(filename)
             for cmd in self.graphicsCommands:
                 cmd.draw(theTurtle)

                 # Update window
                screen.update()

        fileName.add_command(label="Load...", command = loadFile)

        def addToFile():
            filename = tkinter.filedialog.askopenfilename(title="Select a Graphic File")

            theTurtle.penup()
            theTurtle.goto(0,0)
            theTurtle.pendown()
            theTurtle.pencolor("#000000")
            theTurtle.fillcolor("#000000")
            cmd = PenUpCommand()
            self.graphicsCommands.append(cmd)
            cmd = GoToCommand(0, 0,1, "#000000")
            self.graphicsCommands.append(cmd)
            cmd = PenDownCommand()
            self.graphicsCommands.append(cmd)
            screen.update()
            parse(filename)

            for cmd in self.graphicsCommands:
                cmd.draw(theTurtle)

                screen.update()

        fileMenu.add_command(label = "Load Into---", command = addToFile)

        #
        def write(filename):
            file = open(filename, "w")
            file.write('<?xml version ="1.0" encoding = "UTF-8" standalone ="no" ?>\n')
            file.write('<GraphicsCommands>\n')

            for cmd in self.graphicsCommands:
                file.write('        ' +str(cmd) + "\n")

            file.write('</GraphicsCommands>\n')
            file.close()

    def saveFile():
        filename = tkinter.filedialog.asksaveasfilename(title = "Save Picture As...")
        write(filename)

    fileMenu.add_command(label = "Save As ...", command = saveFile)

    filename.add_command(label = "Exit", command = master.quit)

    bar.add_cascade(label = "File", Menu = fileMenu)


    # display newly created menu bar
    self.master.config(menu=bar)

    # Widgets
    canvas = tkinter.Canvas(self, width = 600, height =600)
    canvas.pack(side=tkinter.LEFT)

    # RawTurtle
    #
    theTurtle = turtle.RawTurtle(canvas)

    #
    theTurtle.shape("circle")
    screen = theTurtle.getscreen()

    # hold on screen update
    screen.tracer(0)

    # right side
    sideBar = tkinter.Frame(self, padx=5, pady=5)

    sideBar.pack(side = tkinter.RIGHT, fill=tkinter.BOTH)

    # This is
    pointLabel = tkinter.Label(sideBar, text ="width")
    poitLabel.pack()

    widthSize = tkinter.StringVar()
    widthEntry = tkinter.Entry(sideBar, textvariable = widthSize)

    widthENtry.pack()
    widthSize.set(str(1))

    radiusLabel = tkinter.Label(sideBar, text = "Radius")
    radiusLabel.pack()
    radiusSize = tkinter.StringVar()
    radiusEntry = tkinter.Entry(sideBar, textvariable = radiusSize)
    radiusSize.set(str(10))
    radiusEntry.pack()

    def circleHandler():
        #
        #
        #
        cmd = CircleCommand(float(radiusSize.get()), float(widthSize.get()), penColor.get()
                            )
        cmd.draw(theTurtle)
        self.graphicsCommand.append(cmd)

        screen.update()
        screen.listen()

    #
    #
    circleButton = tkinter.Button(sideBar, text = "Draw Circle", command = circleHandler)
    circleButton.pack(fill-tkinter.BOTH)
