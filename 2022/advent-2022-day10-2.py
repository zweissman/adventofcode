DATA_TEST = ["noop","addx 3","addx -5"]
DATA_TEST2 = ["addx 15","addx -11","addx 6","addx -3","addx 5","addx -1","addx -8","addx 13","addx 4","noop","addx -1","addx 5","addx -1","addx 5","addx -1","addx 5","addx -1","addx 5","addx -1","addx -35","addx 1","addx 24","addx -19","addx 1","addx 16","addx -11","noop","noop","addx 21","addx -15","noop","noop","addx -3","addx 9","addx 1","addx -3","addx 8","addx 1","addx 5","noop","noop","noop","noop","noop","addx -36","noop","addx 1","addx 7","noop","noop","noop","addx 2","addx 6","noop","noop","noop","noop","noop","addx 1","noop","noop","addx 7","addx 1","noop","addx -13","addx 13","addx 7","noop","addx 1","addx -33","noop","noop","noop","addx 2","noop","noop","noop","addx 8","noop","addx -1","addx 2","addx 1","noop","addx 17","addx -9","addx 1","addx 1","addx -3","addx 11","noop","noop","addx 1","noop","addx 1","noop","noop","addx -13","addx -19","addx 1","addx 3","addx 26","addx -30","addx 12","addx -1","addx 3","addx 1","noop","noop","noop","addx -9","addx 18","addx 1","addx 2","noop","noop","addx 9","noop","noop","noop","addx -1","addx 2","addx -37","addx 1","addx 3","noop","addx 15","addx -21","addx 22","addx -6","addx 1","noop","addx 2","addx 1","noop","addx -10","noop","noop","addx 20","addx 1","addx 2","addx 2","addx -6","addx -11","noop","noop","noop"]
DATA = ["noop","noop","addx 5","addx 1","addx 10","addx -4","noop","addx -1","noop","addx 5","addx -5","addx 9","addx 2","addx -15","addx 18","addx 8","addx -2","noop","addx -18","addx 21","addx 1","addx -37","addx 27","addx -24","addx 2","addx 5","addx -7","addx 26","addx -16","addx 2","addx 5","addx -15","noop","addx 20","addx 2","addx 4","addx -3","addx 2","noop","addx 3","addx 2","addx 5","addx -40","addx 2","addx 33","addx -30","addx 5","addx 5","addx 17","addx -19","addx 2","addx 5","addx 20","addx -16","addx 3","addx -2","addx 7","noop","addx -2","addx 5","addx 2","addx 3","addx -2","addx -38","addx 5","addx 2","addx 1","addx 15","addx -8","noop","addx -2","addx 4","addx 2","addx 4","addx -2","noop","addx 6","addx 2","addx -1","addx 4","noop","addx 1","addx 4","noop","noop","noop","addx -37","addx 5","addx 2","addx 22","addx -17","addx -2","noop","addx 3","addx 2","noop","addx 3","addx 2","noop","noop","noop","addx 5","addx 5","addx 2","addx 3","noop","addx 2","addx -23","addx 2","addx -14","noop","addx 29","addx -26","noop","addx 8","noop","noop","noop","addx -9","addx 11","addx 5","addx 2","noop","addx 1","noop","noop","addx 5","noop","noop","addx 2","noop","addx 3","addx 2","addx -2","noop","noop","noop"]

X = 1
Y = 0
#SCREEN = [['.']* 40 for i in range(6)]
SCREEN = ""

def run(data, debug=False):
    global X, Y, SCREEN
    results = 0
    run_command = None
    run_command_arg = None
    clock = 1
    next_pop = 1
    
    
    while True:
        if debug: print(f"CLOCK={clock} X={X} next={next_pop}")
            
        
        if next_pop == clock:
            if len(data) == 0:
                break
            command = data.pop(0)
            if debug: print("\t\t--> " + command)
        
            
            if command == "noop":
                run_command = None
                pop = clock + 1
            elif command.startswith("addx"):
                pop = clock + 2
                _, arg = command.split(" ")
                run_command = addx
                run_command_arg = int(arg)
            else:
                print(f"Unknown command {command}")
        elif next_pop < clock:
            print("We missed it")
        
        if X - 1 <= (clock - 1) % 40 <= X + 1:
            SCREEN += "#"
        else:
            SCREEN += "."
        show(debug)

        if clock % 40 == 0:
            a = 1



        clock += 1
        
        if next_pop == clock and run_command and run_command_arg:
            run_command(run_command_arg, debug)

        next_pop = pop

    return results

def addx(arg, debug):
    global X
    
    if debug: print(f"\t$ addx({arg})  X {X} --> {X+arg}")
    X += arg

def show(debug):
    start = 0
    while True:
        print(SCREEN[start:start+40])
        start += 40
        if len(SCREEN) < start:
            break
    
    
if __name__ == "__main__":
#    results = run(DATA_TEST, debug=True)
#    results = run(DATA_TEST2, debug=True)
    results = run(DATA, debug=True)
    print("ANSWER:", results)
