# HQs do lote 02 (2026-11-05): pacientes, cenários e paletas diferentes dos do lote 01.
# Pesquisa: /mnt/project-files/bernardo/pesquisa/temas_em_alta_2026-11.md
# Ilustrações: design Canva DAHaFek1tFY ("Ilustrações originais HQ lote 02"), cópia em bernardo/ilustracoes/lote_02 no GitHub.
# Uso: HQ_DATA=hq_data_lote02 python3 render_hq.py <pasta_artes> <pasta_saida>
HQS = [
 dict(slot="HQ07", id="HQ07_joelho_padel", tema="JOELHO", titulo="Padel e dor no joelho",
  paleta=dict(fundo="#E0F7F4", quadro="#0B7A75", tarja="#0B7A75", palavra="#FFD23F"),
  capa="ENTREI NA ONDA DO PADEL, JOGO 4 VEZES POR SEMANA... E AGORA O JOELHO DÓI A CADA FREADA.",
  dialogo=[("DEVE SER SÓ FALTA DE ALONGAMENTO, NÉ?", "FREADAS E GIROS CARREGAM MUITO O JOELHO. DOR QUE VOLTA A CADA JOGO NÃO É SÓ FALTA DE ALONGAMENTO."),
           ("MAS EU TENHO 42 ANOS, NÃO 70!", "NÃO É QUESTÃO DE IDADE. PODE SER TENDÃO, MENISCO OU CARTILAGEM. SÓ A AVALIAÇÃO MOSTRA."),
           ("VOU TER QUE LARGAR A QUADRA?", "NA MAIORIA DAS VEZES, NÃO. FORTALECIMENTO, AJUSTE NA ROTINA E, SE PRECISAR, INFILTRAÇÃO OU ONDAS DE CHOQUE.")],
  cta="VOCÊ JOGA PADEL E O JOELHO RECLAMA?",
  legenda="""Entrou na onda do padel e agora o joelho reclama? 🎾

O padel é o esporte que mais cresce no Brasil, e o joelho é o local que mais se machuca entre os amadores. Freadas, giros e mudanças de direção cobram da articulação. Dor que volta a cada jogo merece avaliação, e na maioria dos casos dá para tratar e continuar jogando.

👉 Comente "JOELHO" e entenda como eu posso te ajudar."""),
 dict(slot="HQ08", id="HQ08_coluna_home_office", tema="COLUNA", titulo="Home office no sofá e a coluna",
  paleta=dict(fundo="#F4EDE4", quadro="#5C6BC0", tarja="#283593", palavra="#FFD23F"),
  capa="TRABALHO DE CASA, NO SOFÁ, COM O NOTEBOOK NO COLO. NO FIM DO DIA, A LOMBAR E O PESCOÇO GRITAM.",
  dialogo=[("MAS EU TÔ NO CONFORTO DE CASA!", "SOFÁ É ÓTIMO PRA DESCANSAR, NÃO PRA TRABALHAR 8 HORAS. A COLUNA PASSA O DIA DOBRADA."),
           ("SOU NOVO DEMAIS PRA TER DOR NAS COSTAS.", "QUASE 1 EM CADA 10 JOVENS DE 18 A 29 ANOS JÁ TEM DOR CRÔNICA NAS COSTAS. IDADE NÃO PROTEGE."),
           ("E O QUE EU FAÇO, DOUTOR?", "MESA E CADEIRA, TELA NA ALTURA DOS OLHOS, PAUSAS E MOVIMENTO. SE A DOR NÃO PASSA, A GENTE INVESTIGA E TRATA.")],
  cta="VOCÊ TRABALHA DE CASA E A COLUNA COBRA?",
  legenda="""Trabalha de casa e no fim do dia a coluna cobra a conta? 💻

Notebook no colo e sofá viram 8 horas de coluna dobrada. Quase 1 em cada 10 jovens de 18 a 29 anos já convive com dor crônica nas costas. Mesa, tela na altura dos olhos e pausas ajudam muito. Se a dor não passa, vale investigar.

👉 Comente "COLUNA" e entenda como eu posso te ajudar."""),
 dict(slot="HQ09", id="HQ09_joelho_futevolei", tema="JOELHO", titulo="Torci o joelho no futevôlei",
  paleta=dict(fundo="#FFF6D6", quadro="#00A6D6", tarja="#00718F", palavra="#FFD23F"),
  capa="NO FUTEVÔLEI, CAÍ DE MAU JEITO NA AREIA, O JOELHO GIROU... E AGORA PARECE QUE ELE FALHA.",
  dialogo=[("INCHOU, MAS JÁ TÁ MELHOR. NEM PRECISA VER, NÉ?", "INCHAÇO DEPOIS DE UM GIRO E SENSAÇÃO DE FALSEIO PODEM SER SINAL DE LESÃO NO LIGAMENTO OU NO MENISCO."),
           ("MAS EU ANDO NORMAL!", "ANDAR NO PLANO É UMA COISA. GIRAR, SALTAR E PARAR DE REPENTE É OUTRA. É AÍ QUE A LESÃO APARECE."),
           ("SE FOR LIGAMENTO, ACABOU O VERÃO?", "PRIMEIRO, O DIAGNÓSTICO. DEPENDENDO DA LESÃO, O TRATAMENTO PODE SER REABILITAÇÃO OU CIRURGIA. CADA CASO É UM CASO.")],
  cta="SEU JOELHO JÁ FALHOU DEPOIS DE UM GIRO?",
  legenda="""O joelho girou, inchou e agora parece que falha? 🏐

Com o verão chegando, a areia enche de futevôlei, vôlei e beach tennis. Inchaço depois de uma torção e sensação de falseio podem indicar lesão no ligamento ou no menisco, mesmo quando você anda normal. Avaliar cedo ajuda a escolher o melhor caminho.

👉 Comente "JOELHO" e entenda como eu posso te ajudar."""),
 dict(slot="HQ10", id="HQ10_coluna_mae_colo", tema="COLUNA", titulo="Mãe, colo e dor na lombar",
  paleta=dict(fundo="#FFF1E6", quadro="#FF7043", tarja="#4A148C", palavra="#FFD23F"),
  capa="CARREGO MEU FILHO NO COLO O DIA INTEIRO. À NOITE, A LOMBAR DÓI TANTO QUE EU NEM CONSIGO ME ABAIXAR.",
  dialogo=[("TODA MÃE SENTE ISSO, NÃO É?", "MUITAS SENTEM, MAS ISSO NÃO TORNA NORMAL. DOR CRÔNICA NA COLUNA É MAIS COMUM EM MULHERES, E MUITAS SÓ ACEITAM."),
           ("NÃO TENHO TEMPO DE CUIDAR DE MIM...", "SE A SUA COLUNA PARA, A ROTINA PARA JUNTO. CUIDAR DE VOCÊ TAMBÉM É CUIDAR DELE."),
           ("E SE FOR ALGO SÉRIO?", "A MAIORIA DOS CASOS TEM TRATAMENTO SEM CIRURGIA. A AVALIAÇÃO MOSTRA A CAUSA E O TRATAMENTO CERTO PRO SEU CASO.")],
  cta="VOCÊ CUIDA DE TODO MUNDO, MENOS DA SUA COLUNA?",
  legenda="""Você cuida de todo mundo, menos da sua coluna? 🤱

Dor crônica na coluna atinge mais mulheres do que homens (20,1% contra 15,2%, segundo a Pesquisa Nacional de Saúde), e muitas acham que é o preço da rotina. Não precisa ser. A maioria dos casos tem tratamento sem cirurgia, e o primeiro passo é uma avaliação.

👉 Comente "COLUNA" e entenda como eu posso te ajudar."""),
 dict(slot="HQ11", id="HQ11_joelho_avo_artrose", tema="JOELHO", titulo="O avô que não consegue brincar no chão",
  paleta=dict(fundo="#EAF4E0", quadro="#5D8C3E", tarja="#2E4A1F", palavra="#FFD23F"),
  capa="MEU NETO ME CHAMA PRA BRINCAR NO CHÃO... E EU NÃO CONSIGO NEM ME AGACHAR DE TANTA DOR NO JOELHO.",
  dialogo=[("NA MINHA IDADE É ASSIM MESMO, DOUTOR.", "IDADE NÃO É DIAGNÓSTICO. ISSO PODE SER ARTROSE, E ARTROSE TEM TRATAMENTO."),
           ("ENTÃO VOU TER QUE BOTAR PRÓTESE?", "A PRÓTESE É UMA OPÇÃO PARA ALGUNS CASOS AVANÇADOS. MUITOS PACIENTES COMEÇAM POR OUTROS CAMINHOS."),
           ("QUE CAMINHOS?", "FORTALECIMENTO, CONTROLE DO PESO E INFILTRAÇÃO, COMO A DE ÁCIDO HIALURÔNICO. CADA CASO TEM O SEU PLANO.")],
  cta="A DOR NO JOELHO TÁ TE TIRANDO MOMENTOS ASSIM?",
  legenda="""A dor no joelho está te tirando momentos que importam? 👴

"Na minha idade é assim mesmo" não é diagnóstico. Dor para agachar e levantar pode ser artrose, e artrose tem tratamento. Prótese é uma opção para alguns casos avançados, mas muitos pacientes começam com fortalecimento, controle do peso e infiltração.

👉 Comente "JOELHO" e entenda como eu posso te ajudar."""),
 dict(slot="HQ12", id="HQ12_coluna_cabeleireira_cervical", tema="COLUNA", titulo="Dor do pescoço que desce pro braço",
  paleta=dict(fundo="#FFE4EC", quadro="#D81B60", tarja="#212121", palavra="#FFD23F"),
  capa="PASSO O DIA COM OS BRAÇOS PRA CIMA, SECANDO CABELO. AGORA A DOR SAI DO PESCOÇO E DESCE PRO BRAÇO.",
  dialogo=[("É SÓ TENSÃO, NÉ? UMA MASSAGEM RESOLVE.", "TENSÃO DÓI NO PESCOÇO. DOR QUE DESCE PRO BRAÇO, COM FORMIGAMENTO, PODE SER UM NERVO IRRITADO NA CERVICAL."),
           ("TIPO HÉRNIA? NO PESCOÇO EXISTE ISSO?", "EXISTE, SIM. A HÉRNIA CERVICAL PODE APERTAR O NERVO QUE VAI PRO BRAÇO. POR ISSO PRECISA DE EXAME."),
           ("VOU TER QUE PARAR DE TRABALHAR?", "NA MAIORIA DAS VEZES, NÃO. EXISTEM REMÉDIO CERTO, FISIOTERAPIA E BLOQUEIO GUIADO PARA ALIVIAR A DOR.")],
  cta="SUA DOR SAI DO PESCOÇO E DESCE PRO BRAÇO?",
  legenda="""A dor sai do pescoço e desce para o braço? 💇‍♀️

Quem trabalha com os braços elevados, como cabeleireiros, pintores e professores, sobrecarrega a cervical o dia todo. Quando a dor desce para o braço ou vem com formigamento, pode ser um nervo irritado, como na hérnia cervical. Na maioria das vezes o tratamento não é cirúrgico.

👉 Comente "COLUNA" e entenda como eu posso te ajudar."""),
]
