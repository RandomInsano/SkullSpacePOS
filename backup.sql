PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE user (
	id VARCHAR NOT NULL, 
	name VARCHAR, 
	email VARCHAR, 
	is_admin BOOLEAN, 
	PRIMARY KEY (id), 
	CHECK (is_admin IN (0, 1))
);
CREATE TABLE product (
	id INTEGER NOT NULL, 
	upc VARCHAR, 
	name VARCHAR, 
	cost FLOAT, 
	qty INTEGER, 
	PRIMARY KEY (id)
);
INSERT INTO "product" VALUES(1,'069000070000','Brisk Lemonaide (355ml)',1.0,1);
INSERT INTO "product" VALUES(2,'096619818136','Kirkland Mircowave Popcorn',1.0,1);
INSERT INTO "product" VALUES(3,'06942508','Pepsi (355ml)',1.0,1);
INSERT INTO "product" VALUES(4,'069000014257','Diet Pepsi (355ml)',1.0,1);
INSERT INTO "product" VALUES(5,'05492935','Dr. Pepper (355ml)',1.0,1);
INSERT INTO "product" VALUES(6,'077290902765','Pearson''s Mint Patties',0.25,1);
INSERT INTO "product" VALUES(7,'06224017','Canada Dry Ginger Ale (355ml)',1.0,1);
INSERT INTO "product" VALUES(8,'06541432','7up (355ml)',1.0,1);
INSERT INTO "product" VALUES(9,'058496839604','Skittles Original (36x61g)',0.0,1);
INSERT INTO "product" VALUES(10,'06782900','Coke (355ml)',1.0,1);
INSERT INTO "product" VALUES(11,'071117618082','Baja Cafe (Beef & Bean / Bean & Cheese 24x)',0.0,1);
INSERT INTO "product" VALUES(12,'071117011340','Baja Cafe Beef & Bean Burrito',1.0,1);
INSERT INTO "product" VALUES(13,'071117011302','Baja Cafe Bean & Cheese Burrito',1.0,1);
INSERT INTO "product" VALUES(14,'096619818143','Kirkland Microwave Popcorn (44x)',0.0,1);
INSERT INTO "product" VALUES(15,'063209072377','Tim Hortons Dark Roast Cups',0.25,5);
INSERT INTO "product" VALUES(16,'063209057282','Tim Hortons Original Cups',0.25,1);
CREATE TABLE contains_product (
	parent_id INTEGER NOT NULL, 
	contains_id INTEGER NOT NULL, 
	qty INTEGER, 
	PRIMARY KEY (parent_id, contains_id), 
	FOREIGN KEY(parent_id) REFERENCES product (id), 
	FOREIGN KEY(contains_id) REFERENCES product (id)
);
INSERT INTO "contains_product" VALUES(11,12,12);
INSERT INTO "contains_product" VALUES(11,13,12);
INSERT INTO "contains_product" VALUES(14,2,44);
INSERT INTO "contains_product" VALUES(15,15,14);
INSERT INTO "contains_product" VALUES(16,16,14);
CREATE TABLE "transaction" (
	id INTEGER NOT NULL, 
	date DATETIME, 
	user INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user) REFERENCES user (id)
);
CREATE TABLE purchase (
	id INTEGER NOT NULL, 
	qty INTEGER, 
	cost FLOAT, 
	product INTEGER, 
	"transaction" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(product) REFERENCES product (id), 
	FOREIGN KEY("transaction") REFERENCES "transaction" (id)
);
COMMIT;
