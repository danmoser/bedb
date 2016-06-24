BeDB
=======
Introdução
-----------
**Banco de dados de parâmetros físicos de estrelas Be**

Visão geral:

- As entradas são baseadas em arquivos texto (idealmente que possam ser lidos pelo ``np.loadtxt``). A ideia é aproveitar os arquivos que vêm do Vizier, e que seja fácil alimentarmos nossos próprios dados. Cada linha, uma entrada, e estruturada por "colunas". 
- Duas colunas obrigatórias: um *ID* para o objeto e *ref* para a referências. 
- Cada entrada tem um *key* (ou label) específico. Assume-se padronização nos rótulos e unidades (ler *unit definitions*).
- O funcionamento é simples: entra-se com um valor ou uma lista de IDs e um rótulo (ou uma lista dos mesmos) e o robô do banco de dados faz uma busca pelos arquivos para todas as ocorrências da estrela de um ID que contenha um dos rótulos.

Comandos úteis
------------------
.. code:: python

    # in the directory of BeDB:
    import bedb

    idlist = ['aeri', 'hd11444']
    for id_ in idlist:
        bedb.show_id_results(id_)

Estrutura de arquivos
-----------------------
A proposta é manter o seguinte:

.. code::

    - README.rst  # este leia-me
    - bedb.py  # modulo do bando de dados
    - refs.bib  # arquivo BibTex contendo as informacoes das referencias
    - IDs.txt  # arquivo com os identificadores de cada estrela Be
    -- BeDB/*.bdb  # pasta com arquivos que serão consultados pelo robô
    -- srcs/*.*  # pasta com arquivos fonte com as infos originais (Vizier, p.e.)
    -- scripts/*.py  # pasta comscripts para transformar src > bdb

IDs.txt
~~~~~~~~~
Todas as Be no BeDB devem conter um *ID* para identificação do alvo. Um dado alvo pode conter múltiplos IDs. A associação entre um dado alvo é feita por este arquivo. Note que para consultar o BeDB a estrela não precisa estar do ``IDs.txt`` - porém é o recomendável para as Be, a fim de se evitar que perder informação por não se utilizar o *ID* padrão.

- A regra é simples: cada linha, uma estrela. 
- Separador são vírgulas, e **espaço não é um caracter válido** para o ID. 
- Também, maiúsculas são sempre convertidas para minúsculas.
- Por exemplo, "HR 5907" é igual a "hr5907" (no momento da leitura deste arquivo, o robô ignora os espaços e converte para "lowercase").

refs.bib
~~~~~~~~~
- Outra coluna obrigatória é a coluna *ref* para ser recuperar a citação original. 
- Esta coluna pode ser opcional - mas neste caso, assume-se que o arquivo ``*.bdb`` inicia seu nome com o identificador da referencia (que é única para todo o conteúdo do arquivo).
- Portanto múltiplas referências necessariamente devem ser fornecidas por meio de coluna (e não no nome do arquivo).
- o formato da coluna é "AAA00a", com "AAA" sendo as 3 letras iniciais do primeiro autor, e 00 o ano de publicação.
- a flag "a" é obrigatória e é usada para diferenciar artigos de mesmos autores com letras iniciais e ano de publicação.

``*.bdb``
~~~~~~~~~~~~
- Estes artigos podem ter distintos formatos. A ideia é facilitar a criação de novas entradas.
- Então, antes da extensão ``.bdb`` adiciona-se ``_00``, onde 00 é um identificador para o robô saber ler corretamente este arquivo. 
- A ideia é que estes arquivos sejam independentes dos arquivos em ``scrs``. Não há problema em uma entrada conter mais de um arquivo, desde que respeite o identificador acima.


key definitions
------------------
- A ideia é deixar tudo "pronto para uso". Porém, isso depende muito da aplicação desejada... A lista abaixo foi criada no contexto dos parâmetros do BeAtlas, mas evidentemente será adaptada no futuro.
- Provavelmente, o mais seguro é fazer uma busca por alvo: e aí o robô informa quais referências possuem aquela estrela, e aí se adaptam os valores.
- Na lista abaixo, "intrínseco" significa grandezas que (i) não dependem de efeitos de projeção **e** (ii) foram corrigidas de vieses introduzidos pelos efeitos da rotação.

======= ==========================================
M       Mass, Msun
W       Vrot/Vorb
Vrot    (V=intrinsic), km/s
vsini   (v=apparent), km/s
Vsini   (V=intrinsic), km/s
i       inclination angle, deg
Rp      Polar radius, Rsun
ReRp    Radii ratio, Req/Rpole
logg    (l=apparent), cgs units
Logg    (L=intrinsic), cgs units
Vc      Critical velocity, km/s
teff    (t=apparent Temp. eff.), Kelvin
Teff    (T=intrinsic Temp. eff.), Kelvin
Lum     Luminosity, Lsun
d       distance, pc
PA      on-sky orientation (N > E), deg
beta    Von Zeipel coefficient
b_sh    has shell feature history
polV    polarization, %
magV    photometry, Vega
======= ==========================================

Unit definitions
~~~~~~~~~~~~~~~~~
- Usar W: não usar v/v_crit ou Omega/Omega_crit.
- Lum = area_star * sigma * Teff**4
- Usar d: não usar plx

Errors
~~~~~~~~
- Os erros devem ser precedidos por *e_* e usar o mesmo rótulo daquela variável. 
- Assume-se erro simétrico. Caso não seja, usar rótulo *l_*, onde o *e* vai ser assumido como o erro superior e *l* como o inferior.
- Note que os erros tem valores como :math:`\sigma`. Ou seja, grava-se **a diferença** para o valor do rótulo.
- Por exemplo, *M = 13* variando de 12 a 14 Msun, grava-se *e_M = 1.0* (não grava-se *l_M*, ou deixa-se *l_M = 0*).
- Exemplo 2, *M = 12.5* variando de 12 a 14 Msun, grava-se *e_M = 1.5* e *l_M = 0.5*.

Boolean quantities
~~~~~~~~~~~~~~~~~~~~
- Os rótulos são precedidos por *b_* e os valores deve ser sempre 0 ou 1.

Time-flag
~~~~~~~~~~~
- Uma coisa muito útil para dados de fotometria (ou outros, dependendo do contexto - como *vsini* variável de Achernar) é adicionar a informação temporal do dado. Sugestão de usar *J_* para dia juliano, e *M_* para o dia juliano modificado.


TODOs
--------
- Definir grandezas para caracterização do disco CS.

Dados de espectroscopia e outros
---------------------------------
- Acho que não devem ficar abrigados aqui no BeDB. Os headers dos arquivos FITS são um mecanismo muito melhor para se salvar informações extras...
- Um banco de dados de espectroscopia deve ficar a cargo do Beacon.                                                         