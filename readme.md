# Documentação da API GraphQL para o Sistema de Gestão de Incubadoras

# Guia de Requisições em GraphQL

GraphQL é uma linguagem de consulta para APIs que oferece uma maneira mais eficiente, poderosa e flexível de trabalhar com dados. Diferentemente das APIs REST, que usam diferentes endpoints para diferentes tipos de requisições, uma API GraphQL expõe um único endpoint e usa a estrutura da consulta para determinar o que é retornado.

## Estrutura Básica de Requisição

Uma requisição GraphQL é feita enviando uma consulta (query) ou uma modificação (mutation) como um payload de requisição POST. A requisição deve ser enviada para o endpoint da API GraphQL.

endpoint da api: http://127.0.0.1:8000/graphql/

### Formato do Corpo da Requisição

O corpo da requisição deve ser um objeto JSON contendo pelo menos uma chave `query` que tem como valor uma string com a consulta ou a mutation em GraphQL. Opcionalmente, pode incluir uma chave `variables` se a consulta ou mutation contiver variáveis.

#### Exemplo de Corpo de Requisição

```json
{
  "query": "query($id: Int) { user(id: $id) { id username email } }",
  "variables": {
    "id": 1
  }
}
```

## Realizando Consultas (Queries)

### Estrutura de uma Query

As queries em GraphQL são usadas para ler ou buscar dados. Elas são estruturadas especificando o nome da operação (opcional), seguido de um conjunto de campos que você deseja obter.

#### Exemplo de Query

```json
query GetUser($id: Int) {
  user(id: $id) {
    id
    username
    email
  }
}
```

### Enviando a Query

Para enviar a query, você deve realizar uma requisição POST para o endpoint GraphQL com o corpo da requisição formatado como mostrado acima.

## Realizando Modificações (Mutations)

### Estrutura de uma Mutation

As mutations são usadas para criar, atualizar ou deletar dados. Elas são semelhantes às queries em estrutura, mas geralmente incluem argumentos para especificar os dados a serem modificados.

#### Exemplo de Mutation

```json
mutation CreateUser($email: String!, $username: String!) {
  createUser(email: $email, username: $username) {
    user {
      id
      username
    }
  }
}
```

### Enviando a Mutation

Assim como as queries, as mutations são enviadas como um payload de requisição POST para o endpoint GraphQL.

# Tutorial do GraphiQL

GraphiQL é uma ferramenta de interface gráfica integrada para explorar e testar APIs GraphQL. Este tutorial guiará você pelos passos básicos para usar o GraphiQL.

## Passo 1: Acessando o GraphiQL

Primeiro, você precisa acessar o GraphiQL. Geralmente, ele é disponibilizado em um endpoint específico da sua API GraphQL.

## Passo 2: Familiarizando-se com a Interface

A interface do GraphiQL é dividida em várias seções:

- **Área de Consulta (Esquerda):** Aqui você escreve suas queries ou mutations.
- **Área de Resposta (Direita):** Aqui são exibidos os resultados das suas consultas.
- **Barra de Ferramentas:** Contém botões para executar consultas, acessar a documentação, etc.
- **Documentação (Primeiro icone da barra de ferramentas):** Acesse a documentação da sua API GraphQL.

## Passo 3: Escrevendo uma Query

Para escrever uma query:

1. Digite a query no lado esquerdo da tela. Por exemplo: `query { users { id name } }`.
2. Pressione o botão "Executar" (ícone de play) ou use o atalho (Ctrl+Enter).

## Passo 4: Visualizando os Resultados

Após executar a query, você verá os resultados no lado direito da tela.

## Passo 5: Usando Variáveis

1. Defina a query com variáveis: `query GetUser($id: ID!) { user(id: $id) { name } }`.
2. Na parte inferior da área de consulta, clique em "Query Variables".
3. Insira as variáveis em formato JSON: `{ "id": "1" }`.

## Passo 6: Explorando a Documentação

Clique no ícone "Docs" (primeiro icone da barra de ferramentas) para explorar a documentação da API. Isso é útil para entender os tipos, queries, mutations e outros aspectos da API.

## Queries (Consultas)

### Buscar Todos os Dispositivos de Incubadora

```graphql
query {
  allIncubatorDevices {
    uniqueId
    user {
      id
      username
      email
      isStaff
    }
    currentSetting {
      id
      name
      temperature
      humidity
      incubationDuration
    }
    isOn
    humiditySensor
    temperatureSensor
    startTime
  }
}
```

### Buscar Dispositivo de Incubadora por ID Único

```graphql
query ($uniqueId: String) {
  incubatorDevice(uniqueId: $uniqueId) {
    uniqueId
    user {
      id
      username
      email
      isStaff
    }
    currentSetting {
      id
      name
      temperature
      humidity
      incubationDuration
    }
    isOn
    humiditySensor
    temperatureSensor
    startTime
  }
}
```

### Buscar Todas as Configurações de Incubadora

```graphql
query {
  allIncubatorSettings {
    id
    name
    temperature
    humidity
    incubationDuration
    user {
      id
      username
    }
    assignedDevices {
      uniqueId
    }
  }
}
```

### Buscar Configuração de Incubadora por ID

```graphql
query ($id: Int) {
  incubatorSetting(id: $id) {
    id
    name
    temperature
    humidity
    incubationDuration
    user {
      id
      username
    }
    assignedDevices {
      uniqueId
    }
  }
}
```

### Buscar Todos os Usuários

```graphql
query {
  users {
    id
    username
    email
    isStaff
  }
}
```

### Buscar Usuário por ID

```graphql
query ($id: Int) {
  user(id: $id) {
    id
    username
    email
    isStaff
  }
}
```

## Mutations (Modificações)

### Criar Dispositivo de Incubadora

```graphql
mutation (
  $humiditySensor: String!
  $temperatureSensor: String!
  $userId: Int!
) {
  createIncubatorDevice(
    humiditySensor: $humiditySensor
    temperatureSensor: $temperatureSensor
    userId: $userId
  ) {
    incubatorDevice {
      uniqueId
      user {
        id
        username
      }
      currentSetting {
        id
        name
      }
      isOn
      humiditySensor
      temperatureSensor
      startTime
    }
  }
}
```

### Criar Usuário

```graphql
mutation ($email: String!, $password: String!, $username: String!) {
  createUser(email: $email, password: $password, username: $username) {
    user {
      id
      username
      email
      isStaff
    }
  }
}
```

### Criar Configuração de Incubadora

```graphql
mutation (
  $humidity: Float!
  $incubationDuration: Int!
  $name: String!
  $temperature: Float!
  $userId: Int!
) {
  createIncubatorSetting(
    humidity: $humidity
    incubationDuration: $incubationDuration
    name: $name
    temperature: $temperature
    userId: $userId
  ) {
    incubatorSetting {
      id
      name
      temperature
      humidity
      incubationDuration
      user {
        id
        username
      }
      assignedDevices {
        uniqueId
      }
    }
  }
}
```

### Atualizar Configuração de Incubadora

```graphql
mutation (
  $humidity: Float
  $id: Int!
  $incubationDuration: Int
  $name: String
  $temperature: Float
) {
  updateIncubatorSetting(
    humidity: $humidity
    id: $id
    incubationDuration: $incubationDuration
    name: $name
    temperature: $temperature
  ) {
    incubatorSetting {
      id
      name
      temperature
      humidity
      incubationDuration
      user {
        id
        username
      }
      assignedDevices {
        uniqueId
      }
    }
  }
}
```

### Atualizar Dispositivo de Incubadora

```graphql
mutation($currentSettingId: Int, $humiditySensor: String, $isOn: Boolean, $temperatureSensor: String, $uniqueId: String!, $userId: Int) {
  updateIncubatorDevice(currentSettingId: $currentSettingId, humiditySensor: $humiditySensor, isOn:
```
