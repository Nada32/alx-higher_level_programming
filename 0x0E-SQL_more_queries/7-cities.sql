-- sql.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
	state_id int NOT NULL ,
	name varchar(256) NOT NULL, UNIQUE id,
	FORIGN KEY (state_id) REFERENCES states(id));
