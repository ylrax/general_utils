# Basic commands


## Sources:

 Instalable:
 http://www.enterprisedb.com/products-services-training/pgdownload
 Portable:
 https://sourceforge.net/projects/postgresqlportable/

## Show databases:

	 \l
	 CREATE USER me WITH PASSWORD 'me';

## Start

	create database testing OWNER me;
	\c testing
	\l

## Show tables inside the database

	\d

## Creation of new content

	create table table1 (id int, col1 int, col2 varchar, col3 timestamp);
	create table table2 (id int, cool1 int, cool2 varchar);
	insert into table1 values(1,2,'a',    '2016-01-01');  --comillas simples
	insert into table1 values(2,4,'aa',   '2017-01-01');
	insert into table1 values(3,6,'aaa',  '2016-02-01');
	insert into table1 values(4,8,'aaaa', '2016-01-10');
	insert into table2 values(1,3,'b');
	insert into table2 values(1,3333,'  b  ');
	insert into table2 values(2,5,'bb');
	insert into table2 values(3,7,'bbb');
	insert into table2 values(4,9,'bbbb');
	insert into table2 values(5,11,NULL);


	select * from table1 as one inner join table2 as two on one.id=two.id;


	select  row_number() over(partition by t.len order by t.cool2  DESC) as counter, * from (select *,length(cool2) as len from table2) as t;

	select  rank() over (order by id ASC) as rank,*  from table2;


## Python connector:

	import psycopg2
	import pandas.io.sql as psql

	connection = psycopg2.connect(host='localhost', database='testing', user='me', password='me')
	cursor = connection.cursor()
	cursor.execute('select * from table1')
	for query in cursor:
	    print(str(query))


	# get connected to the database

	df = psql.read_sql("SELECT * FROM table1", connection)
	print(df)


## Others

	select col1, col2 from test 
	group by col1,col2 having count(*) >1 and max( CASE col2 WHEN '1' THEN 1 ELSE 0 END ) = 0;

	select case when coalesce(cool2, '') = '' then 'fake' else 'no fake' end from table2;
	

	select * from (select * from table2 as one left join table1 as two on one.id=two.id) as foo where foo.cool1 != (select max(cool1) from table2);


	select
	  nack.val2,
	  split_part(split_part(nack.val, ';', numbers.n), ';', 1) val
	from
	  (select 1 n 
	  union all
	   select 2 
	   union all 
	   select 3 
	   union all
	   select 4 
	   union all 
	   select 5) numbers INNER JOIN nack
	  on CHAR_LENGTH(nack.val) -CHAR_LENGTH(REPLACE(nack.val, ';', ''))>=numbers.n-1
	order by
	  val2, n

	  select id, cool1, cool2 from (select * from (select row_number() over(partition by id order by id DESC) as num, * from table2) aux where num=1) aux2;
	  