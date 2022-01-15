-- create mysql schema
create database if not exists esps;


-- create investment varieties info
create table if not exists `investment_varieties_info` (
    `id` int unsigned auto_increment primary key comment '唯一id',
    `variety` varchar(100) default null comment '所属投资品类别',
    `code` varchar(100) default null comment '代码，如股票代码',
    `name` varchar(100) not null comment '名称，如股票名称',
    `industry` varchar(100) default null comment '所属行业，可能属于多个行业，用;分开',
    `is_huge` varchar(100) default null comment '是否属于行业龙头',
    `rank_of_industry` varchar(100) default null comment '所属行业排名，用;分开',
    `investing_class` varchar(100) default null comment '投资品类别:权益、固收、现金等'
);

-- temp sql
show tables;
desc investment_varieties_info;