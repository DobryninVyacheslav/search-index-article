# Optimization of the structure of a full-text search index using neural networks of the "Transformer" architecture

Requirements:
- In order to add SVG files to a document at compile time, you need an Inkscape. Installation example for macOS: `brew install inkscape`

To compile user guide:

```shell
  cd src
  rm -r ../out/
  pdflatex --shell-escape search-index-article -output-directory=../out 
  bibtex ../out/search-index-article 
  pdflatex --shell-escape search-index-article -output-directory=../out 
  pdflatex --shell-escape search-index-article -output-directory=../out
```

The --shell-escape option allows the running program to invoke an external program, in this case, Inkscape.
