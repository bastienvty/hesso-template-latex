# # --- engine / runs ---
# # No need as latex-workshop sets these in its `latexmk` tool args
# $pdf_mode = 1;                 # = -pdf
# $synctex  = 1;                 # = -synctex=1
# $interaction = 'nonstopmode';  # = -interaction=nonstopmode
# $file_line_error = 1;          # = -file-line-error

# # --- output locations ---
$out_dir = 'output';           # = -outdir=...
$aux_dir = 'output/extra';     # = -auxdir=...

# --- bibliography ---
# If we use biblatex+biber, latexmk normally auto-detects biber.
# If we want to force it explicitly, uncomment the next line:
# $bibtex = 'biber %O %B';

# --- glossaries ---
use File::Basename;
add_cus_dep('glo', 'gls', 0, 'makeglossaries');
sub makeglossaries {
  my ($base) = @_;                 # e.g. "output/extra/report"
  my $dir  = dirname($base);       # -> "output/extra"
  my $name = basename($base);      # -> "report"
  return system("makeglossaries -d \"$dir\" \"$name\"");
}
