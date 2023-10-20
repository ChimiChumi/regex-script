## Különböző műveletek REGEX-el

### Megvalósított részek:
- fájl írás/olvasás és working-directory útvonal beállítása
- egyszerű regex matchelés (szavak amik tartalmaznak 'bb'-t)
- lookahead "example" szóra
- telefonszám formázás
- capturing group (számok átalakítása: ONE, TWO --> 1, 2 etc.)
- backreference (azonos betűvel kezdődő és végződő szavak)
- lazy/greedy összehasonlítása, hatékonysága:
  - Pythonban a reguláris kifejezések motorjai hatékonyan vannak optimalizálva emiatt néhány esetben a lazy és greedy közötti különbségek nem olyan hangsúlyosak, mint más nyelvek regex motorjaiban
  - Ebben a példában a lazy iteration `(a+?)` a lehető legkevesebb `a` karaktert fogja megfeleltetni a `a+b` mintázat előtt, ami "a" illeszkedést eredményez. A greedy bejárásnál `(a+)` a lehető legtöbb `a` karaktert fogja megfeleltetni a `a+b` mintázat előtt, ami "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" illeszkedést eredményez.