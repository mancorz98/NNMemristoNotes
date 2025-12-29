# [Polska wersja pliku](main.pdf)
# [English file version](main_en.pdf)
# [IEEE format file version](main_ieee.pdf)


# WARNING: 
IEEE version of file, For compilation is using memoize package to cache tikz picture temporary file, to not compiling tikz pictures for every compilation. For this project `Python` version is involved. 
Instalation: http://polish-mirror.evolution-host.com/ctan/macros/generic/memoize/doc/memoize-doc.pdf
If the `Python` is installed, for the `UNIX` systems,  type in terminal: 
```bash
$(which python3)  -m pip install --break-system-packages  pdfrw2
```

# Removing adnotation

To remove approved changed commands from the text you can use prepared python script: 
```bash
python replace_changed.py $inputFile $outputFile
```



### 2025-09-10 Meeting notes:
  - [x] controversial constraints function 
  - [x] problem with the notation for Algorithm 1
  - [x] controversial $\mathcal{L}_{iv}$ loss function
  - [x] controversial way to describe hyperparameter results
  - [x] show detailed results as table

### 2025-10-03 Meeting notes: 
  - [x] Rewrite to the IEEE format, 
  - [x] Use test loss instead of full loss, 
  - [x] Add information about specific Neural Architecture structure,


### 2025-10-22 Meeting notes: 
  - [x] Controversial validation metrics


### 2025-11-21
  - [x] Controversial Algorithm. 1
  - [x] Compare the evaluation time
  - [x] Extend training time section
  - [x] Analyse, the hyperparameter space influence
  

### 2025-12-29 
  - [ ] Zgodnie z tym co napisałem przed Świętami trzeba przerobić artykuł, zwłaszcza "Introduction" zgodnie z uwagami EiC. Ma rację, jest mało opisu na temat modeli memrystorów, a dużo na temat zastosowań sieci neuronowych, doboru parametrów, itp. Ponieważ wysyłamy pracę do TCAS, to trzeba zmienić proporcje.

  - [ ] Proszę, dokonaj zmian w rozdziale 1. Trzeba mniej napisać na temat Neural ODE (w szczególności trzeba usunąć paragraf zaczynający się od słów "In [5], the authors extend the classical Neural ODE". Nie korzystamy z tej wersji, więc nie ma sensu o tym pisać. Trzeba dodać więcej opisów na temat modeli i modelowania memrystorów. Trzeba dodać więcej cytowań prac z TCAS1 i TCAS2 (możesz dodać jakieś cytowanie mojego artykułu z tych czasopism, żeby było wiadomo, że zajmowaliśmy się wcześniej memrystorami), a usunąć cytowania, które nie są niezbędne, z czasopism i konferencji poświęconych innym tematom (Neural Information Processing, Learning representations, Computer Vision, Pattern Recognition, Machine learning, Energies, itd.).

  - [ ] W pozostałych rozdziałach lepiej usunąć/skrócić opisy zalet stosowanych metod (np. Diffrax, tsit5, L-BFGS-B, TPE), które wyglądają jakby były skopiowane z oryginalnych artykułów. Nie musimy podkreślać ich zalet. Jeśli są, to wystarczy je wymienić bez dodatkowych ozdobników.

  - [ ] Rozdział III B. Hyperparameter Sensitivity Analysis sprawia wrażenie, że koncentrujemy się na wykorzystaniu sieci neuronowych, co może nie być pożądane przez TCAS 1, ale proponuję to zostawić (może nieco skrócić). Zobaczymy jakie będą uwagi recenzentów, jeśli w ogóle artykuł zostanie przyjęty do tego etapu.



