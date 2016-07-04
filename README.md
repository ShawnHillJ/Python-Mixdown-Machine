# Python-Mixdown-Machine
A simple script that accepts a pattern and overlays it onto a base song.
In order to use this, you must have Python 2.7 and Pydub.
The template uses these characters:
'_' is a blank space of 1/10 a second.
'#' is a number from 1-3 that indicates the subclip number.
'x' is a special character that defines a multiple number of one code. By following the 'x' with a character from above and a two digit number, such as '99', you can indicate the times necessary to repeat the command.
