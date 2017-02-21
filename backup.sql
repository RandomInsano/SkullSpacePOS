PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE product (
	id INTEGER NOT NULL, 
	parent_id INTEGER, 
	upc VARCHAR, 
	name VARCHAR, 
	cost FLOAT, 
	qty INTEGER, 
	contains_qty INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(parent_id) REFERENCES product (id)
);
INSERT INTO "product" VALUES(1,NULL,'069000070000','Brisk Lemonaide (355ml)',1.0,1,1);
INSERT INTO "product" VALUES(2,NULL,'096619818136','Kirkland Mircowave Popcorn (1x)',1.0,1,1);
INSERT INTO "product" VALUES(3,NULL,'06942508','Pepsi (355ml)',1.0,1,1);
INSERT INTO "product" VALUES(4,NULL,'069000014257','Diet Pepsi (355ml)',1.0,1,1);
INSERT INTO "product" VALUES(5,NULL,'05492935','Dr. Pepper (355ml)',1.0,1,1);
INSERT INTO "product" VALUES(6,NULL,'077290902765','Pearson''s Mint Patties',0.25,1,1);
INSERT INTO "product" VALUES(7,NULL,'06224017','Canada Dry Ginger Ale (355ml)',1.0,1,1);
INSERT INTO "product" VALUES(8,NULL,'06541432','7up (355ml)',1.0,1,1);
CREATE TABLE user (
	id VARCHAR NOT NULL, 
	name VARCHAR, 
	email VARCHAR, 
	is_admin BOOLEAN, 
	PRIMARY KEY (id), 
	CHECK (is_admin IN (0, 1))
);
CREATE TABLE purchase (
	id INTEGER NOT NULL, 
	date DATETIME, 
	qty INTEGER, 
	cost FLOAT, 
	user INTEGER, 
	product INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user) REFERENCES user (id), 
	FOREIGN KEY(product) REFERENCES product (id)
);
COMMIT;
