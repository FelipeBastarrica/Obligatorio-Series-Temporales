import glob
import pandas as pd

path = r'/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/may19_set19/' # use your path
all_files = glob.glob(path + "/*.csv")
li = []
all_files_2017 = ['/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_diciembre_2017/autoscope_enero_2017.csv',
                  '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_diciembre_2017/autoscope_febrero_2017.csv',
                  '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_diciembre_2017/autoscope_marzo_2017.csv',
                  '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_diciembre_2017/autoscope_abril_2017.csv',
                  '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_diciembre_2017/autoscope_mayo_2017.csv',
                  '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_diciembre_2017/autoscope_junio_2017.csv',
                  '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_diciembre_2017/autoscope_julio_2017.csv',
                  '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_diciembre_2017/autoscope_agosto_2017.csv',
                  '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_diciembre_2017/autoscope_set_2017.csv',
                  '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_diciembre_2017/autoscope_oct_2017.csv',
                  '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_diciembre_2017/autoscope_nov_2017.csv',
                  '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_diciembre_2017/autoscope_dic_2017.csv']

all_files_2018 = ['/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_septiembre_2018/autoscope_ene_2018.csv',
                     '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_septiembre_2018/autoscope_feb_2018.csv',
                     '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_septiembre_2018/autoscope_mar_2018.csv',
                     '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_septiembre_2018/autoscope_abr_2018.csv',
                     '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_septiembre_2018/autoscope_may_2018.csv',
                     '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_septiembre_2018/autoscope_jun_2018.csv',
                     '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_septiembre_2018/autoscope_julio_2018.csv',
                     '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_septiembre_2018/autoscope_ago_2018.csv',
                     '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_septiembre_2018/autoscope_sep_2018.csv']

all_files_2018_2019 = ['/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/octubre18_abril19/autoscope_oct_2018.csv',
                       '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/octubre18_abril19/autoscope_nov_2018.csv',
                       '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/octubre18_abril19/autoscope_dic_2018.csv',
                        '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/octubre18_abril19/autoscope_ene_2019.csv',
                        '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/octubre18_abril19/autoscope_feb_2019.csv',
                       '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/octubre18_abril19/autoscope_mar_2019.csv',
                       '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/octubre18_abril19/autoscope_abril_2019.csv']

all_files_2019 = ['/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/may19_set19/Autoscope_05_2019.csv',
                  '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/may19_set19/Autoscope_06_2019.csv',
                  '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/may19_set19/Autoscope_07_2019.csv',
                  '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/may19_set19/Autoscope_08_2019.csv',
                  '/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/may19_set19/Autoscope_09_2019.csv']

for filename in all_files_2019:
    df = pd.read_csv(filename, sep=',', encoding='latin-1', index_col=None, header=0, engine='python')
    li.append(df)
'''
df = pd.read_csv('/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/test.csv', sep=',', encoding='latin-1', index_col=None, header=0, engine='python')
li.append(df)'''
frame = pd.concat(li, axis=0, ignore_index=True)
print(frame.head())
print(frame.size)
parametro_a_filtrar = "dsc_avenida"
nombre_a_filtrar = "Sarmiento"

df_2017_filtered = frame[frame[parametro_a_filtrar] == nombre_a_filtrar]

#df = pd.read_csv('/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_diciembre_2017/autoscope_julio_2017.csv', sep=';', encoding='latin-1', index_col=None, header=0, engine = 'python')
#df.to_csv("/Users/felipebastarricaboghossian/PycharmProjects/Procesamiento_conteo/enero_a_diciembre_2017/autoscope_julio_2017_2.csv")
print(df_2017_filtered.head())
print(df_2017_filtered.size)
df_2017_filtered["date"] = df_2017_filtered["fecha"].astype(str) +' '+ df_2017_filtered["hora"].astype(str)
df_2017_filtered['date'] = pd.to_datetime(df_2017_filtered['date'])
df_final = df_2017_filtered[["date", "volumen"]]
df_final.set_index('date', inplace=True)

#df_2017_filtered["date"] = df_2017_filtered[['fecha', 'hora']].agg(' '.join, axis=1)
df_2017_filtered.to_csv("all_files_2019.csv")
df_final.to_csv("df_final_2019.csv")
#df.Date = pd.to_datetime(df.Date)
