from pyspark.sql.functions import count, col, lit, when
from pyspark.sql.types import IntegerType,DecimalType
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import datetime
import scipy
import sklearn
from sklearn import metrics
import seaborn as sns
from datetime import datetime

# simple count of nulls per column:
print 'Number of rows: {}'.format(df5.count())
df_5=df5.select([count(when(col(c).isNull(), c)).alias(c) for c in df5.columns]).toPandas()
print "number of null values:"
df_5.loc[:, (df_5 != 0).any(axis=0)]



def partial_analyzer_by_df(df, unique=True):
    df.cache()

    number_of_rows = df.count()
    print' \nNumber of rows: {}\n'.format(number_of_rows)

    print    "#" * 20
    print    ""
    print    "Number of null values:"
    nulls = df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns])
    print    "Summarize of all variables nulls (number of nulls)"
    nulls.show()

    print    "\n \n Percentage of null values (%):"
    df_ = df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns]).toPandas()
    print    df_.loc[:, (df_ != 0).any(axis=0)] / number_of_rows * 100
    all_null_cols = []
    some_nulls_cols = []
    nonNulls_cols = []

    print    "\nAnalyzing column's 'completeness'\n"
    for c in nulls.columns:
        if nulls[[c]].first()[c] == 0:
            nonNulls_cols.append(c)
        elif nulls[[c]].first()[c] == number_of_rows:
            all_null_cols.append(c)
        else:
            some_nulls_cols.append(c)

    print    "Columns with ALL values as nulls:"
    print    "   ", all_null_cols
    print    " "
    print    "Columns with SOME values as nulls:"
    print    "   ", some_nulls_cols
    print    " "
    print    "Columns with NO values as nulls:"
    print    "   ", nonNulls_cols
    print    " "

    print    "#" * 20
    if unique:
        size_string = max([len(x) for x in df.schema.names]) + 1
        print        ""
        print        "Number of unique values per column"
        for name in df.schema.names:
            # print name + ':' ,df.select(name).distinct().count()
            cou = df.select(name).distinct().count()
            total = df.select(name).count()
            if cou == total:
                uni = "unique value per row ({}/{})".format(cou, total)
            else:
                uni = "Repeted values in the column"
            print            '       {message: <{size}}:{counter: <7}/{total}   ({uni})'.format(message=name, size=size_string,
                                                                               counter=cou, uni=uni, total=total)
        print        ""
    df.unpersist()
    return df

def repetidos(df,columns, number=30):
    #columns as a list
    df.select(columns).groupBy(columns).count().orderBy("count", ascending=False).show(number, truncate=False)

def unique_by_pair(dataframe, pair):
    if dataframe.select("column", pair).distinct().count() == dataframe.count():
        print "The pair column-{} is unique".format(pair.upper())
    else:
        print "The pair column-{} is NOOOT unique".format(pair.upper())
        dataframe.select("column", pair).groupby("column", pair).count().orderBy("count", ascending=False).show()


def analyzer(spark, address, source_type, schema, unique=True):
    # tipe: parquet or csv
    # schema: class raw schema (only for raws)
    if source_type == "parquet":
        df = spark.read.parquet(address)
    else:
        df = spark.read.format(source_type).option("header", "false").option("delimiter", "|").schema(schema).load(
            address)

    df.cache()
    number_of_rows = df.count()
    print    ' \nNumber of rows: {}\n'.format(number_of_rows)
    print    "#" * 20

    print    "\n Showing the dataframe \n"
    df.show(3)
    print    "\n"
    print    "#" * 20
    print    ""
    print    "Number of null values:\n"
    nulls = df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns])
    print    "Summarize of all variables nulls (number of nulls)"
    nulls.show()

    df_ = df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns]).toPandas()
    print    "\n \n Percentage of null values (%):\n"
    print    df_.loc[:, (df_ != 0).any(axis=0)] / number_of_rows * 100
    all_null_cols = []
    some_nulls_cols = []
    nonNulls_cols = []

    print    "\n\nAnalyzing column's 'completeness'\n"
    for c in nulls.columns:
        if nulls[[c]].first()[c] == 0:
            nonNulls_cols.append(c)
        elif nulls[[c]].first()[c] == number_of_rows:
            all_null_cols.append(c)
        else:
            some_nulls_cols.append(c)

    print    "Columns with ALL values as nulls:"
    print    "   ", all_null_cols
    print    " "
    print    "Columns with SOME values as nulls:"
    print    "   ", some_nulls_cols
    print    " "
    print    "Columns with NO values as nulls:"
    print    "   ", nonNulls_cols
    print    " "

    print    "#" * 20
    if unique:
        size_string = max([len(x) for x in df.schema.names]) + 1
        print        ""
        print        "Number of unique values per column"
        for name in df.schema.names:
            # print name + ':' ,df.select(name).distinct().count()
            cou = df.select(name).distinct().count()
            total = df.select(name).count()
            if cou == df.select(name).count():
                uni = "unique value per row"
            else:
                uni = "Repeted values in the column"
            print            '       {message: <{size}}:{counter: <7}/{total}   ({uni})'.format(message=name, size=size_string,
                                                                               counter=cou, uni=uni, total=total)
        print        ""
    if "last_payment_dt" in nonNulls_cols:
        nonNulls_cols.remove("last_payment_dt")

    print
    "\n General description of the dataframe (except booleans)"

    nonNulls_cols2 = []
    for coll in nonNulls_cols:
        if not coll.startswith("bit_") and not coll.endswith("_dt") and not coll == "timestamp":
            nonNulls_cols2.append(coll)

    df.describe(*nonNulls_cols2).show()

    if set(["column_id", "column_id_2"]).issubset(df.columns):
        print "\n***"
        unique_by_pair(df, "column")
        print "***\n"

    print    "sampling:"
    try:
        if df.count() > 2000000:
            df1 = df.sample(fraction=float(2000000) / df.count(), withReplacement=False).toPandas()
        else:
            df1 = df.toPandas()
    except Py4JJavaError:
        print        "Dataframe too big. Shrinking sample size"
        try:
            df1 = df.sample(fraction=float(1600000) / df.count(), withReplacement=False).toPandas()
        except Py4JJavaError:
            print            "Dataframe too big again. Shrinking sample size more"
            df1 = df.sample(fraction=float(1200000) / df.count(), withReplacement=False).toPandas()

    print    "Sample size:", df1.count()[0]

    print    "\n Sample description: \n"
    print    df1.describe()

    print    "#" * 50
    print    "#" * 50 + "################# features analysis (sampled)  ################### "
    print    "#" * 50
    print    ""

    #     for column in df1.columns:
    for column in some_nulls_cols + nonNulls_cols:
        print        ""
        print        "Feature: {}".format(column)
        print        "  Description"
        print        df1[column].describe()
        print        " "
        valid_ids = ["valid_id_list..."]
        if column.endswith("_id") and column not in valid_ids:
            print            " "
            if df1[column].nunique() == df1[column].count():
                print                " **YES,  unique id value per row"
            else:
                print                "Not unique value per row"
                if df1[column].nunique() == 1:
                    print                    "    Constant column, all values are:  ", df1[column][1]
                else:
                    df1[column].astype(unicode).describe()
            print            " "
            print            "#" * 40
            continue
        if column.startswith("cat_"):
            print            " "
            print            "Categories distributions: "
            print            " "
            plt.figure(figsize=(15, 7))
            df1[column].value_counts().plot(kind='bar')
            plt.show()
        elif column.startswith("bit_"):
            print            " "
            print            "binary distributions: "
            print            " "
            print            df1[column].value_counts()
            plt.figure(figsize=(15, 7))
            df1[column].value_counts().plot(kind='bar')
            plt.show()
        elif column.endswith("_dt"):
            print            "Minimum date of the column:", min(df1[column].dropna())
            print            "Maximum date of the column:", max(df1[column].dropna())
            print            ""
            plt.figure(figsize=(15, 7))
            df1[column].groupby(df1[column]).count().plot()
            plt.show()
        else:
            if df1[column].nunique() == 1:
                print                "         Constant column, all values are:  ", df1[column][1]
                print                " "
                continue
            elif df1[column].nunique() == 0:
                print                "empty column, all values are empty"
                print                " "
                continue

            else:
                print                "Regular distribution"
                if df1[column].dtype == object:  # and not column.endswith("_dt"):
                    if df1[column].nunique() > 40:
                        plt.figure(figsize=(15, 7))
                        df1[column].value_counts().plot(kind='hist', bins=100)
                        plt.xticks(rotation=90)
                        plt.show()
                    else:
                        plt.figure(figsize=(15, 7))
                        df1[column].value_counts().plot(kind='bar')
                        plt.show()
                else:
                    plt.figure(figsize=(15, 7))
                    sns.kdeplot(df1[column].dropna(inplace=False, axis=0, how='all'))  # sns.kdeplot(df1[column])
                    plt.show()
        print        "#" * 40
    print    "*" * 10
    df.unpersist()
    return df, df1
