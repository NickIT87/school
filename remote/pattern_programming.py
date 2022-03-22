#       = GLORY  TO  UKRAINE =  
#    |            |            |
#    |\           ^           /|
#    |#\         /#\         /#|
#    |##\       /# #\       /##|
#    |# #\     /#   #\     /# #|
#    |#  #>   <#  @  #>   <#  #|
#    |# #/     \#   #/     \# #|
#    |##/       \# #/       \##|
#    |#/         \#/         \#|
#    |/          /|\          \|
#    |###//////// | \\\\\\\\###|
#    |###\\\\\\\\ | ////////###|
#    |__/        \|/        \__|
#    |_/          ^          \_|
#    |/          /#\          \|
#               /# #\           
#              <#   #>          
#               \# #/           
#                \#/            
#                 |             
#     = GLORY  TO  THE  HEROES =

WIDTH = 30
HEIGHT = 25

def line_1():
    # '   |            |            |'
    line = []
    for i in range(WIDTH+1):
        if i == 3 or i == 16 or i== 30:
            line.append('|')
        else:
            line.append(' ')    
    print(''.join(line))


def line_2():
    # '   |\           ^           /|'
    line = []
    for i in range(WIDTH+1):
        if i == 3 or i== 30:
            line.append('|')
        elif i == 4:
            line.append('\\')
        elif i == 16:
            line.append('^')
        elif i == 29:
            line.append('/')
        else:
            line.append(' ')    
    print(''.join(line))


def draw():
    line_1()
    line_2()


if __name__ == "__main__":
    print('      = GLORY  TO  UKRAINE =  ')
    draw()