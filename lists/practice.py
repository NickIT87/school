import array

zodiac = array.array(
    'u', 
    ['\u26CE', # змееносец
     '\u2648', '\u2649', '\u264A', 
     '\u264B', '\u264C', '\u264D', 
     '\u264E', '\u264F', '\u2650', 
     '\u2651', '\u2652', '\u2653',]
)

for z in zodiac:
    print(z)