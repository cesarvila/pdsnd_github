#this script is used for asking questions

import useful_functions as uf
import bikeshare as bs
sep = '\n============================================================'
type_the_no = '\nPlease select your option typing the number (e.g.: 1):'
type_the_no += '\n\t\t--> '
main_qt_txt = '\n\nDo you want to get the stadistics in terms of:'
error_text ='Your input does not match with any of the options:\n'

class Filtering:
    def __init__(self, lista_filtros, lista_encabezados, texto):
        self.f = lista_filtros
        self.e = lista_encabezados
        self.t = texto

def start_questions():
    print(sep + '\n\n\tType 0 always you want to exit. \n' + sep)
    sqtext = '\n\t 1. Cities\n\t 2. Time\n\t 3. Users'
    sqtext += '\n\t 4. Combination of any of them\n\t 5. No filters at all\n'
    fq = uf.error_handle(sep + main_qt_txt +
    sqtext + type_the_no)
    while fq not in [1,2,3,4,5]:
        fq = uf.error_handle(error_text + sqtext + type_the_no)
    return fq

def deepcity(question,options,verb,sizeoflist):
    cityn = uf.error_handle(question.format(verb)
                                    + options + type_the_no)
    cityn = temp_bucle(cityn,sizeoflist,options)
    return cityn

def getcity(cities_list):
    fil = []
    co = []
    tgcity = '\n\nWhich city do you want to {}?\n'
    copttext = cbucle(cities_list)
    copttext1 = copttext + '\t4. Exclude one\n\t5. All\n'
    city = deepcity(tgcity,copttext1,'evaluate',5)
    if city == 4:
        city = deepcity(tgcity,copttext,'exclude',3)
        cities_list.pop(city-1)
        cit_c = cbucle_listas(cities_list,fil,co,'City Name')
    elif city == 5:
        cit_c = Filtering(['None'], ['None'], '\t\tAll cities\n')
    elif city < 4:
        city = cities_list[city-1]
        fil.append(city)
        co.append('City Name')
        tex = '\t\t' + city + '\n'
        cit_c = Filtering(fil, co, tex)
    else:
        print('I have accessed to line 56 in Questions.py, not possible.')
        uf.go_out(0)
    return  cit_c

def temp_bucle(a,b,text):
    while a not in [i for i in range(b+1) if i>0]:
        a = uf.error_handle(error_text + text + type_the_no)
    return a

def cbucle(lista):
    tex = ''
    j=0
    while j < len(lista):
        tex += '\t{}. '.format(j+1) + lista[j] +'\n'
        j += 1
    return tex

def cbucle_listas(lista,f,c,enca):
    tex = ''
    j=0
    while j < len(lista):
        tex += '\t\t{}. '.format(j+1) + lista[j] +'\n'
        f.append(lista[j])
        c.append(enca)
        j += 1
    clfil = Filtering(f,c,tex)
    return clfil

def for_mistake(k,selection,fil,co):
    if k == 0:
        selection += '\t\tNo filter by any Period of time\n'
    else:
        selection += '\t\tNo filter by Users, Gender or Age\n'
    fil.append('None')
    co.append('None')
    time_user_c = Filtering(fil,co,selection)
    return time_user_c

def goption(l,t,o,selection,k,cols):
    fil = []
    co = []
    if k == 3:
        y = 1
    else:
        y = 0
    chus = uf.error_handle(t[k + y]+ o[y] + type_the_no)
    chus = temp_bucle(chus,4,o[y])
    if chus == 4:
        time_user_c = for_mistake(k,selection,fil,co)
        return time_user_c
    else:
        try:
            u = len(l[chus-1])
            for n in range(u):
                t2lis = cbucle(l[chus-1])
                if chus == (n + 1):
                    chs = uf.error_handle(t[k + y + n + 1] + t2lis + type_the_no)
                    chs = temp_bucle(chs,u,t2lis)
                    j = n
                    selection += '\t\t ' + l[chus-1][chs-1] + '\n'
                    break
            if k == 0 and (chus == 1 or chus == 3):
                if chus == 1:
                    filtro = chs
                else:
                    filtro = (chs - 1)
            else:
                filtro = l[chus-1][chs-1]
            fil.append(filtro)
            co.append(cols[k+j])
            time_user_c = Filtering(fil, co, selection)
        except UnboundLocalError:
            print(sep)
            print('\n\nYou cannot filter by\n {} '.format(o[y]) +
            'since there are no registers for them\n in the current dataframe.')
            input('Press Enter to continue...')
            time_user_c = for_mistake(k,selection,fil,co)
        finally:
            time_user_c = time_user_c
        return time_user_c


def restart(df):
    zt = '\nDo you want to restart?'
    zt1 = '\n\tType y or n for yes or no:\n\t\t--> '
    z = input(zt + zt1)
    while z not in ['0','y','n']:
        z = input(error_text + zt1)
    if z == '0' or z == 'n':

        uf.go_out(0)
    else:
        a = True
        uf.clearscreen()
        bs.main(a,df)

def main():
    print('all ok')

if __name__ == '__main__':

    main()
