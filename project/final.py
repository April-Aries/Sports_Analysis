import re

########################################################

# ReadData function 

def ReadData(filename):
    # open file
    with open( filename ) as infile:
        data = infile.readlines()

    # split tab '\t'
    new = [ ]
    for e in data:
        new.append( re.split("\t+", e) )

    # remove newline '\n'
    for e in new:
        e[-1] = e[-1].replace('\n', '')

    # integer and floting point cast
    for e in new:
        for k in range( len( e ) ):
            if k == 0 or k == 1: # NAME and TEAM
                continue
            elif '-' in e[k]:
                e[k] = -1
            elif '.' in e[k]:
                e[k] = float(e[k])
            elif e[k].isdigit():
                e[k] = int(e[k])

    return new

########################################################

filename = "final_GSW.txt"
GSW_raw_data = ReadData( filename )

GSW_total_attempt = 0
GSW_far_attempt = 0
GSW_total_made = 0
GSW_far_made = 0

for e in GSW_raw_data:
    print(*e)
    GSW_total_attempt += e[6]
    GSW_far_attempt += e[7]
    GSW_total_made += e[5]
    GSW_far_made += e[8]

filename = "final_HOU.txt"
HOU_raw_data = ReadData( filename )

HOU_total_attempt = 0
HOU_far_attempt = 0
HOU_total_made = 0
HOU_far_made = 0

for e in HOU_raw_data:
    print(*e)
    HOU_total_attempt += e[6]
    HOU_far_attempt += e[7]
    HOU_total_made += e[5]
    HOU_far_made += e[8]

# Result

print( 'GSW' )
print( 'Total attempts:    ', GSW_total_attempt )
print( 'Total made:        ', GSW_total_made )
print( 'Total far attempts:', GSW_far_attempt )
print( 'Total far made:    ', GSW_far_made)
print( '---> 三分球投球數佔總投球數比例：', round( GSW_far_attempt / GSW_total_attempt, 4 ) )

print( 'HOU' )
print( 'Total attempts:    ', HOU_total_attempt )
print( 'Total made:        ', HOU_total_made )
print( 'Total far attempts:', HOU_far_attempt )
print( 'Total far made:    ', HOU_far_made)
print( '---> 三分球投球數佔總投球數比例：', round( HOU_far_attempt / HOU_total_attempt, 4 ) )

