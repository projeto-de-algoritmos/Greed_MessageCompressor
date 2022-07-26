# Message Compressor

**Número da Lista**: Não se aplica<br>
**Conteúdo da Disciplina**: Greed<br>

## Alunos
| Matrícula  | Aluno                         |
| ---------- | ----------------------------- |
| 19/0124997 | Amanda Jeniffer Pereira Nobre |
| 15/0129866 | Igor Araujo de Sousa          |

## Sobre 
Este projeto tem como objetivo compactar uma mensagem de texto, enviá-la através de um serviço de mensageria, e descompactá-la no recebimento.

## Screenshots

### Enviando requisição
![image](https://user-images.githubusercontent.com/44625056/180907615-ec9a8b02-e6d2-4abc-ab5c-b33dcb13cffa.png)

### RabbitMQ
![image](https://user-images.githubusercontent.com/44625056/180907650-83bbc62e-ca32-4846-980e-ee62dabf7046.png)

### Mensagem recebida e descompactada
![image](https://user-images.githubusercontent.com/44625056/180907685-4ab28e3d-a5e5-4ed1-8b55-8e5c0d6a3f24.png)

## Instalação 
**Linguagem**: Python<br>
**Framework**: Flask<br>

## Uso 
Tudo que é necessário para executar esse projeto é ter em sua máquina instalado o [docker](https://docs.docker.com/engine/install/ubuntu/) e o [docker-compose](https://docs.docker.com/compose/install/)

Após a intalação de ambos é necessário executar os seguintes comandos na raiz desse projeto:

```
docker-compose up
```

```
docker-compose exec consumer python consumer.py
```

Agora basta enviar uma requisição do tipo POST para a url http://localhost:8081/huffman na seguinte forma:

```
{
	"msg": "sua mensagem"
}
```

## Outros 

A string de acesso é um dado sensível, portanto para fins de avaliação do professor e avaliação por pares a equipe deixará no projeto até o fim do semestre.




