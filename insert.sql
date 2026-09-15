-- =========================
-- CLIENTES
-- =========================

INSERT INTO clientes (nome, telefone)
VALUES
('Maria', '99999-1111'),
('Luiz', '99999-2222'),
('Larissa', '99999-3333'),
('Rosolem', '99999-4444'),
('Jaison', '99999-5555'),
('Fernando', '99999-6666');


-- =========================
-- FUNCIONARIOS
-- =========================

INSERT INTO funcionarios (nome, cargo, telefone)
VALUES
('Ana', 'Garçonete', '98888-1111'),
('Pedro', 'Garçom', '98888-2222'),
('Julia', 'Caixa', '98888-3333'),
('Carlos', 'Gerente', '98888-4444');


-- =========================
-- CATEGORIA
-- =========================

INSERT INTO categoria (nome)
VALUES
('Sushi'),
('Temaki'),
('Pratos Quentes'),
('Bebidas'),
('Sobremesas');


-- =========================
-- CARDAPIO
-- =========================

INSERT INTO cardapio (descricao, valor)
VALUES
('Sushi de Salmão', 28.90),
('Sushi de Atum', 26.90),
('Temaki de Salmão', 24.90),
('Temaki de Atum', 22.90),
('Yakisoba', 32.90),
('Guioza', 19.90),
('Refrigerante', 6.00),
('Água', 4.00),
('Sushi Doce', 12.90); 


-- =========================
-- MESAS
-- =========================

INSERT INTO mesas (numero, capacidade, status)
VALUES
(1, 2, 'Livre'),
(2, 4, 'Ocupada'),
(3, 4, 'Livre'),
(4, 6, 'Reservada'),
(5, 2, 'Livre'),
(6, 8, 'Ocupada');


-- =========================
-- PEDIDOS
-- =========================

INSERT INTO pedidos (cliente_id, funcionarios_id, total, data, status)
VALUES
(1, 1, 53.80, '2026-09-15 12:30:00', 'Entregue'),
(2, 2, 32.90, '2026-09-15 13:00:00', 'Em preparo'),
(3, 3, 47.80, '2026-09-15 13:20:00', 'Pendente'),
(4, 1, 24.90, '2026-09-15 14:00:00', 'Entregue'),
(5, 2, 38.80, '2026-09-15 18:30:00', 'Em preparo');


-- =========================
-- ITENS
-- =========================

INSERT INTO itens (cardapio_id, pedidos_id, categoria_id, mesas_id, quantidade)
VALUES
(1, 1, 1, 2, 1),
(7, 1, 4, 2, 1),
(3, 2, 2, 3, 1),
(5, 3, 3, 4, 1),
(6, 3, 3, 4, 1),
(3, 4, 2, 5, 1),
(8, 5, 4, 6, 1),
(9, 5, 5, 6, 2);