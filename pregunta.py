"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #
###########################################################
# Borrado de registros duplicados
#
    df=df.drop(['Unnamed: 0'], axis=1)
    df[df.duplicated()]
    df.drop_duplicates(inplace=True)

    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)

#Convertir sexo y emprendimiento lower ################################################
    df.sexo=df.sexo.str.lower()
    df.tipo_de_emprendimiento=df.tipo_de_emprendimiento.str.lower()

#CATEGORIAS ARREGLADAS ###############################################
    idea_negocio_df = pd.DataFrame({ 'idea_negocio': list(df.idea_negocio) })
    idea_negocio_df = idea_negocio_df.drop_duplicates()
    idea_negocio_df = idea_negocio_df.assign(key=idea_negocio_df.idea_negocio.str.lower())
    idea_negocio_df.groupby('key').agg(list)
#
# Corrección por reemplazo
#
    df['idea_negocio'] = df.idea_negocio.str.replace(' ', '_')
    df['idea_negocio'] = df.idea_negocio.str.replace('-', '_')
    df['idea_negocio'] = df.idea_negocio.str.replace('_', ' ')
    df['idea_negocio'] = df.idea_negocio.str.lower()
    df.sort_values('idea_negocio')

#CATEGORIAS ARREGLADAS ###############################################
    barrio_df = pd.DataFrame({ 'barrio': list(df.barrio) })
    barrio_df = barrio_df.drop_duplicates()
    barrio_df = barrio_df.assign(key=barrio_df.barrio.str.lower())
    barrio_df.groupby('key').agg(list)
#
# Corrección por reemplazo
#
    df['barrio'] = df.barrio.str.replace(' ', '_')
    df['barrio'] = df.barrio.str.replace('-', '_')
    df['barrio'] = df.barrio.str.replace('_', ' ')
    df['barrio'] = df.barrio.str.lower()
    df.sort_values('barrio')

#CATEGORIAS ARREGLADAS ###############################################
    línea_credito_df = pd.DataFrame({ 'línea_credito': list(df.línea_credito) })
    línea_credito_df = línea_credito_df.drop_duplicates()
    línea_credito_df = línea_credito_df.assign(key=línea_credito_df.línea_credito.str.lower())
    línea_credito_df.groupby('key').agg(list)
#
# Corrección por reemplazo
#
    df['línea_credito'] = df.línea_credito.str.replace(' ', '_')
    df['línea_credito'] = df.línea_credito.str.replace('-', '_')
    df['línea_credito'] = df.línea_credito.str.replace('_', ' ')
    df['línea_credito'] = df.línea_credito.str.lower()
    df.sort_values('línea_credito')

    df[df.duplicated()]
    df.drop_duplicates(inplace=True)

###############################################
# Corrección
#
    df.monto_del_credito = df.monto_del_credito.str.strip('$')
    df.monto_del_credito = df.monto_del_credito.str.replace(',', '')
    df.monto_del_credito = df.monto_del_credito
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df.monto_del_credito.value_counts()

    df[df.duplicated()]
    df.drop_duplicates(inplace=True)

# BORRAR NA DE BARRIO 
    df=df.dropna(subset=["barrio"])
    df=df.dropna(subset=["tipo_de_emprendimiento"])

    return df
