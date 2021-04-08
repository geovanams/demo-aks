# Tutorial - Implantar um Cluster AKS

<h2>Objetivo</h2>

* Criar e implantar um cluster AKS
* Fazer deploy e executar uma aplicação python com flask
* Realizar dimensionamento manual e automático de pod 

<h2>Sumário</h2>

1. [Criando Cluster AKS](#criandocluster)
2. [Deploy e executando aplicação](#executandoapp)
3. [Dimensionando pods](#dimensionandopods)

___

<h2>Criando Cluster AKS (Azure Portal) <a name="criandocluster"></a></h2>

Antes de criar nosso Cluster precisamos criar um resource group:

<h3>1- Criando resource group</h3>

* No portal do Azure, clique no ícone superior esquerdo e depois em __Resource groups__

<img src="https://user-images.githubusercontent.com/50850895/113924056-b66bd500-97bf-11eb-8f81-60529a346233.png" />

* Clique em __+Create__

<img src="https://user-images.githubusercontent.com/50850895/113924058-b7046b80-97bf-11eb-89b7-4816c90b242d.png" />

* Forneça as informações do seu resource group:

  * __Subscription:__ Nome da sua subscription
  * __Resource group:__ Nome do resource group como por exemplo:  __AKSDemo__
  * __Region:__ Escolha a região da sua escolha
  * Depois clique em __Review + Create__ e então em __Create__

![Picture3](https://user-images.githubusercontent.com/50850895/113932928-5e869b80-97ca-11eb-906b-9a5bb0c999e1.png)

Depois do resource group criado vamos criar nosso cluster:

<h3>2 - Criando Cluster </h3>

* Dentro do Resource Group clique em +Add

![Picture4](https://user-images.githubusercontent.com/50850895/113928526-524c0f80-97c5-11eb-86d7-2fe3b3fa610a.png)

* Clique em Containers e depois em __Kubernetes Service__

![Picture5](https://user-images.githubusercontent.com/50850895/113933527-14ea8080-97cb-11eb-8006-04e1afac11be.png)

* Forneça as informações do seu Cluster:

  * __Project Details__:
    * __Subscription:__ Nome da sua subscription
    * __Resource group:__ Nome do resource group criado anteriormente
  * __Cluster Details__
    * __Kubernetes cluster name:__ Nome do seu cluster como por exemplo: __MyAKSCluster__
    * __Region:__ Escolha a região da sua escolha
    * __Availability Zones:__ None
    * __Kubernetes version:__ Manter a versão padrão
  * __Primary Node pool__
    * __Node Size:__ Clique em Change size, selecione B2s e clique em Select
    * __Node Count:__ Deixe como 1 a quantidade de nodes iniciais
  * Clique em __Next:Node Pools>__

![Picture6](https://user-images.githubusercontent.com/50850895/113934284-f33dc900-97cb-11eb-8c54-8e7820622c36.png)

* Na sessão Node Pools defina as configurações:

  * Habilite virtual Machine Scale Sets
  * Mantenha os outros valores padrão
  * Clique em __Next: Authentication>__
  
![Picture7](https://user-images.githubusercontent.com/50850895/113937540-b1168680-97cf-11eb-83f2-5d0759479b7b.png)

* Na sessão Authentication e Network, mantenha os valores padrão

* Na sessão Integrations, defina:

  * __Container Monitoring:__ Enable
  * __Log Analytics workspace:__ Mantenha o padrão ou crie um novo selecionando uma região e um nome da sua escolha
  * __Azure Policy:__ Enable
  * Clique em __Review + Create__ e então em __Create__
  * (O cluster leva alguns minutos para ser criado)

![Picture10](https://user-images.githubusercontent.com/50850895/113940397-c1c8fb80-97d3-11eb-90c9-58942beec5cf.png)

* Depois que o Deployment estiver completo, clique em __Go to resource__ para ir para a página do Cluster

* Com o cluster criado, agora vamos executar um aplicativo python com flask 

___

<h2>Executando aplicação <a name="executandoapp"></a></h2>

Vamos utilizar o Cloud Shell para rodar nossos comandos

<h3> 1 - Abra o Cloud Shell </h3>

* Selecione o ícone superior direito como mostra na imagem

![Picture11](https://user-images.githubusercontent.com/50850895/113941548-abbc3a80-97d5-11eb-8d2b-3d02342eac46.png)

* Selecione Bash e caso você não tenha uma storage account clique em create que será criada uma para você, pois a storage account é necessária para persistência de dados

<h3> 2 - Clone o Repositório </h3>

A aplicação que executaremos está no github: https://github.com/geovanams/demo-aks - automatic!

* No CloudShell faça o clone do repositório executando o comando:

```git clone https://github.com/geovanams/demo-aks.git ```

* Vá até o repositório:

```cd demo-aks```

<h3> 3 - Conectando-se ao Cluster </h3>

* Clique em Connect e copie o comando que aparece ao lado

![Picture14](https://user-images.githubusercontent.com/50850895/113945555-ef667280-97dc-11eb-954e-d9c8e958be1e.png)

* Cole o comando no CloudShell

Agora podemos subir nossos containers

<h3> 4 - Fazendo deploy </h3>

* No CloudShell certifique-se de estar no diretório /demo-aks 
  
  ```cd demo-aks```
  
* Para realizar o deploy da aplicação no cluster rode o seguinte comando:

  ```kubectl apply -f app-hello.yaml```

Agora ja podemos acessar a aplicação

* Para encontrar o IP público do nosso service, execute no cloudShell:

  ```kubectl get services```

* Copie o valor da coluna External-IP e cole em uma aba do seu navegador

* PRONTO!! A aplicação já está funcionando!!

![Picture15](https://user-images.githubusercontent.com/50850895/113946341-9992ca00-97de-11eb-919e-0f7f3e7cebe2.png)

* Para ver quais pods estão rodando, rode o seguinte comando:

  ```kubectl get pods```

___

<h2> Dimensionando pods <a name="dimensionandopods"></a> </h2> 

<h3> Dimensionamento Manual </h3>

* Podemos aumentar  manualmente a quantidade de pods do nosso deployment definindo a quantidade de replicas:
 
```kubectl scale --replicas=3 deployment/demo-aks```

<h3> Dimensionamento Automático </h3>

O Kubernetes dá suporte a dimensionamento automático horizontal de pods, para ajustar o número de pods em um deployment dependendo da utilização da CPU ou de outras métricas selecionadas.

* Podemos fazer o dimensionamento automático através do comando:

```kubectl autoscale deployment demoaks --cpu-percent=50 --min=3 --max=10```

Onde o comando é utilizado para dimensionar automaticamente o número de pods no deployment demoaks. 
Se a utilização média da CPU entre todos os pods exceder 50% do seu uso solicitado, o dimensionamento automático aumentará os pods até um máximo de 10 instâncias e um mínimo de 3


