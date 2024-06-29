### show databases;

### use pythondb;

### select * from user;

### show columns from user;

### describe user;

### alter table user add column avatar varchar(45) default null;

## CREATE TABLE roles(
###    -> id INT AUTO_INCREMENT PRIMARY KEY,
###    -> title VARCHAR(255) NOT NULL
###    -> );

## ALTER TABLE user
###    -> ADD COLUMN role_id INT,
###    -> ADD CONSTRAINT role_id
###    -> FOREIGN KEY (role_id) REFERENCES roles(id)
###    -> ON UPDATE CASCADE
###    -> ON DELETE CASCADE;

### describe roles;

## INSERT INTO roles (title)
###    -> VALUES ('superadmin')
###    -> ;

## UPDATE user
###    -> SET role_id = 1
###    -> WHERE id = 3;

## CREATE TABLE endpoints (id INT AUTO_INCREMENT PRIMARY KEY, endpoint VARCHAR(100) NOT NULL, methods VARCHAR(20) NOT NULL);

### describe endpoints;

### select * from endpoints;

## INSERT INTO endpoints (endpoint, methods) VALUES ('/user/addone', 'POST');

## create table accessibility (id INT AUTO_INCREMENT PRIMARY KEY, endpoint_id INT, roles LONGTEXT NOT NULL, FOREIGN KEY (endpoint_id) REFERENCES endpoints(id));

### describe accessibility;

### INSERT INTO accessibility (endpoint_id, roles) VALUES(1, 7);

### INSERT INTO roles(title) VALUES('Moderator');

### INSERT INTO accessibility (endpoint_id, roles) VALUES(2, JSON_ARRAY(7,8,9));

##  create view accessibility_view as select endpoints.endpoint, accessibility.roles from endpoints join accessibility where endpoints.id = accessibility.endpoint_id;

### SELECT * FROM accessibility_view;

### update user set role_id = 7 where id = 2;