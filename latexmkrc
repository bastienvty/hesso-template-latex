# latexmkrc
add_cus_dep('glo', 'gls', 0, 'makeglossaries');
sub makeglossaries { system("makeglossaries $_[0]"); }
$bibtex = 'biber';
$pdflatex = 'pdflatex -synctex=1 -interaction=nonstopmode -file-line-error -recorder -shell-escape %O %S';
