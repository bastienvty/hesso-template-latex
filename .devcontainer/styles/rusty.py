from pygments.style import Style
from pygments.token import (
    Comment, Keyword, Name, String, Number, Operator, Punctuation, Generic, Token, Literal
)

class RustyStyle(Style):
    """GitHub-style syntax highlighting optimized for Rust."""

    background_color = "#ffffff"

    styles = {
        Token:                  "#24292f",

        # Comments - gray italic
        Comment:                "italic #6e7781",
        Comment.Multiline:      "italic #6e7781",
        Comment.Single:         "italic #6e7781",
        Comment.Preproc:        "#cf222e",

        # Keywords - red (fn, let, mut, pub, impl, struct, enum, match, etc.)
        Keyword:                "#cf222e",
        Keyword.Constant:       "#0550ae",        # true, false
        Keyword.Declaration:    "#cf222e",        # let, const, static
        Keyword.Namespace:      "#cf222e",        # use, mod, crate
        Keyword.Reserved:       "#cf222e",
        Keyword.Type:           "#0550ae",        # i32, u64, bool, Self

        # Names
        Name:                   "#24292f",
        Name.Builtin:           "#0550ae",        # Option, Result, Vec, String
        Name.Function:          "#8250df",        # function names - purple
        Name.Function.Magic:    "#8250df",
        Name.Class:             "#0550ae",        # type names
        Name.Decorator:         "#6e7781",        # #[derive], #[test]
        Name.Attribute:         "#0550ae",
        Name.Label:             "#0550ae",        # lifetimes 'a
        Name.Tag:               "#0550ae",
        Name.Variable:          "#24292f",
        Name.Constant:          "#0550ae",

        # Macros - purple (println!, vec!, etc.)
        Name.Other:             "#8250df",

        # Strings - dark blue
        String:                 "#0a3069",
        String.Char:            "#0a3069",
        String.Doc:             "italic #6e7781",
        String.Escape:          "#cf222e",
        String.Interpol:        "#cf222e",
        String.Regex:           "#0a3069",
        String.Affix:           "#cf222e",

        # Numbers - blue
        Number:                 "#0550ae",
        Number.Float:           "#0550ae",
        Number.Integer:         "#0550ae",
        Number.Hex:             "#0550ae",
        Number.Oct:             "#0550ae",
        Number.Bin:             "#0550ae",

        # Literals
        Literal:                "#0550ae",

        # Operators - dark
        Operator:               "#24292f",
        Operator.Word:          "#cf222e",

        # Punctuation - dark
        Punctuation:            "#24292f",

        # Generic (diffs, etc.)
        Generic.Deleted:        "#82071e bg:#ffebe9",
        Generic.Inserted:       "#116329 bg:#dafbe1",
        Generic.Heading:        "bold #0550ae",
        Generic.Subheading:     "bold #0550ae",
        Generic.Emph:           "italic",
        Generic.Strong:         "bold",
        Generic.Error:          "#cf222e",
        Generic.Traceback:      "#cf222e",
    }
