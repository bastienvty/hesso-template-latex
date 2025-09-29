FROM ghcr.io/bastienvty/latexdevcontainer:latest
RUN apt-get update && apt-get install -y --no-install-recommends fontconfig fonts-dejavu
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
    libertinus libertinus-type1 unicode-math fontaxes \
    sourcecodepro inconsolata \
    tcolorbox \
    babel-french hyphen-french \
    ly1 \
    glossaries-english glossaries-french \
    xetex fontspec
    # collection-fontsrecommended
RUN texhash && \
    tlmgr update --self --all && \
    mktexlsr && \
    fmtutil-sys --all
