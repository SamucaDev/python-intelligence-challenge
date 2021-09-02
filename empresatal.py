def selecionar_categoria():
  categorias = [];
  while True:
    print('\n\nSelecione a categoria deste usuário:');
    print('1 - Funcionários');
    print('2 - Voluntários');
    print('3 - Doadores');
    print('4 - Atendidos');
    print('5 - Visitantes');

    categoria = input('\n\nDigite o código da categoria -> ');

    problem = 1;

    if categoria == '3' or categoria == '1':
      if '4' in categorias:
        problem = 0
    
    if categoria == '4':
      if '3' in categorias or '1' in categorias:
        problem = 0
    
    print(problem);
    if problem == 0:
      print('\n\nOs Atendidos não podem ser doadores ou funcionários.\nInsira outro código de categoria')
    else:
      categorias.append(categoria);

    proxima_categoria = input('\n\nDeseja inserir mais uma categoria?\nDigite 1 para sim, e 0 para Não -> ');

    if(proxima_categoria == '0'):
      return categorias;

def inserir_dados():
  categorias         = selecionar_categoria();
  name               = input('\n\nDigite seu nome: ');
  data_de_nascimento = input('Digite sua data de nascimento: ');
  email              = input('Digite seu email: ');
  cpf                = input('Digite seu cpf: ');
  rg                 = input('Digite seu rg: ');
  numero_filhos      = input('Digite quantos filhos voce tem: ');

  usuarios.append({
    'name'              : name,
    'data_de_nascimento': data_de_nascimento,
    'email'             : email,
    'cpf'               : cpf,
    'rg'                : rg,
    'numero_filhos'     : numero_filhos,
    'categorias'        : categorias
  });

  return input('\n\nDeseja cadastrar outra pessoal?\nDigite 1 para sim, e 0 para Não -> ');

def registrar_usuario():
  while True:
    if(inserir_dados() == '0'):
      break;


print(' ____                            _           _       ');
print('| __ )  ___ _ __ ___      __   _(_)_ __   __| | ___  ');
print("|  _ \ / _ \ '_ ` _ \ ____\ \ / / | '_ \ / _` |/ _ \ ");
print('| |_) |  __/ | | | | |_____\ V /| | | | | (_| | (_) |');
print('|____/ \___|_| |_| |_|      \_/ |_|_| |_|\__,_|\___/ ');
print('\n\n');


usuarios = [];

while True:
  print('\n\nSelecione uma das opcoes:');
  print('1 - Inserir');
  print('2 - Consultar');
  print('3 - Excluir');
  print('\n\n');
  
  option = input('Número da opção: ');

  if option == '1':
    registrar_usuario();

    voltar_menu = input('\n\nDeseja voltar para o menu?\nDigite 1 para sim, e 0 para Não -> ');
    if(voltar_menu == '0'):
      break;  

print(usuarios);
#METODOS


