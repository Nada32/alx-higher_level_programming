-- sql.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id int NOT NULL AUTO_INCREAMENT,
	state_id int NOT NULL ,
	name varchar(256) NOT NULL, UNIQUE id, PRIMARY KEY (id),
	FORIGN KEY (state_id));
