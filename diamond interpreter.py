# underground("guess", "=", 0)
# sys.out.println("i am thinking of a number between 0 to 100")
# sys.in.scaninput()
# changevar("guess","=","#input")
# tostring("guess")
# if "$guess" < 34
# sys.out.println("Too low!")
# }
# if "$guess" > 34 {
# sys.out.println("Too high!")
# }
# if "$guess" == 34 {
# sys.out.println("it is 34!")
# }
def readline(r="arg", line=""):
    command = line.split("(")[0]
    args = line.split("(")[1].split(")")[0].split(",")
    if r == "arg":
        return args
    elif r == "cmd":
        return command
def interpret(code):
    line = 0
    def error(error="this command is not available at the moment", l=line):
        print(f"An error has occured at line {l}: {error}")
    def initial(args):
        if args[1] == "=":
            variables[0] = variables[2]
    def println(args):
        print(args[0])
    def cvar(args):
        if variables[args[0]].startswith("#"):
            error("This variable cannot be changed by user's desire.", l=line)
        elif args[0] in variables:
            if args[1] == "=":
                variables[args[0]] = variable[args[2]]
        else:
            error("Variable does not exist (Use the \"underground()\" command to declare new variables.)", l=line)
    variables = {
        "#version": "1.0 release"
        "#input": "?"
    }
    commands = {
        "underground": initial,
        "sys.out.println": println,
        "changevar":cvar,
        "if":error,
        "notif":error,
        "sys.in.scaninput": error,
        "repeatuntil": error,
        "sys.out.printvar": error,
    }
