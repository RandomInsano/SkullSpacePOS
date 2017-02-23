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
INSERT INTO "product" VALUES(9,NULL,'058496839604','Skittles Original (36x61g)',0.0,1,1);
INSERT INTO "product" VALUES(10,NULL,'06782900','Coke (355ml)',1.0,1,1);
INSERT INTO "product" VALUES(11,NULL,'071117618082','Baja Cafe (Beef & Bean / Bean & Cheese 24x)',0.0,1,1);
INSERT INTO "product" VALUES(12,NULL,'071117011302','Baja Cafe Beef & Bean Burrito',1.0,1,1);
INSERT INTO "product" VALUES(13,NULL,'07117011302','Baja Cafe Bean & Cheese Burrito',1.0,1,1);
INSERT INTO "product" VALUES(14,NULL,'096619818143','Kirkland Microwave Popcorn (44x)',0.0,1,1);
INSERT INTO "product" VALUES(15,NULL,'063209072377','Tim Hortons Dark Roast Cups',0.25,5,1);
INSERT INTO "product" VALUES(16,NULL,'063209057282','Tim Hortons Original Cups',0.25,1,1);
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
