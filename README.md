Sistema de Agendamento de Equoterapia

Este projeto é um sistema simples para gerenciar um centro de equoterapia, permitindo o cadastro de pacientes, cavalos, percursos com desafios e o agendamento de sessões. Os dados são armazenados em um arquivo JSON para facilitar a persistência.
✨ Funcionalidades

    Cadastro de Pacientes: Nome, idade e laudo médico.
    Cadastro de Cavalos: Nome do cavalo utilizado nas sessões.
    Cadastro de Percursos e Desafios: Adicione percursos e seus desafios detalhados.
    Agendamento de Sessões: Relacione paciente, cavalo e percurso para uma sessão específica.
    Exibição de Cronograma: Visualize os agendamentos salvos.
    Persistência de Dados: Salve os agendamentos em um arquivo JSON.

🚀 Como Executar

    Clone o repositório:

git clone https://github.com/seu-usuario/nome-do-repositorio.git

Navegue até o diretório do projeto:

cd nome-do-repositorio

Execute o script principal:

    python main.py

📂 Estrutura do Projeto

/
├── main.py                 # Interface de interação com o usuário
├── Classes.py              # Classes que estruturam o sistema
├── dados.json              # Arquivo de persistência de dados (gerado após salvar dados)
└── README.md               # Documentação do projeto

🛠️ Tecnologias Utilizadas

    Python 3.8+: Linguagem de programação utilizada.
    JSON: Para armazenamento e persistência dos dados.

🎯 Melhorias Futuras

    Integração com banco de dados para maior escalabilidade, permitindo assim, um melhor uso dos dados coletados.
    Implementação de interface gráfica para melhor usabilidade.
    Adição de autenticação de usuários para acesso restrito ao sistema.
    

