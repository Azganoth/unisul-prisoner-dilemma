from socketserver import ThreadingMixIn
from xmlrpc.server import SimpleXMLRPCServer
from typing import Optional


# Permitir a resolução paralela de múltiplas requisições
class ThreadingXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass


# Definir ponto de acesso
HOST = 'localhost'
PORT = 8000

prisoner_1_testimony: Optional[bool] = None
prisoner_2_testimony: Optional[bool] = None

with ThreadingXMLRPCServer((HOST, PORT)) as server:
    @server.register_function(name='testify')
    def judge(testimony: bool):
        """Recebe o testemunho de um prisioneiro e aguarda o testemunho
        de outro prisioneiro para realizar o julgamento de cada um.
        """
        global prisoner_1_testimony, prisoner_2_testimony

        # Reiniciar as duas variáveis de testemunho caso as duas já tenham sido modificadas
        if prisoner_1_testimony is not None and prisoner_2_testimony is not None:
            prisoner_1_testimony, prisoner_2_testimony = None, None

        # Guarda o testemunho do prisioneiro
        if prisoner_1_testimony is None:
            prisoner_1_testimony = testimony
        elif prisoner_2_testimony is None:
            prisoner_2_testimony = testimony

        # Aguarda o testemunho de dois prisioneiros
        while prisoner_1_testimony is None or prisoner_2_testimony is None:
            pass

        # Julga cada prisioneiro pelo seu testemunho
        if prisoner_1_testimony == True and prisoner_2_testimony == True:
            return '5 anos'
        elif prisoner_1_testimony == True and prisoner_2_testimony == False:
            return 'liberdade' if testimony == prisoner_1_testimony else '10 anos'
        elif prisoner_1_testimony == False and prisoner_2_testimony == True:
            return '10 anos' if testimony == prisoner_1_testimony else 'liberdade'
        else:
            return '6 meses'

    print(f'O juíz está aguardando o testemunho dos prisioneiros em http://{HOST}:{PORT}.')
    try:
        # Iniciar o servidor e mantê-lo executando até uma interrupção
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nO juíz ficou impaciente...')
        raise SystemExit
