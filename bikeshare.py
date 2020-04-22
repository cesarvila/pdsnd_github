#This is the script for the bikeshare project
#let's import some libs
import glob
import os
import time
#below are included the supporting scripts with their Aliases
import questions as q
import useful_functions as uf
import stat_script as sta
#now import my own scripts
#from useful_functions import sele
#from useful_functions import sel

def main(a = False, df = 'None'):
    tgtime = '\n\nWhich term do you want to include in your stats?\n'
    t1 = '\nWhich month?\n'
    t2 = '\nWeekend or weekdays?\n'
    t3 = '\nWhich day?\n'
    opttext = '\t1. Month\n\t2. Weekdays / weekend\n\t'
    opttext += '3. Day of the week\n\t4. All\n'
    tgus = '\n\nYou want to filter by:\n'
    p1 = '\nWhich User type?\n'
    p2 = '\nWhich gender?\n'
    p3 = '\nWhich group of ages?\n'
    opttext1 = '\t1. User type\n\t2. Gender\n\t3. Age\n\t4. All\n'
    texto = [tgtime,t1,t2,t3,tgus,p1,p2,p3]
    op = [opttext, opttext1]
    cols = ['Month','Weekend/Weekdays','Day of Week (number)',
            'User Type','Gender','Adult/Under18']
    csvS = glob.glob('csv/*.csv')
    current_dir = os.path.dirname(os.path.realpath(__file__))
    #now it is created a list of cities "cities_list"
    cities_list = []
    for csv in csvS:
        csv = csv[4:-4].title().replace("_"," ")
        cities_list.append(csv)
    path_cities = [os.path.join(current_dir, csvS[0]),
     os.path.join(current_dir, csvS[1]), os.path.join(current_dir, csvS[2])]

    f1 = '\n' + ' | '*20
    f1 += '\n' + ' | '*20
    f1 += '\n' + ' V '*20

    if a == False:
        uf.clearscreen()
        print('\n\nHello! Let\'s explore some US bikeshare data!\n')
        uf.loading()
        start = time.time()
        df = uf.abro(path_cities,cities_list)
        end = time.time()
        print('\n\nOnly {} seconds to open {} csvs with {} lines!'.format(end-start,
                                            len(csvS), df['Start Time'].count()))
        input("\nPress Enter to continue...\n")
        uf.clearscreen()
    selection = '\n\nYour choice is filter by: \n'
    a = q.start_questions()
    if a == 1:
        selection += '\t * Cities, including:\n'
        uf.clearscreen()
        print(selection)
        cityoutput = q.getcity(cities_list)
        uf.clearscreen()
        print(f1 + selection + cityoutput.t)
        try:
            df1 = uf.filterdf(df, cityoutput.f, cityoutput.e)
        except:
            print('algo pasa cuando a == 1')
    elif a == 2:
        clasededf = uf.getthefiltered_df(selection,0,df,cols,texto,op)
        sel = clasededf.tt
        uf.clearscreen()
        print (f1 + selection + sel)
        df1 = clasededf.d
    elif a == 3:
        clasededf = uf.getthefiltered_df(selection,3,df,cols,texto,op)
        sel = clasededf.tt
        uf.clearscreen()
        print (f1 + selection + sel)
        df1 = clasededf.d
    elif a == 4:
        selection += '\n A combination of:\n'
        uf.clearscreen()
        print(selection)
        cityoutput = q.getcity(cities_list)
        selection += '\t * Cities, including:\n'

        df1 = uf.filterdf(df, cityoutput.f, cityoutput.e)
        selection += cityoutput.t
        uf.clearscreen()
        print(selection)

        clasededf = uf.getthefiltered_df(selection,0,df1,cols,texto,op)
        sel = clasededf.tt
        uf.clearscreen()
        print(sel)
        df1 = clasededf.d
        clasededf2 = uf.getthefiltered_df(sel,3,df1,cols,texto,op)
        sel = clasededf2.tt
        uf.clearscreen()
        print(f1 + sel)
        df1 = clasededf2.d
    elif a == 5:
        selection += '\t* Not filters at all'
        uf.clearscreen()
        print(f1 + selection)
        df1 = df
    else:
        print('An error shall have occurred.')
        uf.go_out(0)


    input('\nPress enter to start the statistics...')
    sta.start_stats(df1)

    q.restart(df)

if __name__ == "__main__":
	main()
