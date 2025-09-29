## Install fonts for XeLaTeX and LuaLaTeX

To use the fonts you want with XeLaTeX or LuaLaTeX, you can install them in the `fonts/` directory. For example, you can download the [Libertinus](https://github.com/Libertinus/Libertinus) font package.

Then, you can configure the fonts in `settings/fonts.tex`. Here is an example configuration using the Libertinus font:

```latex
% Load fontspec package for font selection
\usepackage{fontspec}
\setmainfont{LibertinusSerif}[
    Path=./fonts/Libertinus-7.051/OTF/,
    Extension=.otf,
    UprightFont=*-Regular,
    BoldFont=*-Bold,
    ItalicFont=*-Italic,
    BoldItalicFont=*-BoldItalic
]

\setsansfont{LibertinusSans}[
    Path=./fonts/Libertinus-7.051/OTF/,
    Extension=.otf,
    UprightFont=*-Regular,
    BoldFont=*-Bold,
    ItalicFont=*-Italic
]

\setmonofont{LibertinusMono}[
    Path=./fonts/Libertinus-7.051/OTF/,
    Extension=.otf,
    UprightFont=*-Regular
]

% Use Libertinus Math for mathematics
\usepackage{unicode-math}
\setmathfont{LibertinusMath-Regular.otf}[
    Path=./fonts/Libertinus-7.051/OTF/
]
```
