# LaTeX user template and guide

To compile user guide:

```shell
  cd src
  rm -r ../out/
  pdflatex sample-2col -output-directory=../out 
  bibtex ../out/sample-2col 
  pdflatex sample-2col -output-directory=../out 
  pdflatex sample-2col -output-directory=../out
```
