# Postgres database


Example:

    \l
    \d
    create database testing;
    \c testing
    \l
    \d
    create table table1 (id int, col1 int, col2 varchar);
    create table table2 (id int, cool1 int, cool2 varchar);
    insert into table1 values(1,2,'a');
    insert into table1 values(2,4,'aa');
    insert into table1 values(3,6,'aaa');
    insert into table1 values(4,8,'aaaa');
    insert into table2 values(1,3,'b');
    insert into table2 values(1,3333,'  b  ');
    insert into table2 values(2,5,'bb');
    insert into table2 values(3,7,'bbb');
    insert into table2 values(4,9,'bbbb');
    insert into table2 values(5,11,'bbbbb');
    insert into table1 values(1,2,'a');
    insert into table1 values(2,4,'aa');
    insert into table1 values(3,6,'aaa');
    insert into table1 values(4,8,'aaaa');
    insert into table2 values(1,3,'b');
    insert into table2 values(1,3333,'  b  ');
    insert into table2 values(2,5,'bb');
    insert into table2 values(3,7,'bbb');
    insert into table2 values(4,9,'bbbb');
    insert into table2 values(5,11,'bbbbb');


Other:

     select
      nack.val2,
      split_part(split_part(nack.val, ';', numbers.n), ';', 1) val
    from
      (select 1 n union all
       select 2 union all select 3 union all
       select 4 union all select 5) numbers INNER JOIN nack
      on CHAR_LENGTH(nack.val)
         -CHAR_LENGTH(REPLACE(nack.val, ';', ''))>=numbers.n-1
    order by
      val2, n
