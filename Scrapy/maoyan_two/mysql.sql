create table movie(
  movie_id integer auto_increment primary key,
  name varchar(512) not null ,
  actor varchar(512),
  release_time varchar(512),
  score varchar(32)
)engine=innodb default charset=utf8;


create table yaoqi(
  yaoqi_id integer auto_increment primary key,
  comic_id varchar(512) not null ,
  name varchar(512),
  cover varchar(1024),
  category varchar(512)
)engine=innodb default charset=utf8;


