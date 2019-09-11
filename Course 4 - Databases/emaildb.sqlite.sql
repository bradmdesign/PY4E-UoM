BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Users" (
	"name"	VARCHAR(128),
	"email"	VARCHAR(128)
);
INSERT INTO "Users" VALUES ('Hey','Fakeemail@test.com');
INSERT INTO "Users" VALUES ('Brad','Bradm89@hotmail.com');
INSERT INTO "Users" VALUES ('Tester','Test@testing.com');
COMMIT;
