FROM ghcr.io/bastienvty/latexdevcontainer:latest
RUN apt-get update && apt-get install -y --no-install-recommends fontconfig fonts-dejavu python3-pygments python3-pip python3-venv \
    && rm -rf /var/lib/apt/lists/*
RUN tlmgr update --self && \
tlmgr install algorithmicx \
    algorithms \
    algpseudocodex \
    float newfloat \
    caption \
    placeins \
    booktabs \
    multirow \
    makecell \
    biblatex \
    biber \
    tocloft \
    minitoc \
    xcolor \
    mdframed \
    zref \
    needspace \
    minted \
    upquote \
    lineno \
    comment \
    csquotes \
    nowidow \
    microtype \
    parskip \
    nth \
    paralist \
    enumitem \
    titlesec \
    lipsum \
    blindtext \
    pdflscape \
    todonotes \
    glossaries \
    cmbright \
    kpfonts \
    cleveref \
    libertinus libertinus-type1 unicode-math fontaxes \
    sourcecodepro inconsolata \
    tcolorbox \
    babel-french hyphen-french \
    ly1 \
    pgfplots fontawesome5 \
    glossaries-english glossaries-french \
    xetex fontspec \
    threeparttable siunitx
    # collection-fontsrecommended
RUN texhash && \
    tlmgr update --self --all && \
    mktexlsr && \
    fmtutil-sys --all

# Install Pygments custom style
COPY styles/ /tmp/styles/
RUN pip install --break-system-packages /tmp/styles/ && rm -rf /tmp/styles/
