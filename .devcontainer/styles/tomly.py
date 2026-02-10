from pygments.style import Style
from pygments.token import (
    Comment, Keyword, Name, String, Number, Operator, Punctuation, Generic, Token, Literal
)

class TomlyStyle(Style):
    """GitHub-style syntax highlighting optimized for TOML."""

    background_color = "#ffffff"

    styles = {
        Token:                  "#24292f",

        # Comments - gray italic
        Comment:                "italic #6e7781",
        Comment.Single:         "italic #6e7781",

        # Keywords (true, false)
        Keyword:                "#8250df",
        Keyword.Constant:       "#0550ae",

        # Names
        Name:                   "#24292f",
        Name.Builtin:           "#8250df",
        Name.Tag:               "#8250df",        # [section] headers
        Name.Attribute:         "#8250df",        # keys
        Name.Property:          "#8250df",        # keys
        Name.Label:             "#8250df",

        # Strings - dark blue
        String:                 "#0a3069",
        String.Basic:           "#0a3069",
        String.Double:          "#0a3069",
        String.Single:          "#0a3069",
        String.Escape:          "#cf222e",

        # Numbers - blue
        Number:                 "#0550ae",
        Number.Float:           "#0550ae",
        Number.Integer:         "#0550ae",

        # Literals (dates, times)
        Literal:                "#0550ae",
        Literal.Date:           "#0550ae",

        # Operators (=)
        Operator:               "#24292f",

        # Punctuation (brackets, commas)
        Punctuation:            "#24292f",

        # Generic
        Generic.Heading:        "#8250df",
        Generic.Emph:           "italic",
        Generic.Strong:         "bold",
        Generic.Error:          "#cf222e",
    }
