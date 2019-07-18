# Hive


## Launch with docker:

De https://github.com/big-data-europe/ descargar el hive project: docker-hive-master 
y ejecutar para lanzar:

	cd <path>\docker-hive-master
	docker-compose up -d
	docker-compose exec hive-server bash
	cd /opt/hive/bin/
	beeline -u jdbc:hive2://localhost:10000

	# o 
	hive

## Launch in local:

After downloading and doing god-like instalation. Never works perfectly...

	C:\hadoop-2.3.0\sbin>start-all.cmd
	C:\db-derby-10.12.1\bin>startNetworkServer -h 0.0.0.0
	hive --hiveconf hive.root.logger=WARN,console


## Basic code examples

	create database  if not exists testing;
	show databases;
	show databases like 't*';
	use testing;
	create database if not exists Movies_data comment 'Data of the movies';
	create database test location '/user/fake_directory';
    describe database testing;

    drop database test_databse;
    drop database test_database cascade; # With all tables inside


### Simple usage

	create table table1 (id int, col1 int, col2 string);
	show tables;
	insert into table1 values (1,1, 'a'); 
	insert into table1 values (2,1, 'aa');
	insert into table1 values (3,2, 'aaa');
	insert into table1 values (4,2, 'aaaa');
	insert into table1 values (5,3, 'aaaaa');
	select *, '' as Empty from table1;


### Ouside usage

	hive -S -e "set" | grep warehouse;
	hive -f /<path>/.file.hql

	hive>

    ! pwd
    ! ls
    dfs -ls /;

    -- inside database
    set hive.cli.print.current.db=true;

#### Other usages

	impala-shell -i <impala_server> -q "select * from table" 
	impala-shell -i <impala_server> -f path/to/file/query.sql


	# o en pasos:
	impala-shell
	connect <impala_server>;
	show databases;
	...

### Complete usage

    create table a_table (user_id int)
    row formatted delimited    
    fields terminated ny '|'
    stored as textfile;    

    DESCRIBE FORMATTED a_table;
    load data inpath '/user/.../file' overwrite into table a_table; # loads data into the table and move the hdfs file    


    create external table a_atable location '/user/....';

    create external table balbal (user_id int)
    row formatted delimited    
    fields terminated by '\t'
    stored as textfile
    location '/user/....';
    -- (no tiene porque existir)

    -- drop de external no borra el hdfs


	select distinct substring(cast(column as string), 1,4) from table


## Extra commands

### Explain

Muestra el plan de ejecución de una query. Memoria de las fuentes, estimaciones de espacio, ...

La palabra EXTENDED muestra más información.

	EXPLAIN [EXTENDED|CBO|AST|DEPENDENCY|AUTHORIZATION|LOCKS|VECTORIZATION|ANALYZE] query


### STATS

Genera las estadísticas de toda la tabla (y de las particiones si tiene). Estas se muestran en los procesos EXPLAIN o en los SHOW.

La palabra INCREMENTAL hace que solo las nuevas particiones que no tengan stats generadas se calculen. Adicionalmente a este argumento se puede añadir PARTITION que especifica la partición sobre la que se quiere ejecutar las estadísticas (debe tener ambas palabras)

También se puede mostrar las stats por columna con column.
	
	COMPUTE [INCREMENTAL] STATS table [PARTITION x];

	SHOW table STATS table;
	SHOW column STATS table;


### SHOW

Muestra queries o información. Tiene usos muy variados.


	SHOW (DATABASES|SCHEMAS) [LIKE 'pattern'];
	SHOW TABLES [IN database_name] ['pattern'];
	SHOW VIEWS [IN/FROM database_name] [LIKE 'pattern'];	
	SHOW PARTITIONS table_name;
	SHOW PARTITIONS table_name PARTITION(partitinoned_column1='2010-03-03', partitinoned_column2='muu');
	SHOW TABLE EXTENDED [IN|FROM database_name] LIKE 'identifier_with_wildcards' [PARTITION(partition_spec)];
	SHOW CREATE TABLE ([db_name.]table_name|view_name);
	SHOW COLUMNS (FROM|IN) table_name [(FROM|IN) db_name];


### Describe

Muestra información de lo su que se le pida. No requiere de STATS procesadas ni nada previo.

	DESCRIBE DATABASE [EXTENDED] db_name;
	DESCRIBE SCHEMA [EXTENDED] db_name;
	DESCRIBE [EXTENDED|FORMATTED] table_name;
	DESCRIBE [EXTENDED|FORMATTED] table_name[col_name];
	DESCRIBE FORMATTED [db_name.]table_name column_name PARTITION (partition_spec);


### SET

Para definir o mostrar las variables 'de entorno propias'. Cambia la configuración o la muestra. Hay que mirar todo en detalle ya que algunos entornos como HUE solo lo cambian para la siguiente query.

	-- muestra todas las variables
	SET;
	-- establece una variable
	SET MEM_LIMIT=3g;
	-- muestra la variable
	SET MEM_LIMIT;

Se muestran también las creadas por el usuario y pasadas en la llamada:

	name=$(hive -S -e "select name from table;")
	hive -d name=$name -f new_query.hql

inside hql file:

	${name}


## Fechas


sELECT to_utc_timestamp ('1971-01-01 00:00:00','CET');


sELECT unix_timestamp(to_utc_timestamp ('2018-11-08T16:10:36Z','CET')) - unix_timestamp('2018-11-08 15:10:26');