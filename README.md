
<body>
  <h1>Proposta de Projeto de Rede P2P Híbrida</h1>

  <h2>Objetivo</h2>

  <p>Desenvolver uma rede Peer-to-Peer (P2P) robusta e eficiente em Python, permitindo a transferência confiável de arquivos diversos (textos, planilhas, imagens, vídeos, etc.). A rede utilizará uma arquitetura híbrida, combinando nós regulares e nós de borda para otimizar a descoberta, roteamento e gerenciamento de arquivos.</p>

  <h2>Arquitetura</h2>

  <p>A arquitetura proposta consiste em dois tipos de nós:</p>

  <ul>
    <li><strong>Nós Regulares:</strong> Participantes que armazenam e compartilham arquivos. Eles mantêm uma lista de seus arquivos, incluindo informações de nome e integridade (checksum).</li>
    <li><strong>Nós de Borda:</strong> Servidores responsáveis por coordenar a descoberta e o roteamento de arquivos. Eles mantêm informações atualizadas sobre a localização de arquivos e nós ativos.</li>
  </ul>

  <h2>Funcionalidades Principais</h2>

  <ul>
    <li><strong>Descoberta e Transferência de Arquivos:</strong> Os nós de borda facilitam a descoberta de arquivos solicitados e direcionam as transferências para os nós que os possuem.</li>
    <li><strong>Balanceamento de Carga:</strong> As solicitações são distribuídas uniformemente entre os nós para evitar sobrecarga.</li>
    <li><strong>Manutenção de Listas Atualizadas:</strong> Os nós de borda atualizam regularmente suas listas de arquivos e nós ativos solicitando informações aos nós regulares. Nós inativos são removidos para manter a integridade da rede.</li>
  </ul>

  <h2>Implementação</h2>

  <ul>
    <li><strong>Linguagem de Programação:</strong> Python</li>
    <li><strong>Comunicação via Sockets:</strong> Para comunicação entre nós para transferência de arquivos e mensagens de controle.</li>
    <li><strong>Programação Concorrente:</strong> Uso de threads ou processos para gerenciar solicitações e transferências simultâneas.</li>
    <li><strong>Transferência de Arquivos:</strong> Suporte a vários formatos de arquivos, incluindo documentos, planilhas, imagens, vídeos e CSV. Verificação de integridade usando checksums.</li>
    <li><strong>Manutenção e Atualização de Listas:</strong> Solicitação periódica de atualizações aos nós regulares. Remoção de nós inativos que não respondem às solicitações.</li>
  </ul>

</body>
</html>
