-- Buat Database
create database flaskapp;
-- drop database flaskapp;

-- Use Database
use flaskapp;

-- Buat Tabel Jam
create table jam_new (instant smallint, dteday date, season char(10), yr varchar(20), mnth varchar(20), hr tinyint, holiday varchar(20), weekday varchar(20), 
workingday varchar(20), weathersit varchar(30), temp float, atemp float, hum float, windspeed float, casual smallint, registered smallint, cnt smallint, event char(10));

desc jam_new;
drop table jam_new;

-- Untuk cari tau di mana directory untuk menyimpan data 
SHOW VARIABLES LIKE 'secure_file_priv';

-- Pindah file ke directory tersebut

-- lalu run query ini untuk mengimport data
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\new_hour.csv'
INTO TABLE jam_new
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;