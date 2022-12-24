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

#LEAGUE 

## REGULAR
league_regular_year = [ '201718', '201819', '201920', '202021', '202122' ]

league_regular_near_attempt = []
league_regular_near_made = []
league_regular_middle_attempt = []
league_regular_middle_made = []
league_regular_far_attempt = []
league_regular_far_made = []

for i in range( len(league_regular_year) ):
    league_regular_filename = league_regular_year[i] + '_regular_all_all.txt'
    league_regular_raw_data = ReadFile( league_regular_filename )

    regular_near_attempt = []
    regular_near_made = []
    regular_middle_attempt = []
    regular_middle_made = []
    regular_far_attempt = []
    regular_far_made = []

    for e in range( len( league_regular_raw_data ) ):
        if e == 0:
            continue
        regular_near_attempt.append( league_regular_raw_data[e][4] )
        regular_near_made.append( league_regular_raw_data[e][3] )
        regular_middle_attempt.append( league_regular_raw_data[e][7] + league_regular_raw_data[e][10] + league_regular_raw_data[e][13] )
        regular_middle_made.append( league_regular_raw_data[e][6] + league_regular_raw_data[e][9] + league_regular_raw_data[e][12] )
        regular_far_attempt.append( league_regular_raw_data[e][16] + league_regular_raw_data[e][19] ) 
        regular_far_made.append( league_regular_raw_data[e][15] + league_regular_raw_data[e][18] )

    league_regular_near_attempt.append( regular_near_attempt )
    league_regular_near_made.append( regular_near_made )
    league_regular_middle_attempt.append( regular_middle_attempt )
    league_regular_middle_made.append( regular_middle_made )
    league_regular_far_attempt.append( regular_far_attempt ) 
    league_regular_far_made.append( regular_far_made )

    print( '※※', league_regular_filename, '※※' )
    print( 'League average near attempt:', round( sum(league_regular_near_attempt[i]) / len(league_regular_near_attempt[i]), 6 ) )
    print( 'League average near made:', round( sum(league_regular_near_made[i]) / len(league_regular_near_made[i]), 6 ) )
    print( 'League average middle attempt:', round( sum(league_regular_middle_attempt[i]) / len(league_regular_middle_attempt[i]), 6 ) )
    print( 'League average middle made:', round( sum(league_regular_middle_made[i]) / len(league_regular_middle_made[i]), 6 ) )
    print( 'League average far attempt:', round( sum(league_regular_far_attempt[i]) / len(league_regular_far_attempt[i]), 6 ) )
    print( 'League average far made:', round( sum( league_regular_far_made[i]) / len(league_regular_far_made[i]), 6 ) )
    print('\n')

print('----------------------------------------------------------\n')

## PLAYOFF
league_playoff_year = [ '201718', '201819', '201920', '202021', '202122' ]

league_playoff_near_attempt = []
league_playoff_near_made = []
league_playoff_middle_attempt = []
league_playoff_middle_made = []
league_playoff_far_attempt = []
league_playoff_far_made = []

for i in range( len(league_playoff_year) ):
    league_playoff_filename = league_playoff_year[i] + '_playoff_all_all.txt'
    league_playoff_raw_data = ReadFile( league_playoff_filename )

    playoff_near_attempt = []
    playoff_near_made = []
    playoff_middle_attempt = []
    playoff_middle_made = []
    playoff_far_attempt = []
    playoff_far_made = []

    for e in range( len( league_playoff_raw_data ) ):
        if e == 0:
            continue
        playoff_near_attempt.append( league_playoff_raw_data[e][4] )
        playoff_near_made.append( league_playoff_raw_data[e][3] )
        playoff_middle_attempt.append( league_playoff_raw_data[e][7] + league_playoff_raw_data[e][10] + league_playoff_raw_data[e][13] )
        playoff_middle_made.append( league_playoff_raw_data[e][6] + league_playoff_raw_data[e][9] + league_playoff_raw_data[e][12] )
        playoff_far_attempt.append( league_playoff_raw_data[e][16] + league_playoff_raw_data[e][19] ) 
        playoff_far_made.append( league_playoff_raw_data[e][15] + league_playoff_raw_data[e][18] )

    league_playoff_near_attempt.append( playoff_near_attempt )
    league_playoff_near_made.append( playoff_near_made )
    league_playoff_middle_attempt.append( playoff_middle_attempt )
    league_playoff_middle_made.append( playoff_middle_made )
    league_playoff_far_attempt.append( playoff_far_attempt ) 
    league_playoff_far_made.append( playoff_far_made )

    print( '※※', league_playoff_filename, '※※' )
    print( 'League average near attempt:', round( sum(league_playoff_near_attempt[i]) / len(league_playoff_near_attempt[i]), 6 ) )
    print( 'League average near made:', round( sum(league_playoff_near_made[i]) / len(league_playoff_near_made[i]), 6 ) )
    print( 'League average middle attempt:', round( sum(league_playoff_middle_attempt[i]) / len(league_playoff_middle_attempt[i]), 6 ) )
    print( 'League average middle made:', round( sum(league_playoff_middle_made[i]) / len(league_playoff_middle_made[i]), 6 ) )
    print( 'League average far attempt:', round( sum(league_playoff_far_attempt[i]) / len(league_playoff_far_attempt[i]), 6 ) )
    print( 'League average far made:', round( sum( league_playoff_far_made[i]) / len(league_playoff_far_made[i]), 6 ) )
    print('\n')

