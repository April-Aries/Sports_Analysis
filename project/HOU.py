import re

#-------------------------------------------------------------#

# ReadData function 
def ReadFile(filename):
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

#-------------------------------------------------------------#

#HOU 

## REGULAR
HOU_regular_year = [ '201718', '201819', '201920', '202021', '202122' ]

HOU_regular_near_attempt = []
HOU_regular_near_made = []
HOU_regular_middle_attempt = []
HOU_regular_middle_made = []
HOU_regular_far_attempt = []
HOU_regular_far_made = []

for i in range( len(HOU_regular_year) ):
    HOU_regular_filename = HOU_regular_year[i] + '_regular_HOU_all.txt'
    HOU_regular_raw_data = ReadFile( HOU_regular_filename )

    regular_near_attempt = []
    regular_near_made = []
    regular_middle_attempt = []
    regular_middle_made = []
    regular_far_attempt = []
    regular_far_made = []

    for e in range( len( HOU_regular_raw_data ) ):
        if e == 0:
            continue
        regular_near_attempt.append( HOU_regular_raw_data[e][4] )
        regular_near_made.append( HOU_regular_raw_data[e][3] )
        regular_middle_attempt.append( HOU_regular_raw_data[e][7] + HOU_regular_raw_data[e][10] + HOU_regular_raw_data[e][13] )
        regular_middle_made.append( HOU_regular_raw_data[e][6] + HOU_regular_raw_data[e][9] + HOU_regular_raw_data[e][12] )
        regular_far_attempt.append( HOU_regular_raw_data[e][16] + HOU_regular_raw_data[e][19] ) 
        regular_far_made.append( HOU_regular_raw_data[e][15] + HOU_regular_raw_data[e][18] )

    HOU_regular_near_attempt.append( regular_near_attempt )
    HOU_regular_near_made.append( regular_near_made )
    HOU_regular_middle_attempt.append( regular_middle_attempt )
    HOU_regular_middle_made.append( regular_middle_made )
    HOU_regular_far_attempt.append( regular_far_attempt ) 
    HOU_regular_far_made.append( regular_far_made )

    print( '※※', HOU_regular_filename, '※※' )
    print( 'HOU average near attempt:', round( sum(HOU_regular_near_attempt[i]) / len(HOU_regular_near_attempt[i]), 6 ) )
    print( 'HOU average near made:', round( sum(HOU_regular_near_made[i]) / len(HOU_regular_near_made[i]), 6 ) )
    print( 'HOU average middle attempt:', round( sum(HOU_regular_middle_attempt[i]) / len(HOU_regular_middle_attempt[i]), 6 ) )
    print( 'HOU average middle made:', round( sum(HOU_regular_middle_made[i]) / len(HOU_regular_middle_made[i]), 6 ) )
    print( 'HOU average far attempt:', round( sum(HOU_regular_far_attempt[i]) / len(HOU_regular_far_attempt[i]), 6 ) )
    print( 'HOU average far made:', round( sum( HOU_regular_far_made[i]) / len(HOU_regular_far_made[i]), 6 ) )
    print('\n')

print('----------------------------------------------------------\n')

## PLAYOFF
HOU_playoff_year = [ '201718', '201819' ]

HOU_playoff_near_attempt = []
HOU_playoff_near_made = []
HOU_playoff_middle_attempt = []
HOU_playoff_middle_made = []
HOU_playoff_far_attempt = []
HOU_playoff_far_made = []

for i in range( len(HOU_playoff_year) ):
    HOU_playoff_filename = HOU_playoff_year[i] + '_playoff_HOU_all.txt'
    HOU_playoff_raw_data = ReadFile( HOU_playoff_filename )

    playoff_near_attempt = []
    playoff_near_made = []
    playoff_middle_attempt = []
    playoff_middle_made = []
    playoff_far_attempt = []
    playoff_far_made = []

    for e in range( len( HOU_playoff_raw_data ) ):
        if e == 0:
            continue
        playoff_near_attempt.append( HOU_playoff_raw_data[e][4] )
        playoff_near_made.append( HOU_playoff_raw_data[e][3] )
        playoff_middle_attempt.append( HOU_playoff_raw_data[e][7] + HOU_playoff_raw_data[e][10] + HOU_playoff_raw_data[e][13] )
        playoff_middle_made.append( HOU_playoff_raw_data[e][6] + HOU_playoff_raw_data[e][9] + HOU_playoff_raw_data[e][12] )
        playoff_far_attempt.append( HOU_playoff_raw_data[e][16] + HOU_playoff_raw_data[e][19] ) 
        playoff_far_made.append( HOU_playoff_raw_data[e][15] + HOU_playoff_raw_data[e][18] )

    HOU_playoff_near_attempt.append( playoff_near_attempt )
    HOU_playoff_near_made.append( playoff_near_made )
    HOU_playoff_middle_attempt.append( playoff_middle_attempt )
    HOU_playoff_middle_made.append( playoff_middle_made )
    HOU_playoff_far_attempt.append( playoff_far_attempt ) 
    HOU_playoff_far_made.append( playoff_far_made )

    print( '※※', HOU_playoff_filename, '※※' )
    print( 'HOU average near attempt:', round( sum(HOU_playoff_near_attempt[i]) / len(HOU_playoff_near_attempt[i]), 6 ) )
    print( 'HOU average near made:', round( sum(HOU_playoff_near_made[i]) / len(HOU_playoff_near_made[i]), 6 ) )
    print( 'HOU average middle attempt:', round( sum(HOU_playoff_middle_attempt[i]) / len(HOU_playoff_middle_attempt[i]), 6 ) )
    print( 'HOU average middle made:', round( sum(HOU_playoff_middle_made[i]) / len(HOU_playoff_middle_made[i]), 6 ) )
    print( 'HOU average far attempt:', round( sum(HOU_playoff_far_attempt[i]) / len(HOU_playoff_far_attempt[i]), 6 ) )
    print( 'HOU average far made:', round( sum( HOU_playoff_far_made[i]) / len(HOU_playoff_far_made[i]), 6 ) )
    print('\n')

