### Autor:
Diogo Fernandes 
201503723

### Trabalho 1 Sistemas Distribuidos

Nesta pasta encontra-se o primeiro trabalho de Sistemas Distribuidos mais o código que vem com os projetos de grpc.

O source code realizado por mim encontra-se na pasta Trabalho.

O trabalho foi realizado em python e foi sempre executado em python3.

Na pasta protos, encontra-se o ficheiro .proto utilizado na implementação de grpc.
Para qualquer alteração do ficheiro correr o comando na pasta trab_SD/pubsub

`$ python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/helloworld.proto`

***

Na pasta trab_SD/pubsub encontram-se os ficheiros principais:

- pubsusb_server.py

O broker requesitado no trabalho.
Tem a possibilidade de registar e autenticar um subscritor
Lidar com os pedidos de subscrição ou desubscrição de um subscritor.
Enviar as mensagens antigas ou as correntes para o subscritor
Receber as mensagens do publisher e enviar diretamente para todos os subscritores ativos ou guardar para os não ativos.
Capacidade de tracking dos subscritores ativos.
Regista de qual terminal veio a mensagem e o número interno iterativo,


- subscriber.py

O subscritor, que subscreve às tags, e vai realizando pull de novas mensagens, e tem também a possibilidade de ir buscar mensagens antigas dando um T de horas.
Pode requisitar as tags no inicio após a sua autenticação.

- publisher.py

Envia as mensagens para o servidor num intervalo conforme a distribuição de Poisson.
O publisher pode requisitar a lista de tags disponiveis no inicio de execução.
Pode escolher qual tag quer enviar e a mensagem que quer enviar.

- pois.py

Ficheiro onde é calculado quando deve ser executada a próxima ação tendo em conta a distribuição de poisson.
