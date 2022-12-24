import re
from matplotlib import pyplot as plt

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

# GSW

## REGULAR
GSW_regular_year = [ '201718', '201819', '201920', '202021', '202122' ]

GSW_regular_near_attempt = []
GSW_regular_near_made = []
GSW_regular_middle_attempt = []
GSW_regular_middle_made = []
GSW_regular_far_attempt = []
GSW_regular_far_made = []

for i in range( len(GSW_regular_year) ):
    GSW_regular_filename = GSW_regular_year[i] + '_regular_GSW_all.txt'
    GSW_regular_raw_data = ReadFile( GSW_regular_filename )

    regular_near_attempt = []
    regular_near_made = []
    regular_middle_attempt = []
    regular_middle_made = []
    regular_far_attempt = []
    regular_far_made = []

    for e in range( len( GSW_regular_raw_data ) ):
        if e == 0:
            continue
        regular_near_attempt.append( GSW_regular_raw_data[e][4] )
        regular_near_made.append( GSW_regular_raw_data[e][3] )
        regular_middle_attempt.append( GSW_regular_raw_data[e][7] + GSW_regular_raw_data[e][10] + GSW_regular_raw_data[e][13] )
        regular_middle_made.append( GSW_regular_raw_data[e][6] + GSW_regular_raw_data[e][9] + GSW_regular_raw_data[e][12] )
        regular_far_attempt.append( GSW_regular_raw_data[e][16] + GSW_regular_raw_data[e][19] ) 
        regular_far_made.append( GSW_regular_raw_data[e][15] + GSW_regular_raw_data[e][18] )

    GSW_regular_near_attempt.append( regular_near_attempt )
    GSW_regular_near_made.append( regular_near_made )
    GSW_regular_middle_attempt.append( regular_middle_attempt )
    GSW_regular_middle_made.append( regular_middle_made )
    GSW_regular_far_attempt.append( regular_far_attempt ) 
    GSW_regular_far_made.append( regular_far_made )

    print( '※※', GSW_regular_filename, '※※' )
    print( 'GSW average near attempt:', round( sum(GSW_regular_near_attempt[i]) / len(GSW_regular_near_attempt[i]), 6 ) )
    print( 'GSW average near made:', round( sum(GSW_regular_near_made[i]) / len(GSW_regular_near_made[i]), 6 ) )
    print( 'GSW average middle attempt:', round( sum(GSW_regular_middle_attempt[i]) / len(GSW_regular_middle_attempt[i]), 6 ) )
    print( 'GSW average middle made:', round( sum(GSW_regular_middle_made[i]) / len(GSW_regular_middle_made[i]), 6 ) )
    print( 'GSW average far attempt:', round( sum(GSW_regular_far_attempt[i]) / len(GSW_regular_far_attempt[i]), 6 ) )
    print( 'GSW average far made:', round( sum( GSW_regular_far_made[i]) / len(GSW_regular_far_made[i]), 6 ) )
    print('\n')

print('----------------------------------------------------------\n')

## PLAYOFF
GSW_playoff_year = [ '201718', '201819', '202021' ]

GSW_playoff_near_attempt = []
GSW_playoff_near_made = []
GSW_playoff_middle_attempt = []
GSW_playoff_middle_made = []
GSW_playoff_far_attempt = []
GSW_playoff_far_made = []

for i in range( len(GSW_playoff_year) ):
    GSW_playoff_filename = GSW_playoff_year[i] + '_playoff_GSW_all.txt'
    GSW_playoff_raw_data = ReadFile( GSW_playoff_filename )

    playoff_near_attempt = []
    playoff_near_made = []
    playoff_middle_attempt = []
    playoff_middle_made = []
    playoff_far_attempt = []
    playoff_far_made = []

    for e in range( len( GSW_playoff_raw_data ) ):
        if e == 0:
            continue
        playoff_near_attempt.append( GSW_playoff_raw_data[e][4] )
        playoff_near_made.append( GSW_playoff_raw_data[e][3] )
        playoff_middle_attempt.append( GSW_playoff_raw_data[e][7] + GSW_playoff_raw_data[e][10] + GSW_playoff_raw_data[e][13] )
        playoff_middle_made.append( GSW_playoff_raw_data[e][6] + GSW_playoff_raw_data[e][9] + GSW_playoff_raw_data[e][12] )
        playoff_far_attempt.append( GSW_playoff_raw_data[e][16] + GSW_playoff_raw_data[e][19] ) 
        playoff_far_made.append( GSW_playoff_raw_data[e][15] + GSW_playoff_raw_data[e][18] )

    GSW_playoff_near_attempt.append( playoff_near_attempt )
    GSW_playoff_near_made.append( playoff_near_made )
    GSW_playoff_middle_attempt.append( playoff_middle_attempt )
    GSW_playoff_middle_made.append( playoff_middle_made )
    GSW_playoff_far_attempt.append( playoff_far_attempt ) 
    GSW_playoff_far_made.append( playoff_far_made )

    print( '※※', GSW_playoff_filename, '※※' )
    print( 'GSW average near attempt:', round( sum(GSW_playoff_near_attempt[i]) / len(GSW_playoff_near_attempt[i]), 6 ) )
    print( 'GSW average near made:', round( sum(GSW_playoff_near_made[i]) / len(GSW_playoff_near_made[i]), 6 ) )
    print( 'GSW average middle attempt:', round( sum(GSW_playoff_middle_attempt[i]) / len(GSW_playoff_middle_attempt[i]), 6 ) )
    print( 'GSW average middle made:', round( sum(GSW_playoff_middle_made[i]) / len(GSW_playoff_middle_made[i]), 6 ) )
    print( 'GSW average far attempt:', round( sum(GSW_playoff_far_attempt[i]) / len(GSW_playoff_far_attempt[i]), 6 ) )
    print( 'GSW average far made:', round( sum( GSW_playoff_far_made[i]) / len(GSW_playoff_far_made[i]), 6 ) )
    print('\n')

# GRAPH

## RATE

### LEAGUE
league_regular_near_total_attempt = []
league_regular_middle_total_attempt = []
league_regular_far_total_attempt = []
league_regular_near_total_made = []
league_regular_middle_total_made = []
league_regular_far_total_made = []

for i in range( len( league_regular_near_attempt ) ):
    league_regular_near_total_attempt.append( sum( league_regular_near_attempt[i] ) )
    league_regular_near_total_made.append( sum( league_regular_near_made[i] ) )
    league_regular_middle_total_attempt.append( sum( league_regular_middle_attempt[i] ) )
    league_regular_middle_total_made.append( sum( league_regular_middle_made[i] ) )
    league_regular_far_total_attempt.append( sum( league_regular_far_attempt[i] ) )
    league_regular_far_total_made.append( sum( league_regular_far_made[i] ) )

league_regular_total_attempt = []
league_regular_total_made = []

for i in range( len( league_regular_near_total_attempt ) ):
    league_regular_total_attempt.append( league_regular_near_total_attempt[i] + league_regular_middle_total_attempt[i] + league_regular_far_total_attempt[i] )
    league_regular_total_made.append( league_regular_near_total_made[i] + league_regular_middle_total_made[i] + league_regular_far_total_made[i] )

league_regular_near_total_attempt_rate = []
league_regular_near_total_made_rate = []
league_regular_middle_total_attempt_rate = []
league_regular_middle_total_made_rate = []
league_regular_far_total_attempt_rate = []
league_regular_far_total_made_rate = []

for i in range( len( league_regular_near_attempt ) ):
    league_regular_near_total_attempt_rate.append( league_regular_near_total_attempt[i] / league_regular_total_attempt[i] )
    league_regular_near_total_made_rate.append( league_regular_near_total_made[i] / league_regular_total_made[i] )
    league_regular_middle_total_attempt_rate.append(  league_regular_middle_total_attempt[i] / league_regular_total_attempt[i]  )
    league_regular_middle_total_made_rate.append(   league_regular_middle_total_made[i] / league_regular_total_made[i] )
    league_regular_far_total_attempt_rate.append(   league_regular_far_total_attempt[i] / league_regular_total_attempt[i] )
    league_regular_far_total_made_rate.append(   league_regular_far_total_made[i] / league_regular_total_made[i] )

### GSW
GSW_regular_near_total_attempt = []
GSW_regular_middle_total_attempt = []
GSW_regular_far_total_attempt = []
GSW_regular_near_total_made = []
GSW_regular_middle_total_made = []
GSW_regular_far_total_made = []

for i in range( len( GSW_regular_near_attempt ) ):
    GSW_regular_near_total_attempt.append( sum( GSW_regular_near_attempt[i] ) )
    GSW_regular_near_total_made.append( sum( GSW_regular_near_made[i] ) )
    GSW_regular_middle_total_attempt.append( sum( GSW_regular_middle_attempt[i] ) )
    GSW_regular_middle_total_made.append( sum( GSW_regular_middle_made[i] ) )
    GSW_regular_far_total_attempt.append( sum( GSW_regular_far_attempt[i] ) )
    GSW_regular_far_total_made.append( sum( GSW_regular_far_made[i] ) )

GSW_regular_total_attempt = []
GSW_regular_total_made = []

for i in range( len( GSW_regular_near_total_attempt ) ):
    GSW_regular_total_attempt.append( GSW_regular_near_total_attempt[i] + GSW_regular_middle_total_attempt[i] + GSW_regular_far_total_attempt[i] )
    GSW_regular_total_made.append( GSW_regular_near_total_made[i] + GSW_regular_middle_total_made[i] + GSW_regular_far_total_made[i] )

GSW_regular_near_total_attempt_rate = []
GSW_regular_near_total_made_rate = []
GSW_regular_middle_total_attempt_rate = []
GSW_regular_middle_total_made_rate = []
GSW_regular_far_total_attempt_rate = []
GSW_regular_far_total_made_rate = []

for i in range( len( GSW_regular_near_attempt ) ):
    GSW_regular_near_total_attempt_rate.append( GSW_regular_near_total_attempt[i] / GSW_regular_total_attempt[i] )
    GSW_regular_near_total_made_rate.append( GSW_regular_near_total_made[i] / GSW_regular_total_made[i] )
    GSW_regular_middle_total_attempt_rate.append(  GSW_regular_middle_total_attempt[i] / GSW_regular_total_attempt[i]  )
    GSW_regular_middle_total_made_rate.append(   GSW_regular_middle_total_made[i] / GSW_regular_total_made[i] )
    GSW_regular_far_total_attempt_rate.append(   GSW_regular_far_total_attempt[i] / GSW_regular_total_attempt[i] )
    GSW_regular_far_total_made_rate.append(   GSW_regular_far_total_made[i] / GSW_regular_total_made[i] )

### HOU
HOU_regular_near_total_attempt = []
HOU_regular_middle_total_attempt = []
HOU_regular_far_total_attempt = []
HOU_regular_near_total_made = []
HOU_regular_middle_total_made = []
HOU_regular_far_total_made = []

for i in range( len( HOU_regular_near_attempt ) ):
    HOU_regular_near_total_attempt.append( sum( HOU_regular_near_attempt[i] ) )
    HOU_regular_near_total_made.append( sum( HOU_regular_near_made[i] ) )
    HOU_regular_middle_total_attempt.append( sum( HOU_regular_middle_attempt[i] ) )
    HOU_regular_middle_total_made.append( sum( HOU_regular_middle_made[i] ) )
    HOU_regular_far_total_attempt.append( sum( HOU_regular_far_attempt[i] ) )
    HOU_regular_far_total_made.append( sum( HOU_regular_far_made[i] ) )

HOU_regular_total_attempt = []
HOU_regular_total_made = []

for i in range( len( HOU_regular_near_total_attempt ) ):
    HOU_regular_total_attempt.append( HOU_regular_near_total_attempt[i] + HOU_regular_middle_total_attempt[i] + HOU_regular_far_total_attempt[i] )
    HOU_regular_total_made.append( HOU_regular_near_total_made[i] + HOU_regular_middle_total_made[i] + HOU_regular_far_total_made[i] )

HOU_regular_near_total_attempt_rate = []
HOU_regular_near_total_made_rate = []
HOU_regular_middle_total_attempt_rate = []
HOU_regular_middle_total_made_rate = []
HOU_regular_far_total_attempt_rate = []
HOU_regular_far_total_made_rate = []

for i in range( len( HOU_regular_near_attempt ) ):
    HOU_regular_near_total_attempt_rate.append( HOU_regular_near_total_attempt[i] / HOU_regular_total_attempt[i] )
    HOU_regular_near_total_made_rate.append( HOU_regular_near_total_made[i] / HOU_regular_total_made[i] )
    HOU_regular_middle_total_attempt_rate.append(  HOU_regular_middle_total_attempt[i] / HOU_regular_total_attempt[i]  )
    HOU_regular_middle_total_made_rate.append(   HOU_regular_middle_total_made[i] / HOU_regular_total_made[i] )
    HOU_regular_far_total_attempt_rate.append(   HOU_regular_far_total_attempt[i] / HOU_regular_total_attempt[i] )
    HOU_regular_far_total_made_rate.append(   HOU_regular_far_total_made[i] / HOU_regular_total_made[i] )

## PLOT

years = [ '201718', '201819', '201920', '202021', '202122' ]

## attempt
plt.title("NBA attempt rate in near position", loc = 'left', fontsize = 24 )
plt.xlabel("Year", fontsize = 10)
plt.ylabel("Rate", fontsize = 10)

plt.plot( years, league_regular_near_total_attempt_rate, color = 'gray', marker = 'o' )
plt.plot( years, GSW_regular_near_total_attempt_rate, color = 'yellow', marker = 'o' )
plt.plot( years, HOU_regular_near_total_attempt_rate, color = 'red', marker = 'o' )

plt.savefig("near_league__attempt_comparison.png")
plt.show()

plt.title("NBA attempt rate in middle position", loc = 'left', fontsize = 24 )
plt.xlabel("Year", fontsize = 10)
plt.ylabel("Rate", fontsize = 10)

plt.plot( years, league_regular_middle_total_attempt_rate, color = 'gray', marker = 'o' )
plt.plot( years, GSW_regular_middle_total_attempt_rate, color = 'yellow', marker = 'o' )
plt.plot( years, HOU_regular_middle_total_attempt_rate, color = 'red', marker = 'o' )

plt.savefig("middle_league_attempt_comparison.png")
plt.show()

plt.title("NBA attempt rate in far position", loc = 'left', fontsize = 24 )
plt.xlabel("Year", fontsize = 10)
plt.ylabel("Rate", fontsize = 10)

plt.plot( years, league_regular_far_total_attempt_rate, color = 'gray', marker = 'o' )
plt.plot( years, GSW_regular_far_total_attempt_rate, color = 'yellow', marker = 'o' )
plt.plot( years, HOU_regular_far_total_attempt_rate, color = 'red', marker = 'o' )

plt.savefig("far_league_attempt_comparison.png")
plt.show()

## made 
plt.title("NBA made rate in near position", loc = 'left', fontsize = 24 )
plt.xlabel("Year", fontsize = 10)
plt.ylabel("Rate", fontsize = 10)

plt.plot( years, league_regular_near_total_made_rate , color = 'gray', marker = 'o' )
plt.plot( years, GSW_regular_near_total_made_rate , color = 'yellow', marker = 'o' )
plt.plot( years, HOU_regular_near_total_made_rate , color = 'red', marker = 'o' )

plt.savefig("near_league_made_comparison.png")
plt.show()

plt.title("NBA made rate in middle position", loc = 'left', fontsize = 24 )
plt.xlabel("Year", fontsize = 10)
plt.ylabel("Rate", fontsize = 10)

plt.plot( years, league_regular_middle_total_made_rate , color = 'gray', marker = 'o' )
plt.plot( years, GSW_regular_middle_total_made_rate , color = 'yellow', marker = 'o' )
plt.plot( years, HOU_regular_middle_total_made_rate , color = 'red', marker = 'o' )

plt.savefig("middle_league_made_comparison.png")
plt.show()

plt.title("NBA made rate in far position", loc = 'left', fontsize = 24 )
plt.xlabel("Year", fontsize = 10)
plt.ylabel("Rate", fontsize = 10)

plt.plot( years, league_regular_far_total_made_rate , color = 'gray', marker = 'o' )
plt.plot( years, GSW_regular_far_total_made_rate , color = 'yellow', marker = 'o' )
plt.plot( years, HOU_regular_far_total_made_rate , color = 'red', marker = 'o' )

plt.savefig("far_league_made_comparison.png")
plt.show()
