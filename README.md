# 3 EN RAYA 
**Autors**
Nadia Fernández
Paula Justo
---
Aquest repositori conté una implementació avançada i personalitzable del joc del **Tres en Ratlla**, desenvolupada com a part d'un projecte de programació. El joc inclou tant una versió bàsica com una ampliada amb reptes matemàtics, personalització de jugadors i interfície gràfica.

## Estructura del Repositori

El projecte està organitzat en dues versions:

* **`bàsic/`**: Implementació fonamental del joc amb les regles clàssiques.
* **`implementat/`**: Versió millorada que inclou configuracions de partida, modes de dificultat i personalització visual.
* **`Informe_NadiaFernandez_PaulaJusto.pdf`**: Documentació detallada del disseny i desenvolupament.

## Característiques Principals

### Personalització Total
A la versió ampliada, els usuaris poden configurar:
* **Mida del taulell (BSIZ):** Mida dinàmica (mínim 3x3).
* **Quantitat de pedres:** Nombre de peces per jugador totalment ajustable.
* **Mode de joc:** * *Classic*: Guanya qui aconsegueix fer la línia.
    * *Inverse*: Guanya qui evita fer el tres en ratlla.
* **Identitat:** Elecció de *nickname* i colors personalitzats (via mòdul `colored`).

### Reptes de Càlcul (Dificultat)
Per afegir una capa d'habilitat extra, el joc inclou modes on cal respondre operacions per poder tirar:
* **Sum mode**: Dificultat baixa (sumes aleatòries).
* **Multiplication mode**: Dificultat alta (multiplicacions aleatòries).
* *Si el jugador falla l'operació, perd el torn.*

## Requisits i Instal·lació

El projecte requereix Python 3 i les següents llibreries addicionals per a la versió completa:

```
pip install pygame
pip install coloured
```
