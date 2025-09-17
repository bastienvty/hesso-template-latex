# Waiting for this image to update to TeX Live 2025
# FROM qmcgaw/latexdevcontainer
FROM skrallex/latexdevcontainer
RUN apt-get update && apt-get install -y python3 python3-pip
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
    libertinus libertinus-type1 fontaxes \
    sourcecodepro inconsolata \
    tcolorbox \
    babel-french hyphen-french \
    ly1 \
    glossaries-english glossaries-french
RUN texhash && \
    tlmgr update --self --all && \
    mktexlsr && \
    fmtutil-sys --all

