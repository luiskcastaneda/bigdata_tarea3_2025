from pyspark.sql import SparkSession

# Crear sesión de Spark
spark = SparkSession.builder \
    .appName("ConsultaDatasetColombia") \
    .getOrCreate()

# Ruta al archivo CSV en HDFS (ajústala si tu ruta HDFS es distinta)
ruta_hdfs = "hdfs://localhost:9000/Tarea3_bigdata/twnk-hika.csv"

# Cargar el CSV en un DataFrame de Spark
df = spark.read.csv(ruta_hdfs, header=True, inferSchema=True)

# Mostrar esquema del DataFrame
print("Esquema del DataFrame:")
df.printSchema()

# Mostrar las primeras 10 filas del DataFrame
print("Primeras filas del dataset:")
df.show(10)

# Ejemplo de algunas operaciones
print("Número de registros en el dataset:")
print(df.count())

# Mostrar columnas únicas en una columna específica (ej: tipo de servicio)
if 'tipo_servicio' in df.columns:
    print("Tipos de servicio únicos:")
    df.select("tipo_servicio").distinct().show()

# Filtrar por algún valor (ejemplo si existe una columna 'municipio')
if 'municipio' in df.columns:
    print("Registros del municipio de Medellín:")
    df.filter(df["municipio"] == "Medellín").show(10)


# Cantidad total de registros
print("Número de registros en el dataset:")
print(df.count())

# Tipos de servicio únicos (si existe la columna)
if 'tipo_servicio' in df.columns:
    print("Tipos de servicio únicos:")
    df.select("tipo_servicio").distinct().show()

# Filtrar registros por municipio (si existe)
if 'municipio' in df.columns:
    print("Registros del municipio de Medellín:")
    df.filter(df["municipio"] == "Medellín").show(10)

# Agrupación por especialidad (si existe la columna)
if 'especialidad' in df.columns:
    print("Cantidad de citas por especialidad:")
    df.groupBy("especialidad").count().orderBy("count", ascending=False).show(truncate=False)
else:
    print("La columna 'especialidad' no se encuentra en el DataFrame.")

# Detener sesión de Spark

# Detener la sesión de Spark
spark.stop()
