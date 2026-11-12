# Conteúdo dos 6 carrosséis storytelling
REV = {
 "DMCS": dict(ini="D.M.C.S.", date="19/08/2026", local="C.O.T. - Centro Ortopédico e Traumatológico", text="Dr. Bernardo explica tudo nos detalhes, de maneira clara e não técnica. Escuta o paciente e endereça suas dúvidas. Impecável! Recomendo a todos."),
 "VS": dict(ini="V.S.", date="09/09/2026", local="C.O.T. - Centro Ortopédico e Traumatológico", text="Dr. Bernardo é muito envolvido para gerar a solução do paciente e muito sincero na avaliação. Ótimo profissional!"),
 "AC": dict(ini="A.C.", date="12/08/2026", local="C.O.T. · Infiltração do joelho", text="Médico maravilhoso, paciente e muito educado. Ótimo profissional"),
 "VG": dict(ini="V.G.", date="02/09/2026", local="C.O.T. - Centro Ortopédico e Traumatológico", text="Dr Bernardo Mercante, muito atencioso, explicou tudo sobre o meu problema; escoliose e indicou tratamento adequado. Consulta que deixa o paciente tranquilo e confiante nas respostas bem exemplificadas sobre a escoliose na terceira idade. Indico 100%."),
 "RM": dict(ini="R.M.", date="23/09/2026", local="C.O.T. - Centro Ortopédico e Traumatológico", text="Bem atendido desde a primeira consulta. Parabéns a toda equipe do Dr. Bernardo. Todos atenciosos. Dr. Bernardo é um excelente profissional!"),
 "CFSF": dict(ini="C.F.S.F.", date="22/09/2026", local="CIDOR · Consulta especialista em dor", text="O atendimento foi conforme o esperado de uma consulta médica, fui bem atendido, foram feitos os exames clínicos e fui encaminhado para exames de imagem que identifiquem com detalhes qual será o melhor procedimento para o meu caso. Agradeço pelo ótimo atendimento."),
}
# slide types: cover, card (pre, hi, post), item (title, body), review, cta
POSTS = [
 dict(id="ST01_joelho_escadas", tema="JOELHO", photo="bernardo_28_jaleco_mesa_modelos.jpg", pos="62% 30%",
  slides=[
   dict(t="cover", pre="Seu joelho dói ao ", hi="descer escadas?", sub="Isso pode ser um alerta."),
   dict(t="card", pre="Dor ao descer escadas pode indicar", hi="desgaste da cartilagem ou lesão no menisco."),
   dict(t="card", pre="Descer degraus exige mais do joelho do que caminhar no plano.", hi="Por isso a dor costuma aparecer primeiro ali."),
   dict(t="card", pre="A boa notícia é que, com o diagnóstico certo,", hi="fortalecimento, infiltração e outros tratamentos podem aliviar a dor.", post="Em muitos casos, sem cirurgia."),
   dict(t="review", r="DMCS"),
   dict(t="cta", q="Você também sente dor ao descer escadas?", hi='Comente "JOELHO"', post=" e veja como eu posso te ajudar."),
  ],
  caption="""Dor no joelho ao descer escadas não é "coisa da idade".

Ela pode ser um sinal de desgaste da cartilagem ou de lesão no menisco. E quanto antes você entende a causa, mais opções de tratamento existem.

👉 Comente "JOELHO" e veja como eu posso te ajudar."""),
 dict(id="ST02_coluna_hernia_5_problemas", tema="COLUNA", photo="bernardo_41_jaleco_recepcao_cidor.jpg", pos="18% 30%",
  slides=[
   dict(t="cover", pre="Só quem tem ", hi="hérnia de disco", post=" vai entender esses 5 problemas aqui"),
   dict(t="item", title="Dor que desce para a perna:", body="A dor sai da lombar e desce pela nádega e pela perna, às vezes até o pé."),
   dict(t="item", title="Formigamento:", body="Sensação de dormência ou choque na perna, que piora sentado ou ao tossir."),
   dict(t="item", title="Noites mal dormidas:", body="Difícil achar uma posição confortável. Virar na cama já dói."),
   dict(t="item", title="Medo de se abaixar:", body="Pegar algo no chão ou calçar o sapato vira um momento de tensão."),
   dict(t="item", title="Cansaço emocional:", body="Conviver com dor todo dia afeta o humor, a paciência e a vontade de fazer o que gosta."),
   dict(t="review", r="VS"),
   dict(t="cta", q="Você se identificou com algum desses?", hi='Comente "COLUNA"', post=" e eu te mostro os caminhos de tratamento."),
  ],
  caption="""Hérnia de disco não é só dor nas costas.

Ela mexe com o sono, com a rotina e com o humor. Mas a maioria dos casos tem tratamento sem cirurgia, e o primeiro passo é uma avaliação bem feita.

Qual desses 5 problemas você mais sente?

👉 Comente "COLUNA" e eu te mostro os caminhos de tratamento."""),
 dict(id="ST03_joelho_historia_marcia", tema="JOELHO", photo="bernardo_61_terno_mesa_modelos.jpg", pos="64% 30%",
  slides=[
   dict(t="cover", pre="Márcia achava que a dor no joelho era coisa da idade... ", hi="até que parou de caminhar na praia."),
   dict(t="card", hi="Adiou a consulta por mais de um ano.", post="Tomava remédio por conta própria e seguia a rotina..."),
   dict(t="card", pre="Até que", hi="levantar da cadeira virou um esforço", post="e ela desistiu das caminhadas."),
   dict(t="card", pre="Com exame físico e ultrassom no consultório,", hi="identificamos artrose no joelho."),
   dict(t="card", pre="Tratamos com infiltração de ácido hialurônico e fortalecimento,", hi="e ela voltou a caminhar com muito menos dor.", foot="Caso ilustrativo. Os resultados variam de pessoa para pessoa."),
   dict(t="card", pre="Hoje ela sabe:", hi="dor não é coisa da idade. É um sinal que merece atenção."),
   dict(t="review", r="AC"),
   dict(t="cta", q="Você também acha que sua dor no joelho é da idade?", hi='Comente "JOELHO"', post=" que eu posso te ajudar."),
  ],
  caption="""Dor no joelho não precisa ser aceita como parte da idade.

Artrose tem tratamento, e muitas vezes ele começa sem cirurgia: infiltração, fortalecimento e acompanhamento.

O mais importante é não esperar a dor tirar de você o que você gosta de fazer.

👉 Comente "JOELHO" que eu posso te ajudar.

*Caso ilustrativo. Os resultados variam de pessoa para pessoa."""),
 dict(id="ST04_coluna_acordar_travado", tema="COLUNA", photo="bernardo_52_terno_fundo_neutro.jpg", pos="42% 25%",
  slides=[
   dict(t="cover", pre="Acordar com a coluna travada ", hi="não é normal."),
   dict(t="card", pre="Rigidez que demora a passar, dor ao calçar o sapato, fisgada ao levantar da cama...", hi="são sinais de alerta."),
   dict(t="card", pre="Eles podem indicar", hi="hérnia de disco, desgaste ou inflamação nas articulações da coluna."),
   dict(t="card", pre="A boa notícia é que tratamentos minimamente invasivos, como bloqueios guiados por imagem,", hi="podem ajudar a aliviar a dor e devolver movimento."),
   dict(t="review", r="VG"),
   dict(t="cta", q="Você acorda com a coluna travada?", hi='Comente "COLUNA"', post=" e veja como eu posso te ajudar."),
  ],
  caption="""Você chama de "dormi de mau jeito". Seu corpo pode estar dando um aviso.

Acordar travado com frequência é um sinal de que algo na coluna precisa de atenção. Com avaliação e o tratamento certo, dá para voltar a acordar com mais leveza.

👉 Comente "COLUNA" e veja como eu posso te ajudar."""),
 dict(id="ST05_joelho_5_sinais", tema="JOELHO", photo="bernardo_24_jaleco_mesa_sorrindo.jpg", pos="44% 25%",
  slides=[
   dict(t="cover", pre="5 sinais de que seu ", hi="joelho está pedindo ajuda"),
   dict(t="item", title="Estalos com dor:", body="Estalo sozinho costuma ser tranquilo. Estalo acompanhado de dor merece avaliação."),
   dict(t="item", title="Inchaço depois do esforço:", body="O joelho incha depois de caminhar, treinar ou ficar muito tempo em pé."),
   dict(t="item", title="Sensação de falseio:", body="Parece que o joelho vai \"sair do lugar\" ou falhar ao pisar."),
   dict(t="item", title="Dor ao agachar:", body="Agachar, ajoelhar ou sentar no chão vira um desafio."),
   dict(t="item", title="Travamento:", body="O joelho trava em algum movimento e você precisa \"destravar\" para seguir."),
   dict(t="review", r="RM"),
   dict(t="cta", q="Quantos desses sinais você tem?", hi='Comente "JOELHO"', post=" e entenda como eu posso te ajudar."),
  ],
  caption="""Seu joelho avisa antes de limitar.

Estalos com dor, inchaço, falseio, dor ao agachar e travamento são sinais que não devem ser ignorados. Quanto antes a causa é encontrada, mais simples costuma ser o caminho.

Quantos desses você sente?

👉 Comente "JOELHO" e entenda como eu posso te ajudar."""),
 dict(id="ST06_coluna_historia_carlos", tema="COLUNA", photo="bernardo_36_jaleco_ultrassom.jpg", pos="20% 25%",
  slides=[
   dict(t="cover", pre="Carlos achava que a dor que descia para a perna era mau jeito... ", hi="até que não conseguia mais dirigir."),
   dict(t="card", hi="Ignorou os sinais por meses.", post="Trocou o colchão, fez massagem, tomou relaxante..."),
   dict(t="card", pre="Até que", hi="a dor e o formigamento na perna", post="não deixavam ele ficar 10 minutos sentado no carro."),
   dict(t="card", pre="Com exame físico e ressonância,", hi="identificamos uma hérnia de disco comprimindo o nervo ciático."),
   dict(t="card", pre="Tratamos com bloqueio guiado por imagem e reabilitação,", hi="e ele voltou a dirigir com muito menos dor.", foot="Caso ilustrativo. Os resultados variam de pessoa para pessoa."),
   dict(t="card", pre="Hoje ele sabe:", hi="dor que desce para a perna não é mau jeito."),
   dict(t="review", r="CFSF"),
   dict(t="cta", q="Você sente dor que desce para a perna?", hi='Comente "COLUNA"', post=" que eu posso te ajudar."),
  ],
  caption="""Dor que desce para a perna não é "mau jeito".

Ela pode indicar um nervo comprimido, como acontece na hérnia de disco. A boa notícia é que existem tratamentos minimamente invasivos que podem aliviar a dor e ajudar você a voltar à rotina.

👉 Comente "COLUNA" que eu posso te ajudar.

*Caso ilustrativo. Os resultados variam de pessoa para pessoa."""),
]
