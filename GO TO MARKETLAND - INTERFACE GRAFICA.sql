create database GoTomarketland;

create table usuarios(

id int auto_increment primary key,
nome varchar(50),
sobrenome varchar(50),
usuario varchar(80),
senha varchar(50)

);


insert into usuarios (nome, sobrenome, usuario, senha) values ('andre', 'simao', 'zemildo', '123')




create table produtos(

	id int auto_increment primary key,
	produto varchar(300),
    marca varchar(300),
    mercado varchar(300),
	preco float
    
);

create table mercados(


	id int auto_increment primary key,
    mercado varchar(500),
    endereço varchar(500)
    



);

create table japão(

	id int auto_increment primary key,
    produto varchar(3000),
    marca varchar(3000),
    tipo varchar(3000),
    preco float
    
	


);


create table carrinho(

	id int auto_increment primary key,
    produto varchar(3000),
    marca varchar(3000),
    tipo varchar(3000),
    preco float


);

create table teste(

	id int auto_increment primary key,
    produto varchar(3000),
    marca varchar(3000),
    tipo varchar(3000),
    preco float

	

);

insert into carrinho (produto, marca, tipo, preco) values ('carro', 'jove','ferrugem', 123);

insert into japão (produto, marca, tipo, preco) values('carro', 'jove', 'ferrugem',  12);

drop table japão;