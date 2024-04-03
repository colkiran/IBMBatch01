

glbX = 500

def fun(a, b):          # a, b are local variables
    global glbX         # do not assign any value in this line
    print(f"a + b :{a + b}")
    glbX += 250          # local variable glbX same as the global var
    print(f"glbX inside :{glbX}")

print(f"glbX before :{glbX}")

fun(10, 20)

print(f"glbX after :{glbX}")
