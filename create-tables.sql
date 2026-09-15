-- Active: 1788283817873@@127.0.0.1@5432@restaurante_japones
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    telefone VARCHAR(20)
);

CREATE TABLE cardapio (
    id SERIAL PRIMARY KEY,
    descricao VARCHAR(100),
    valor DECIMAL(10,2)
);
CREATE TABLE funcionarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    cargo VARCHAR(50),
    telefone VARCHAR(20)
);
CREATE TABLE categoria (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50)
);
CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER,
    funcionarios_id INTEGER,
    total DECIMAL(10,2),
    data TIMESTAMP,
    status VARCHAR(20)
);
CREATE TABLE itens (
    id SERIAL PRIMARY KEY,
    cardapio_id INTEGER,
    pedidos_id INTEGER,
    categoria_id INTEGER,
    mesas_id INTEGER,
    quantidade INTEGER
);
CREATE TABLE mesas (
    id SERIAL PRIMARY KEY,
    numero INTEGER,
    capacidade INTEGER,
    status VARCHAR(20)
);