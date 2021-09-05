import usuario as usuario
import menu 
import mensagem_customizada

mensagem_customizada.bem_vindo();

usuarios = [];

while True:
  option = menu.listar_menu();

  if option == '1':
    usuarios = usuario.registrar_usuario(usuarios);

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
      
      voltar_menu = input('\n\nDeseja voltar para o menu?\nDigite 1 para sim, e 0 para Não -> ');
      if(voltar_menu == '0'):
        break;  


       #encontrar a rapaziada
       #Pode nao ter registro na parada
       #Pode nao encontrar
       #Pode encontrar 2

    


# print(usuarios);

