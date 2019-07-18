# Basic example

	from pyspark import SparkContext
	from pyspark.sql import SQLContext
	from pyspark.sql.types import StringType, IntegerType, StructType, StructField
	from pyspark.sql.functions import lit, monotonically_increasing_id
	sc = SparkContext(master="local",  appName="demo")
	sqlContext = SQLContext(sc)

	print(sc.version)
	df2 = sc.textFile("files/demo.txt").map(lambda x: tuple(x.split(",")))
	header = df2.first()
	schema = StructType([StructField(i, StringType(), True) for i in header])
	df2.collect()
	# ojo si min index no es 0
	a2 = sqlContext.createDataFrame(data=df2, schema=schema) \
	    .withColumn("index", monotonically_increasing_id()).filter("index != 0").drop("index")
	sqlContext.createDataFrame([(5, "hello"), (55, "caramba")], ['a', 'b']).show()
	print(df2.isEmpty())
	print(df2.count())
	print(df2.collect())

	a2.show()
	a2.withColumn("new", lit("a")).show()
	df = sqlContext.createDataFrame(sc.parallelize([(1,), (2,), (3,)]), StructType([StructField("neww",
	                                                                                            IntegerType())]))
	df.show()


	sqlContext.createDataFrame([(5,), (6,)], ['beee']).rdd.map(lambda x: x[0]).collect()


	class Test(object):
	    def __init__(self, prop1, prop2):
	        self.prop1 = prop1
	        self.prop2 = prop2

	    def describe(self):
	        print(self.prop1)
	        print(self.prop2)


	ob = Test(1, 2)
	ob2 = Test(3, 4)
	t = sqlContext.createDataFrame([(ob,), (ob2,)], ['beee'])
	t.rdd.map(lambda x: x[0]).collect()
	t.rdd.map(lambda x: x[0]).collect()[0].describe()
	li = [ob, ob2]
	li[0].describe()


# tutorial


    #import pyspark
    from pyspark import SparkContext
    from pyspark.sql import SQLContext, Row
    from pyspark.sql.types import StringType, IntegerType, StructType, StructField, DoubleType
    from pyspark.sql.functions import lit, monotonically_increasing_id
    sqlContext = SQLContext(sc)
    from pyspark.sql import SparkSession
    spark = SparkSession.builder.appName('learning').getOrCreate()
    sc = SparkContext('local[*]',  appName="demo")
    sc.version
    
    
    # do something to prove it works
    rdd = sc.parallelize(range(1000))
    rdd.takeSample(False, 5)
    
    
    #from list
    sqlContext.createDataFrame([(5, "hello"), (55, "caramba")], ['a', 'b']).show()
    
    
    # from dict
    d = [{'name': 'Alice', 'age': 1},
        {'name': 'Alize', 'age': 0}]
    spark.createDataFrame(d).show()
    
    
    # schema
    header = ["id"]
    Schema = StructType([StructField(i, StringType(), True) for i in header])
    rows = [('a',), ("b",)]
    df = spark.createDataFrame(rows, schema=Schema)
    df.printSchema()
    df.show()
    
    
    # empty one
    schema = StructType([])
    empty = sqlContext.createDataFrame(sc.emptyRDD(), schema)
    
    
    # row
    values = [Row(id=1, name='1'),
              Row(id=12, name='12'),
              Row(id=123, name='123'),
              Row(id=1234, name='1234'),
              Row(id=12345, name='12345')]
    spark.createDataFrame(values).show()
    
    
    
    # from rdd
    l = [('a',1),('b',2),('c',3),('d',4)]
    rdd = sc.parallelize(l)
    rdd2 = rdd.map(lambda x: Row(letter=x[0], number=int(x[1])))
    sqlContext.createDataFrame(rdd2).show()
    
    
    
    # or
    rdd = sc.parallelize([(1,2,3),(4,5,6),(7,8,9)])
    rdd.toDF(["a","b","c"]).show()
    
    
    # or 
    rdd = sc.parallelize([Row(a=1,b=2,c=3),Row(a=4,b=5,c=6),Row(a=7,b=8,c=9)])
    rdd.toDF().show()
    
    
    
    # moar...
    # row
    values = [Row(id=1, name='1'),
              Row(id=12, name='12'),
              Row(id=123, name='123'),
              Row(id=1234, name='1234'),
              Row(id=12345, name='12345')]
    df = spark.createDataFrame(values)
    df2 = df.withColumn("new", lit("a")) \
    .withColumn("index", monotonically_increasing_id())
    df2.show()
    
    
    print(df.count())
    print(df.collect())
    
    df.describe().show()
    
    df2.drop("index", "new").show()
    
    
    df2.select("id","name").withColumn("plus", df2["id"] + 5).filter("plus >150").show()
    
    
    
    from pyspark.sql.functions import udf
    def doubler(x):
        return x*2
    doubler_udf = udf(doubler, IntegerType())
    other_doubler_udf = udf(lambda x: x*2)
    df2.withColumn("double", doubler_udf(df2.id)) \
    .withColumn("double_two", other_doubler_udf(df2.id)).show()
    
    
    df2.select("id","name") \
    .withColumn("multiple_columns_udf", udf(lambda x, y: x + len(y))(df2.id, df["name"])).show()
    
    df2.groupBy("new").agg({"id": "sum"}).show()