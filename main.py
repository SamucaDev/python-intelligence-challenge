import usuario as usuario
import menu 
import mensagem_customizada

def listInformationUser(usuario):
  print('\nLista de usuarios cadastrados:\n');
  
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

mensagem_customizada.bem_vindo();

usuarios = [];

while True:
  option = menu.listar_menu();

  if option == '1':
    usuarios = usuario.registrar_usuario(usuarios);

    if len(usuarios) == 0:
      print('Nenhum usuario cadastrado');
    else:
      for x in usuarios:
        listInformationUser(x)

    voltar_menu = input('\n\nDeseja voltar para o menu?\nDigite 1 para sim, e 0 para Não -> ');
    if(voltar_menu == '0'):
      break; 

  if option == '2':
    if len(usuarios) == 0:
        print('Ainda nao ha usuarios cadastrados. Volte para opções');
    else:
      resultado_pesquisa = [];

      opticao_consulta = menu.listar_menu_consulta();

      if opticao_consulta == '2':
        categoria = menu.list_usuarios();

        for _usuario in usuarios:
          if  categoria in _usuario['categorias']:
            resultado_pesquisa.append(_usuario);
      
      if opticao_consulta == '1':
        nome = input('Digite o nome que esta pesquisando, conforme ele foi registrado -> ')
        for _usuario in usuarios:
          if  nome in _usuario['name']:
            resultado_pesquisa.append(_usuario);

      print(resultado_pesquisa); 
      for y in resultado_pesquisa:
        listInformationUser(y);
      # FAZER AQUI A PARADA DE LISTAR A PARADA
      
      voltar_menu = input('\n\nDeseja voltar para o menu?\nDigite 1 para sim, e 0 para Não -> ');
      if(voltar_menu == '0'):
        break;  


