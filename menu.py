def listar_menu():
  print('\n\nSelecione uma das opcoes:');
  print('1 - Inserir');
  print('2 - Consultar');
  print('3 - Excluir');
  print('\n\n');
  
  return input('Número da opção: ');

def listar_menu_consulta():
  print('\n\nSelecione uma das opcoes de consulta: ');
  print('1 - Por nome');
  print('2 - Por categoria');
  print('\n\n');
    
  return input('Número da opção: ');

def list_usuarios():
  print('\n\nSelecione a categoria deste usuário:');
  print('1 - Funcionários');
  print('2 - Voluntários');
  print('3 - Doadores');
  print('4 - Atendidos');
  print('5 - Visitantes');

  return input('\n\nDigite o código da categoria -> ');