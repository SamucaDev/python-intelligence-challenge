#TO DO:
# Verificar se a categoria ja existe na parada
import avl
import menu;
def selecionar_categoria():
  categorias = [];
  while True:
    categoria = menu.list_usuarios();

    problem = 1;

    if categoria == '3' or categoria == '1':
      if '4' in categorias:
        problem = 0
    
    if categoria == '4':
      if '3' in categorias or '1' in categorias:
        problem = 0
  
    if problem == 0:
      print('\n\nOs Atendidos não podem ser doadores ou funcionários.\nInsira outro código de categoria')
    else:
      categorias.append(categoria);

    proxima_categoria = input('\n\nDeseja inserir mais uma categoria?\nDigite 1 para sim, e 0 para Não -> ');

    if(proxima_categoria == '0'):
      return categorias;

def inserir_dados(usuarios, no):
  categorias         = selecionar_categoria();
  name               = input('\n\nDigite seu nome: ');
  data_de_nascimento = input('Digite sua data de nascimento: ');
  email              = input('Digite seu email: ');
  cpf                = input('Digite seu cpf: ');
  rg                 = input('Digite seu rg: ');
  numero_filhos      = input('Digite quantos filhos voce tem: ');

  usuario = {
    'name'              : name,
    'data_de_nascimento': data_de_nascimento,
    'email'             : email,
    'cpf'               : cpf,
    'rg'                : rg,
    'numero_filhos'     : numero_filhos,
    'categorias'        : categorias
  };

  usuarios.append(usuario);

  outro_usuario = input('\n\nDeseja cadastrar outra pessoal?\nDigite 1 para sim, e 0 para Não -> ')

  return [
    outro_usuario,
    usuarios
  ];

def registrar_usuario(usuarios, no):
  while True:
    if(inserir_dados(usuarios,no)[0] == '0'):
      return usuarios;

def listInformationUser(usuario):
  print('\nLista de usuarios cadastrados:');
  print('========================================\n');
  print('Nome: ' + usuario['name']);
  print('Email: ' + usuario['email']);
  print('Data de nascimento ' + usuario['data_de_nascimento']);
  print('CPF: ' + usuario['cpf']);
  print('RG: ' + usuario['rg']);
  print('Numero de filhos: ' + usuario['numero_filhos']);
  print('\nCategorias:\n')

  for y in usuario['categorias']:
    if y == '1':
      print('- Funcionários');
    if y == '2':
      print('- Voluntários');
    if y == '3':
      print('- Doadores'); 
    if y == '4':
      print('- Atendidos');
    if y == '5':
      print('- Visitantes');

  print('\n========================================');