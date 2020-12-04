from sqlite3 import connect
connection = connect('Q1.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS tipos_telefones ('
               'cod_tipo_telefone NUMBER (2) NOT NULL,'
               'descricao VARCHAR2 (20) NOT NULL,'
               'PRIMARY KEY (cod_tipo_telefone));')
cursor.execute('CREATE TABLE IF NOT EXISTS administradores ('
               'cod_administrador NUMBER (6) NOT NULL,'
               'nivel_privilegio NUMBER (1) NOT NULL,'
               'PRIMARY KEY (cod_administrador));')
cursor.execute('CREATE TABLE IF NOT EXISTS clientes_enderecos ('
               'cod_cliente NUMBER (6) NOT NULL,'
               'cod_endereco NUMBER (2) NOT NULL,'
               'data_cadastro DATE NOT NULL,'
               'PRIMARY KEY (cod_cliente));')
cursor.execute('CREATE TABLE IF NOT EXISTS produtos ('
               'cod_produto NUMBER (5) NOT NULL,'
               'titulo VARCHAR2 (200) NOT NULL,'
               'ano_lancamento DATE NOT NULL,'
               'importado CHAR (1) NOT NULL,'
               'preco NUMBER (10, 2) NOT NULL,'
               'prazo_entrega NUMBER (3) NOT NULL,'
               'PRIMARY KEY (cod_produto));')
cursor.execute('INSERT INTO tipos_telefones VALUES (37, "Telefone Fixo");')
cursor.execute('INSERT INTO administradores VALUES (234587, 3);')
cursor.execute('INSERT INTO clientes_enderecos VALUES (305184, 16, "04/12/2019");')
cursor.execute('INSERT INTO produtos VALUES (17594, "Cubo Mágico", "10/10/2020", "S", "70.00", 120);')
cursor.execute('SELECT descricao FROM tipos_telefones;')
connection.commit()
connection = connect('Q2.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS estados('
               'uf CHAR (2) NOT NULL,'
               'nome VARCHAR2 (20) NOT NULL,'
               'regiao CHAR (2) NOT NULL,'
               'PRIMARY KEY (uf));')
cursor.execute('CREATE TABLE IF NOT EXISTS usuarios('
               'cod_usuario NUMBER (6) NOT NULL,'
               'nome VARCHAR2 (100) NOT NULL,'
               'cpf CHAR (11) NOT NULL,'
               'email VARCHAR2 (40) NOT NULL,'
               'username VARCHAR2 (20) NOT NULL,'
               'password VARCHAR2 (20) NOT NULL,'
               'PRIMARY KEY (cod_usuario));')
cursor.execute('CREATE TABLE IF NOT EXISTS cidades('
               'cod_cidade NUMBER (4) NOT NULL,'
               'nome VARCHAR2 (40) NOT NULL,'
               'uf CHAR (2) NOT NULL,'
               'PRIMARY KEY (cod_cidade));')
cursor.execute('CREATE TABLE IF NOT EXISTS pedidos_produtos('
               'num_pedido NUMBER (7) NOT NULL,'
               'cod_produto NUMBER (5) NOT NULL,'
               'quantidade NUMBER (3) NOT NULL,'
               'valor_unitario NUMBER (10, 2) NOT NULL,'
               'PRIMARY KEY (num_pedido));')
cursor.execute('INSERT INTO estados VALUES ("MS", "Mato Grosso do Sul", "CO");')
cursor.execute('INSERT INTO usuarios VALUES (489245, "Bender Bending Rodriguez", "85975647821",'
               '"bender@gmail.com", "Bender", "naoprecisodebebida");')
cursor.execute('INSERT INTO cidades VALUES (1337, "Cascavel", "PR");')
cursor.execute('INSERT INTO pedidos_produtos VALUES (1497562, 47274, 12, 36.99);')
cursor.execute('SELECT password FROM usuarios;')
connection.commit()
connection = connect('Q3.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS enderecos('
               'cod_endereco NUMBER (2) NOT NULL,'
               'rua VARCHAR2 (30) NOT NULL,'
               'numero NUMBER (5) NOT NULL,'
               'complemento VARCHAR2 (20) NOT NULL,'
               'cod_cidade NUMBER (4) NOT NULL,'
               'cep CHAR (8) NOT NULL,'
               'PRIMARY KEY (cod_endereco));')
cursor.execute('CREATE TABLE IF NOT EXISTS telefones('
               'cod_cliente NUMBER (6) NOT NULL,'
               'cod_telefone NUMBER (2) NOT NULL,'
               'cod_tipo_telefone NUMBER (2) NOT NULL,'
               'ddd NUMBER (3) NOT NULL,'
               'numero VARCHAR2 (10) NOT NULL,'
               'PRIMARY KEY (cod_cliente));')
cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
               'cod_cliente NUMBER (6) NOT NULL,'
               'data_nascimento DATE,'
               'data_cadastro DATE NOT NULL,'
               'PRIMARY KEY (cod_cliente));')
cursor.execute('INSERT INTO enderecos VALUES (87, "Samaritano", 15523, "7° andar", 1337, "54128965");')
cursor.execute('INSERT INTO telefones VALUES (478953, 54, 12, 041, "40028922");')
cursor.execute('INSERT INTO clientes VALUES (531487, "12/12/2001", "08/03/2018");')
cursor.execute('SELECT data_nascimento FROM clientes;')
connection.commit()
connection = connect('Q4.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS autores('
               'cod_autor NUMBER (4) NOT NULL,'
               'nome VARCHAR2 (100) NOT NULL,'
               'descricao VARCHAR2 (1024),'
               'PRIMARY KEY (cod_autor));')
cursor.execute('CREATE TABLE IF NOT EXISTS pedidos('
               'num_pedido NUMBER (7) NOT NULL,'
               'cod_cliente NUMBER (6) NOT NULL,'
               'cod_endereco NUMBER (2) NOT NULL,'
               'data_emissao DATE NOT NULL,'
               'PRIMARY KEY (num_pedido));')
cursor.execute('CREATE TABLE IF NOT EXISTS autores_pedidos('
               'cod_autor NUMBER (4) NOT NULL,'
               'cod_produto NUMBER (5) NOT NULL);')
cursor.execute('INSERT INTO autores VALUES (1337, "Felipe Pereira",'
               '"Crie malwares escritos em Python para qualquer plataforma desktop!");')
cursor.execute('INSERT INTO pedidos VALUES (2547883, 331253, 64, "04/12/2020");')
cursor.execute('INSERT INTO autores_pedidos VALUES (1337, 59877);')
cursor.execute('SELECT nome FROM autores;')
connection.commit()
