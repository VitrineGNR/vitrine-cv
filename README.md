> **Nota sobre integração com Google Drive:**  
> Todos os arquivos do sistema (propostas, PDFs, imagens, relatórios, exportações, etc.) serão armazenados e organizados automaticamente na pasta principal `VitrineCV` no Google Drive, criada e gerenciada pelo sistema.

Sistema para controle e automação do ciclo de vendas, cadastro de clientes e prospects, contatos, registros de interação, propostas, pedidos, follow-up, controle de faturamento, logística e entrega, pós-venda, manutenção de carteira de clientes e integração com Google Drive (caso haja necessidade).

---

## **Funcionalidades Principais**

- Cadastro de clientes, prospects e contatos
- Registro de interações e histórico de relacionamento
- Geração e gestão de propostas comerciais (com imagens e PDF)
- Controle e acompanhamento de pedidos (status, datas, valores)
- Gestão de follow-up automático e lembretes de ação
- Controle de faturamento, pagamentos e comissões
- Registro de etapas de logística e entrega
- **Indicadores:** Curva ABC (produtos, clientes e representadas), projeções de performance de produtos, clientes e representadas
- Pós-venda e manutenção da carteira de clientes
- Exportação/importação de dados (Excel, CSV, PDF, etc.)
- **Integração com Google Drive** para armazenar documentos, imagens e relatórios

---

## **Objetivos do Projeto**

- Automatizar e centralizar todas as etapas do ciclo de vendas em um único sistema web, acessível em qualquer dispositivo (PC, tablet, smartphone).
- Reduzir retrabalho e riscos de perda de informações.
- Tornar o acompanhamento de oportunidades mais eficiente e visual.
- Facilitar a gestão documental e de arquivos (propostas, pedidos, contratos) com integração Google Drive.
- Proporcionar acompanhamento gerencial por meio de indicadores, projeções e relatórios dinâmicos.
- Permitir fácil expansão e manutenção do sistema, com versionamento no GitHub.

---

## **Aproveitamento de Dados: Proposta & Pedido**

Um dos princípios centrais deste sistema é **maximizar a produtividade** evitando retrabalho entre propostas e pedidos.

- **Como funciona?**
  - O mesmo modelo de arquivo é utilizado para gerar tanto propostas quanto pedidos.
  - Ao transformar uma proposta em pedido, todos os dados são reaproveitados: basta revisar e editar apenas os campos que mudam.
  - Isso agiliza o processo e garante padronização, histórico e economia de tempo.

```mermaid
flowchart TD
    A[Preencher Proposta] --> B{Salvar Proposta}
    B --> C[Gerar PDF de Proposta]
    C --> D[Converter em Pedido]
    D --> E{Editar Campos Necessários}
    E --> F[Gerar PDF de Pedido]
