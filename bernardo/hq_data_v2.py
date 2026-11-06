# HQs do lote 01, versão 2 (2026-10-06): pacientes, cenários e paletas diferentes, pautas de temas em alta.
# Pesquisa: /mnt/project-files/bernardo/pesquisa/temas_em_alta_2026-10.md
# Cada HQ: capa (paciente sozinho), 3 quadros no consultório (p = paciente, d = doutor) e CTA (doutor sozinho + tarja).
HQS = [
 dict(slot="HQ01", id="HQ01_joelho_corrida", tema="JOELHO", titulo="Comecei a correr e o joelho dói",
  paleta=dict(fundo="#FFF3C4", quadro="#1565C0", tarja="#1565C0", palavra="#FFD23F"),
  media=dict(s1="MAHXRArNMq0", s2="MAHXRKujf0E", s3="MAHXRCgyT7E", s4="MAHXRHr4PLM", s5="MAHXRHFF31c"),
  capa="COMECEI A CORRER HÁ 2 MESES E JÁ TÔ NA META DE 10 KM... MAS A FRENTE DO JOELHO DÓI.",
  dialogo=[("É NORMAL DOER NO COMEÇO, NÉ?", "CANSAÇO É NORMAL. DOR NA FRENTE DO JOELHO QUE VOLTA A CADA TREINO É SINAL DE SOBRECARGA."),
           ("MAS EU SÓ AUMENTEI UM POUQUINHO POR SEMANA...", "O CORAÇÃO SE ADAPTA RÁPIDO. TENDÃO E ARTICULAÇÃO PRECISAM DE MAIS TEMPO."),
           ("E AGORA, PARO DE CORRER?", "NEM SEMPRE. A GENTE ACHA A CAUSA, AJUSTA O TREINO E FORTALECE. EM ALGUNS CASOS, ONDAS DE CHOQUE AJUDAM.")],
  cta="VOCÊ CORRE E O JOELHO RECLAMA?",
  legenda="""Começou a correr e agora a frente do joelho dói? 🏃‍♀️

A corrida virou febre, e com ela a dor na frente do joelho. Quase sempre o problema não é correr, é aumentar o volume mais rápido do que tendão e articulação conseguem acompanhar. Com avaliação, ajuste de treino e fortalecimento, a maioria volta a correr.

👉 Comente "JOELHO" e entenda como eu posso te ajudar."""),
 dict(slot="HQ05", id="HQ05_joelho_canetas_emagrecer", tema="JOELHO", titulo="Emagreci com a caneta e o joelho dói",
  paleta=dict(fundo="#E6F4EE", quadro="#6C4AB6", tarja="#6C4AB6", palavra="#FFD23F"),
  media=dict(s1="MAHXRCKvC4E", s2="MAHXRHTjEx4", s3="MAHXRFWM17I", s4="MAHXRPWYoYU", s5="MAHXRPJRALc"),
  capa="PERDI 15 KG COM A CANETINHA! SÓ QUE O JOELHO... CONTINUA RECLAMANDO.",
  dialogo=[("ERA PRA MELHORAR, NÃO ERA?", "PERDER PESO AJUDA O JOELHO. MAS SE JUNTO VAI EMBORA MÚSCULO, A ARTICULAÇÃO FICA SEM PROTEÇÃO."),
           ("EU TÔ PERDENDO MÚSCULO?", "PODE ACONTECER QUANDO O PESO CAI RÁPIDO E NÃO TEM TREINO DE FORÇA. POR ISSO VALE AVALIAR."),
           ("E COMO EU CUIDO DO JOELHO AGORA?", "COM AVALIAÇÃO, FORTALECIMENTO E, SE PRECISAR, TRATAMENTO PRA DOR, COMO INFILTRAÇÃO. JUNTO COM QUEM TE ACOMPANHA NO EMAGRECIMENTO.")],
  cta="TÁ EMAGRECENDO E O JOELHO NÃO ACOMPANHOU?",
  legenda="""Emagreceu com as canetas e o joelho continua doendo? 💉

Perder peso alivia o joelho, mas quando o peso cai rápido sem treino de força, parte do que vai embora é músculo, e é o músculo que protege a articulação. Cuidar do joelho faz parte do emagrecimento, junto com quem te acompanha.

👉 Comente "JOELHO" e entenda como eu posso te ajudar."""),
 dict(slot="HQ02", id="HQ02_coluna_pescoco_celular", tema="COLUNA", titulo="Pescoço duro de tanto celular",
  paleta=dict(fundo="#EDE7FF", quadro="#2B1B5A", tarja="#2B1B5A", palavra="#FFD23F"),
  media=dict(s1="MAHXRIx-QpY", s2="MAHXRN2GqPs", s3="MAHXRIfD_1s", s4="MAHXRNh6QBE", s5="MAHXRHCxl2c"),
  capa="MEU PESCOÇO VIVE DURO E A CABEÇA DÓI NO FIM DO DIA. DEVE SER O TRAVESSEIRO...",
  dialogo=[("SÉRIO QUE É O CELULAR?", "CABEÇA INCLINADA PRA FRENTE PODE PESAR ATÉ 4 VEZES MAIS NA CERVICAL. HORAS ASSIM, TODO DIA, CANSAM O PESCOÇO."),
           ("MAS EU TENHO 22 ANOS!", "IDADE NÃO PROTEGE DE SOBRECARGA. DOR QUE VIROU ROTINA, OU QUE DESCE PRO BRAÇO, PRECISA DE AVALIAÇÃO."),
           ("VOU TER QUE LARGAR O CELULAR?", "NÃO! AJUSTE A ALTURA DA TELA, FAÇA PAUSAS E FORTALEÇA. E SE A DOR NÃO PASSA, A GENTE TRATA.")],
  cta="QUANTAS HORAS SEU PESCOÇO PASSA DOBRADO?",
  legenda="""Pescoço duro e dor de cabeça no fim do dia? 📱

Com a cabeça inclinada para olhar o celular, a carga na cervical pode chegar a cerca de 4 vezes o peso da cabeça. Pausas, tela na altura dos olhos e fortalecimento ajudam muito. Se a dor virou rotina ou desce para o braço, é hora de avaliar.

👉 Comente "COLUNA" e entenda como eu posso te ajudar."""),
 dict(slot="HQ03", id="HQ03_joelho_beach_tennis", tema="JOELHO", titulo="Beach tennis e dor no joelho",
  paleta=dict(fundo="#FFE3C2", quadro="#E8505B", tarja="#0E7C86", palavra="#FFD23F"),
  media=dict(s1="MAHXRNWcBl4", s2="MAHXRKo-buw", s3="MAHXRB1S6N4", s4="MAHXRJ8KqS4", s5="MAHXRP8QGnM"),
  capa="AMO BEACH TENNIS, MAS AGORA O JOELHO DÓI A CADA ARRANCADA NA AREIA.",
  dialogo=[("DOUTOR, É SÓ PEGAR LEVE QUE PASSA?", "AREIA FOFA, GIROS E ARRANCADAS SOBRECARREGAM O JOELHO. DOR QUE VOLTA TODA SEMANA MERECE AVALIAÇÃO."),
           ("VOU TER QUE PARAR DE JOGAR?", "NA MAIORIA DAS VEZES, NÃO. O OBJETIVO É VOCÊ VOLTAR PRA QUADRA COM SEGURANÇA."),
           ("E O QUE DÁ PRA FAZER?", "DEPENDE DA CAUSA: FORTALECIMENTO, AJUSTE DE TREINO E, EM ALGUNS CASOS, ONDAS DE CHOQUE OU TERAPIAS COM O PRÓPRIO SANGUE, COMO O PRP.")],
  cta="VOCÊ JOGA E SENTE O JOELHO DEPOIS?",
  legenda="""Joga beach tennis e o joelho reclama depois? 🎾

Areia fofa, giros e arrancadas cobram do joelho, principalmente de quem joga várias vezes por semana. Dor que volta toda semana não é para ignorar. Na maioria dos casos dá para tratar e continuar jogando com segurança.

👉 Comente "JOELHO" e entenda como eu posso te ajudar."""),
 dict(slot="HQ04", id="HQ04_coluna_motorista_lombar", tema="COLUNA", titulo="Dirijo o dia todo e a lombar trava",
  paleta=dict(fundo="#F5E6E0", quadro="#B71C1C", tarja="#2E2E2E", palavra="#FFD23F"),
  media=dict(s1="MAHXRORseRk", s2="MAHXRPtLKXk", s3="MAHXRKLH_MU", s4="MAHXRPbCL0s", s5="MAHXRNwU5ec"),
  capa="10 HORAS POR DIA DIRIGINDO. NO FIM DO EXPEDIENTE, A LOMBAR TRAVA E A DOR DESCE PRA PERNA.",
  dialogo=[("É ISSO OU EU PARO DE TRABALHAR?", "DOR NAS COSTAS FOI O MAIOR MOTIVO DE AFASTAMENTO DO TRABALHO NO BRASIL EM 2024. NÃO É FRESCURA."),
           ("E ESSA DOR NA PERNA?", "PODE SER UM NERVO IRRITADO, COMO NA HÉRNIA DE DISCO. POR ISSO PRECISA DE EXAME FÍSICO E, ÀS VEZES, IMAGEM."),
           ("VAI TER QUE OPERAR?", "NA MAIORIA DAS VEZES, NÃO. EXISTEM FISIOTERAPIA, REMÉDIO CERTO E BLOQUEIO GUIADO PARA ALIVIAR A DOR.")],
  cta="VOCÊ PASSA O DIA SENTADO E A LOMBAR COBRA?",
  legenda="""Passa o dia sentado e a lombar cobra no fim do expediente? 🚗

Dor nas costas foi a principal causa de afastamento do trabalho no Brasil em 2024. Quando a dor desce para a perna, pode ser um nervo irritado, como na hérnia de disco. Na maioria das vezes o tratamento não é cirúrgico.

👉 Comente "COLUNA" e entenda como eu posso te ajudar."""),
 dict(slot="HQ06", id="HQ06_coluna_academia_lombar", tema="COLUNA", titulo="Fisgada na lombar no treino",
  paleta=dict(fundo="#EEF7D9", quadro="#1B1B1B", tarja="#1B1B1B", palavra="#C6F432"),
  media=dict(s1="MAHXRD_9lqU", s2="MAHXRC7WBpk", s3="MAHXRKN1gGU", s4="MAHXRJYbmI4", s5="MAHXRN4shp8"),
  capa="SUBI A CARGA NO TERRA PRA BATER RECORDE... E SENTI UMA FISGADA NA LOMBAR.",
  dialogo=[("É SÓ UMA DISTENSÃO, DOUTOR. AMANHÃ EU TREINO.", "FISGADA COM CARGA PODE SER MÚSCULO... OU O DISCO. SE DESCE PRA PERNA OU FORMIGA, PARE E AVALIE."),
           ("MAS TREINO NÃO FORTALECE A COLUNA?", "FORTALECE! O PROBLEMA É CARGA ALTA COM TÉCNICA CANSADA. O ERRO É NO COMO, NÃO NO TREINO."),
           ("VOU TER QUE PARAR A ACADEMIA?", "NA MAIORIA DAS VEZES, NÃO. A GENTE TRATA A DOR, AJUSTA O TREINO E VOCÊ VOLTA COM SEGURANÇA.")],
  cta="VOCÊ TREINA E A LOMBAR RECLAMA?",
  legenda="""Sentiu uma fisgada na lombar no treino e pensou "amanhã passa"? 🏋️

Treino fortalece a coluna. O problema costuma ser carga alta com técnica cansada. Se a dor desce para a perna ou vem com formigamento, pare e avalie antes de voltar a pegar peso.

👉 Comente "COLUNA" e entenda como eu posso te ajudar."""),
]
