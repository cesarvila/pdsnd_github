import pandas as pd
import calendar as cld
import questions as q
import sys
import os
class fw_df:
    def __init__(self, tex, df):
        self.tt = tex
        self.d = df


def loading():
    print('\n\n........opening the csvs, please hold few seconds..........\n\n')

def error_handle(y):
    while True:
        try:
            a = int(input(y))
            go_out(a)
            return a
            break

        except ValueError:
            print('\n\nOops! That was no valid number. Try again...\n\t|\n\tV')

def go_out(x):
    if x == 0:
        print('\n\n\t\t\tGOODBYE \n')
        sys.exit(0)

def clearscreen():
    try:
        os.system("cls")
    except SyntaxError:
        os.system("clear")


def bring_list(k,df,cols):
    listas = []
    listas.append(glist(df,k+1,cols[k+0]))
    listas.append(glist(df,k+2,cols[k+1]))
    listas.append(glist(df,k+3,cols[k+2]))
    return listas


def abro(list_of_path,cities):
    if len(cities) >= 1:
        city1df = pd.read_csv(list_of_path[0])
        city1df['City Name'] = cities[0]
        df = city1df
    if len(cities) >= 2:
        city2df = pd.read_csv(list_of_path[1])
        city2df['City Name'] = cities[1]
        df = pd.concat([df,city2df])
    if len(cities) >= 3:
        city3df = pd.read_csv(list_of_path[2])
        city3df['City Name'] = cities[2]
        df = pd.concat([df,city3df])
    df = editdf(df)
    return df

def contador(number):
    """
    this function is to create a generator
    to iterate from 0 to number - 1
    """
    n = 0
    while n < number:
        yield n
        n += 1

def editdf(df):

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Month (name)'] =  df['Start Time'].dt.month_name()
    df['Day of Week (number)'] = df['Start Time'].dt.dayofweek
    df['Day of Week (name)'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.hour
    df['Weekend/Weekdays'] = df['Day of Week (number)']
    day_of_week_number = df['Day of Week (number)'].unique()
    day_of_week_number.sort()
    lista_w = []
    mycont = contador(7)
    for i in mycont:
        if i < 5:
            lista_w.append('Weekdays')
        else:
            lista_w.append('Weekends')
    dicdays = dict(zip(day_of_week_number,lista_w))
    df.replace({'Weekend/Weekdays': dicdays},  inplace = True)
    df['Journey'] = df['Start Station'] + ' to ' + df['End Station']
    df['Age'] = 2020 - df['Birth Year']
    df['Adult/Under18'] = df['Age']
    age_list = df['Age'].unique()
    age_list.sort()
    age_type = []
    for age in age_list:
        if age <18:
            age_type.append('Under 18')
        else:
            age_type.append('Adult')
    dicage = dict(zip(age_list,age_type))
    df.replace({'Adult/Under18': dicage},  inplace = True)
    return df

def filterdf(df, fil, col):

    if fil[0] != 'None':
        if len(fil) == 1:
            df = df[df[col[0]] == fil[0]]
        elif len(fil) == 2:
            df1 = df[df[col[0]] == fil[0]]
            df2 = df[df[col[1]] == fil[1]]
            df = pd.concat([df1,df2])
        else:
            print('error')
            go_out(0)

    return df

def getthefiltered_df(selection,k,df,cols,texto,op):
    cacerola = False
    if k == 0:
        selection += '\t * Period of time, including:\n'
    else:
        selection += '\t * Users, including:\n'
    l = bring_list(k,df,cols)
    cloutput = q.goption(l,texto,op,selection,k,cols)
    sel = cloutput.t
    try:
        df = filterdf(df, cloutput.f, cloutput.e)
        cdedf = fw_df(sel, df)
        cacerola = True
    except UnboundLocalError:
        print('{} will not be included in the filters of {}.\n\n'.
                format(cloutput.f,cloutput.e))
    finally:
        if cacerola == False:
            cloutput = q.Filtering('None','None',selection)
            sel = cloutput.t
            print('no debería entrar aquí',sel)
            cdedf = fw_df(sel, df)
    return cdedf



def prints(intexto):
    if len(intexto)>60:
        n = 54
        v= reduc(intexto,n)
        print(v)
    else:
        print(intexto)

def reduc(inputtext,length = None):
    """


    Parameters
    ----------
    inputtext : text to be printed.
    length : max length , optional
        DESCRIPTION. The default is None.

    Returns
    -------
    returns a shortened text

    """
    if length == None:
        return inputtext[0:39] + ' (...)'
    return inputtext[0:length] + ' (...)'

def glist(df,k,col):
    """
    returns a list for k=0 (time headers)
    or k=3 (user headers)
    col are the headers
    df is the dataframe for

    Parameters
    ----------
    df : dataframe
    k : integer k=0 (time headers)
    or k=3 (user headers)
    col : list of headers.

    Returns
    -------
    a list of unique items included in the selected headers

    """

    lista = df[col].unique()
    if k == 1:
        lista.sort()
        i = 0
        listatemp = []
        while i < len(lista):
            listatemp.append(cld.month_name[lista[i]])
            i += 1
        lista = listatemp
    elif k == 3:
        lista.sort()
        i = 0
        listatemp = []
        while i < len(lista):
            listatemp.append(cld.day_name[lista[i]])
            i += 1
        lista = listatemp
    lista = [x for x in lista if str(x) != 'nan']

    return lista



def to_minutes_and_seconds (secs):
    """
    Change secs into a string of years, weeks, days....
    Depending on its size

    Parameters
    ----------
    secs : integer

    Returns
    -------
    resul_t : string

    """
    secs = int(round(secs,0))
    texto_list = [' year ',' weeks ', ' days ', ' hours ',
                    ' minutes and ', ' seconds']
    resto_years = secs%31536000
    resto_weeks = resto_years%604800
    resto_dyas = resto_weeks%86400
    resto = resto_dyas%3600
    year_s = str(int(secs//31536000))
    week_s = str(int(resto_years//604800))
    dya_s = str(int(resto_weeks//86400))
    hour_s = str(int(resto_dyas//3600))
    minuto_s = str(int(resto//60))
    segundo_s = str(int(resto%60))

    tiempo_return = [year_s, week_s, dya_s, hour_s, minuto_s, segundo_s]

    if secs < 3600:
        indice = 4
    elif secs < 86400:
        indice = 3
    elif secs < 604800:
        indice = 2
    elif secs < 31536000:
        indice = 1
    else:
        indice = 0

    resul_t = ""
    while indice < len(tiempo_return):
        resul_t += tiempo_return[indice] + texto_list[indice]
        indice += 1
    return resul_t

def main():
    print('all ok')

if __name__ == '__main__':

    main()
