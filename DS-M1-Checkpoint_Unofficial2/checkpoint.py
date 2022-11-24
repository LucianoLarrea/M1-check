# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.
from pickletools import read_uint1
from xml.dom.minidom import Entity
import pandas as pd
import numpy as np

def Ret_Pregunta01():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros cuya entidad sean Colombia o México retornando 
    esos dos valores en una tupla de la siguiente manera (Colombia, México).
    Pista averiguar la funcion Shape
    '''
    #Tu código aca:
    df = pd.read_csv("DS-M1-Checkpoint_02\datasets\Fuentes_Consumo_Energia.csv")
    m = (df['Entity'] == 'Colombia')
    df1 = df[m]
    a = len(df1.index)
    a = int(a)

    n = (df['Entity'] == 'Mexico')
    df2 = df[n]
    b = len(df2.index)
    b = int(b)


    return a,b 
    #return 'Funcion incompleta'

def Ret_Pregunta02():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe eliminar las columnas 'Code' y 'Entity' y luego informar la cantidad de columnas
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    df = pd.read_csv('DS-M1-Checkpoint_02\datasets\Fuentes_Consumo_Energia.csv')
    df.drop (['Code'],axis=1, inplace=True )
    df.drop (['Entity'],axis=1, inplace=True)
    return len(df.columns)

    

def Ret_Pregunta03():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros de la columna Year sin tener en cuenta aquellos
    con valores faltantes retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    df = pd.read_csv('DS-M1-Checkpoint_02\datasets\Fuentes_Consumo_Energia.csv')
    result = df['Year'].dropna().index.size
    return int(result)

    #return 'Funcion incompleta'

def Ret_Pregunta04():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    El ExaJulio es una unidad diferentes al TWh, es decir, no tiene sentido sumarlos o
    buscar proporciones entre ellos, la fórmula de conversión es:
    277.778 Teravatios/Hora (TWh) = 1 Exajulio
    Los campos terminados en "_EJ" corresponden a mediciones en Exajulios,
    y los terminados en "_TWh" corresponden a Teravatios/Hora.
    La consigna es crear un nuevo campo, que se denomine "Consumo_Total"
    y que guarde la sumatoria de todos los consumos expresados en Teravatios/Hora
    (convirtiendo a esta medida los que están en Exajulios)
    Esta función debe informar el consumo total para la entidad 'World' y año '2019',
    redondeado a 2 decimales, retornando ese valor en un dato de tipo float.
    '''
    #Tu código aca:
    df = pd.read_csv('DS-M1-Checkpoint_02\datasets\Fuentes_Consumo_Energia.csv')
    def tera(valor):
        return valor * 277.778

    column_list_twh = ['Geo_Biomass_Other_TWh', 'Hydro_Generation_TWh', 'Nuclear_Generation_TWh', 'Solar_Generation_TWh', 'Wind_Generation_TWh']
    column_list_ej = ['Coal_Consumption_EJ', 'Gas_Consumption_EJ', 'Oil_Consumption_EJ']
    df['Consumo_Total1'] = df[column_list_ej].sum(axis=1)
    df['Consumo_Total1'] = df['Consumo_Total1'].apply(tera)
    df['Consumo_Total2'] = df[column_list_twh].sum(axis=1)
    df['Consumo_Total'] = df[['Consumo_Total1', 'Consumo_Total2']].sum(axis=1)
    del df['Consumo_Total1']
    del df['Consumo_Total2']

    m = (df['Entity'] == 'World') & (df['Year'] == 2019)
    df1 = df[m]
    a = round(float(df1['Consumo_Total']), 2)
    return a

    #return 'Funcion incompleta'

def Ret_Pregunta05():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar el año de mayor generación de energía hídrica (Hydro_Generation_TWh)
    para la entidad 'Europe' retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    df = pd.read_csv('DS-M1-Checkpoint_02\datasets\Fuentes_Consumo_Energia.csv')
    m = (df['Entity'] == 'Europe')
    new = df[m]

    max_gen = new['Hydro_Generation_TWh'].max()

    m2 = new['Hydro_Generation_TWh'] == max_gen
    row = new[m2]
    valor = row['Year']
    return int(valor)
    #return 'Funcion incompleta'

def Ret_Pregunta06(m1, m2, m3):
    '''
    Esta función recibe tres array de Numpy de 2 dimensiones cada uno, y devuelve el valor booleano
    True si es posible realizar una multiplicación entre las tres matrices (n1 x n2 x n3),
    y el valor booleano False si no lo es
    Ej:
        n1 = np.array([[0,0,0],[1,1,1],[2,2,2]])
        n2 = np.array([[3,3],[4,4],[5,5]])
        n3 = np.array([1,1],[2,2])
        print(Ret_Pregunta06(n1,n2,n3))
            True            -> Valor devuelto por la función en este ejemplo
        print(Ret_Pregunta06(n2,n1,n3))
            False            -> Valor devuelto por la función en este ejemplo
    '''
    #Tu código aca:
    a = m1.shape
    b = m2.shape
    c = m3.shape
    if a[1] == b[0]:
        return True
    elif a[1] == c[0]:
        return True
    else:
        return False
    #return 'Funcion incompleta'

def Ret_Pregunta07():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar cuál de la siguiente lista de países tuvo mayor generacíon de
    energía hìdrica (Hydro_Generation_TWh) en el año 2019:
        * Argentina
        * Brazil
        * Chile
        * Colombia
        * Ecuador
        * Mexico
        * Peru
    Debe retornar el valor en un dato de tipo string.
    '''
    #Tu código aca:
    df = pd.read_csv('DS-M1-Checkpoint_02\datasets\Fuentes_Consumo_Energia.csv')

    m1 = ((df['Entity'] == 'Argentina') | (df['Entity'] == 'Brazil') | (df['Entity'] == 'Chile') | (df['Entity'] == 'Colombia') | (df['Entity'] == 'Ecuador') | (df['Entity'] == 'Mexico') | (df['Entity'] == 'Peru')) & (df['Year'] == 2019)
    df2 = df[m1] 

    column = df2['Hydro_Generation_TWh']
    max_value = column.max()
    m2 = (df2 ['Hydro_Generation_TWh'] == max_value)
    df3 = df2[m2]
    valor = df3['Entity'].values[0]
    return valor
    #return 'Funcion incompleta'

def Ret_Pregunta08():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de entidades diferentes que están presentes en el dataset
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    df = pd.read_csv('DS-M1-Checkpoint_02\datasets\Fuentes_Consumo_Energia.csv')

    df1 = df.drop_duplicates(subset='Entity', keep='first')
    a = len(df1.index) - 1
    return a
    #return 'Funcion incompleta'

def Ret_Pregunta09():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "datasets/Tabla1_ejercicio.csv" y "datasets/Tabla2_ejercicio.csv".
    Esta función debe informar: score_promedio_femenino y score_promedio_masculino en formato tupla
    '''
    #Tu código aca:
    df1 = pd.read_csv('DS-M1-Checkpoint_02\datasets\Tabla1_ejercicio.csv', sep=';', encoding='utf-8')
    df2 = pd.read_csv('DS-M1-Checkpoint_02\datasets\Tabla2_ejercicio.csv', sep=';', encoding='utf-8')

    df3 = pd.merge(df1, df2, on='pers_id')

    m = (df3['sexo'] == 'F')
    m2 = (df3['sexo'] == 'M')

    female = df3[m]
    mean_f = female['score'].mean()
    male = df3[m2]
    mean_m = male['score'].mean()
    a = (round(mean_f, 2), round(mean_m, 2))
    return a

    #return 'Funcion incompleta '


def Ret_Pregunta10(lista):
    '''
    Esta función recibe como parámetro un objeto de la clase Lista() definida en el archivo Lista.py.
    Debe recorrer la lista y retornan la cantidad de nodos que posee. Utilizar el método de la clase
    Lista llamado getCabecera()
    Ejemplo:
        lis = Lista()
        lista.agregarElemento(1)
        lista.agregarElemento(2)
        lista.agregarElemento(3)
        print(Ret_Pregunta10(lista))
            3    -> Debe ser el valor devuelto por la función Ret_Pregunta10() en este ejemplo
    '''
    #Tu código aca:
    c = 0
    a = lista.getCabecera()
    if a:
        c = 1
    while a.getSiguiente():
        c += 1
        a = a.getSiguiente()
    
    return c