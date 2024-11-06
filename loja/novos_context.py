from django.template.context_processors import request

from loja.models import Produto, Pedido, ItensPedido

def carrinho(request):
    quantidade_produtos_carrinho = 0
    
    try:
        if request.user.is_authenticated:
            cliente = request.user.cliente
            pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False)
            itens_pedido = ItensPedido.objects.filter(pedido=pedido)
            quantidade_produtos_carrinho = sum(item.quantidade for item in itens_pedido)
        else:
            # Para usuários não autenticados, você pode:
            # 1. Usar sessões para armazenar o carrinho
            # 2. Ou simplesmente retornar 0 como quantidade
            print('nao logado')
            
    except Exception as e:
        print(f'Erro ao processar carrinho: {str(e)}')
    
    return {'quantidade_produtos_carrinho': quantidade_produtos_carrinho}


