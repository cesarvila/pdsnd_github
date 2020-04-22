#let's import some libs
import pandas as pd
import time
import useful_functions as uf
import questions as q
sep = '\n============================================================'
sep1 = '\n------------------------------------------------------------'
texto = '\n\nHere you have some interesting figures in terms of:\n{}\n'
happen = '\tThis happened {}'
headers_list = ['City Name', 'Month (name)', 'Weekend/Weekdays',
                'Day of Week (name)', 'User Type', 'Gender', 'Adult/Under18']
def start_stats(df):
    ttext1 = '\n\n{}A. Distribution of trip duration per {} (in secs):\n'
    ttext2 = '\n\n{}B. "Most common hour to start a ride" per {}:\n'
    ttext3 = '\n\n{}C. "Most common trip" per {}:\n'
    k=1
    print(texto.format(q.cbucle(headers_list)))
    input('Press Enter to see them...\n')
    for header in headers_list:
        start = time.time()
        data = [df[header], df['Trip Duration']]
        headers = [header, 'Trip Duration']
        sf = pd.concat(data, axis=1, keys=headers)
        s1 = sf.groupby(header).agg({'Trip Duration':['mean',
                                                    'min', 'max',
                                                    'sum','count']})
        print(sep1 + ttext1.format(k,header))
        print(s1)
        data2 = [df[header], df['Hour']]
        headers2 = [header, 'Hour']
        sy = pd.concat(data2, axis=1, keys=headers2)
        s2 = sy.groupby([header]).agg(lambda x:x.value_counts().index[0])
        print(ttext2.format(k,header))
        print(s2)
        data3 = [df[header], df['Journey']]
        headers3 = [header, 'Journey']
        st = pd.concat(data3, axis=1, keys=headers3)
        s3 = st.groupby([header]).agg(lambda x:x.value_counts().index[0])
        print(ttext3.format(k,header))
        print(s3)
        k += 1
        end = time.time()
        input("\n this took {} seconds...\nPress Enter to continue...\n".format(end-start))
    print(sep1)
    start = time.time()
    print ('\n Other interesting statistics...\n\n')
    meanduration = uf.to_minutes_and_seconds(df['Trip Duration'].mean())
    minduration = uf.to_minutes_and_seconds(df['Trip Duration'].min())
    maxduration = uf.to_minutes_and_seconds(df['Trip Duration'].max())
    df1 = df[df['Trip Duration'] == df['Trip Duration'].min()]
    df2 = df[df['Trip Duration'] == df['Trip Duration'].max()]
    print('\n  Average duration of trips: ', meanduration)
    print('\n  Shortest duration of trips: ', minduration)
    un1 = df1['City Name'].unique()
    un2 = df2['City Name'].unique()
    um1 = df1['Month (name)'].unique()
    um2 = df2['Month (name)'].unique()
    print(happen.format('in ' + str(un1[0]) + ' on ' + str(um1[0])))
    uf.prints('\n  Longest duration of trips: ' + maxduration)
    print(happen.format('in ' + str(un2[0]) + ' on ' + str(um2[0])))
    hourt = '\n  Most common our to rent the bike: '
    df3 = df['Hour'].mode()[0]
    df3b = df[df['Hour'] == df['Hour'].mode()[0]]
    
    print (hourt, df3, 'h, this happened {} times'.
           format(df3b['Hour'].count()))
    journ = '\n  Most common trip: '
    df4 = df['Journey'].mode()[0]
    df5 = df[df['Journey'] == df['Journey'].mode()[0]]
    
    un3 = df['City Name'].unique()
  
    print(journ,'\n', 'From ', df4)
    print(happen.format('in ' + str(un3[0]) +
                        ' {} times'.format(df5['Journey'].count())))
    end = time.time()
    print('\n this took {} seconds...'.format(end-start))
    print(sep1)
    
def main():
    print('all ok')

if __name__ == '__main__':

    main()
