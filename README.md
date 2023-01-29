# Optimization of the structure of a full-text search index using neural networks of the "Transformer" architecture

Requirements:
- In order to add SVG files to a document at compile time, you need an Inkscape. Installation example for macOS: `brew install inkscape`

To compile user guide:

```shell
  cd src
  rm -r ../out/
  mkdir ../out/
  pdflatex --shell-escape -output-directory=../out search-index-article
  cd ../out 
  BIBINPUTS="../src" bibtex search-index-article
  cd ../src
  pdflatex --shell-escape -output-directory=../out search-index-article 
  pdflatex --shell-escape -output-directory=../out search-index-article
```

The --shell-escape option allows the running program to invoke an external program, in this case, Inkscape.
