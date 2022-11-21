create table wokers(
    id varchar(10) primary key not null,
    nameWorker varchar(90) not null,
    phone varchar(10) unique,
    designation varchar(20) not null
);