# general_utils

    hive -S -e "set" |grep warehouse;
    hive -f /home/user.../.file.hql

hive> 

	show databases like 'm*';
	create database if not exists Movies_data comment 'Data of the movies';
	create database test location '/user/fake_directory
	describe database una_database;
	create table testtable( col1 int);
	drop database test_databse;
	drop database test_database cascade;


	! pwd
	! ls
	dfs -ls /;


inside database

    set hive.cli.print.current.db=true;

    create table balbal (user_id int)
    row formatted delimited	
    fields terminated ny '|'
    stored as textfile;	

    decribe formatted a_table;
    load data inpath '/user/.../file' overwrite into table a_table; # loads data into the table and move the hdfs file	


    create external table a_atable location '/user/....'
    create external table balbal (user_id int)
    row formatted delimited	
    fields terminated ny '\t'
    stored as textfile
    location '/user/....';
        (no tiene porque existir)

    drop de external no borra el hdfs 