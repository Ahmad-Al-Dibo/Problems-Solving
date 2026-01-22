## Technisch Verslag – Two Sum Probleem

### 1. Inleiding

Dit verslag beschrijft de analyse en oplossing van het *Two Sum*-probleem, een veelvoorkomend algoritmisch probleem binnen de informatica. Het doel is om twee indices te vinden van elementen in een lijst waarvan de som gelijk is aan een gegeven doelwaarde (*target*). De nadruk ligt op het oplossingsproces, de gebruikte datastructuren en de efficiëntie van het algoritme.

---

### 2. Probleemdefinitie

Gegeven:

* Een lijst `nums` met gehele getallen
* Een geheel getal `target`

Doel:

* Bepaal twee **verschillende indices** `i` en `j` zodat:
  [
  nums[i] + nums[j] = target
  ]

Beperkingen (constraints):

* (2 \leq \text{len(nums)} \leq 10^4)
* (-10^9 \leq nums[i], target \leq 10^9)

---

### 3. Intuïtie

Een brute-force aanpak, waarbij alle mogelijke paren worden vergeleken, heeft een tijdscomplexiteit van (O(n^2)) en is inefficiënt voor grote invoer.
De kernintuïtie van de efficiënte oplossing is dat bij elk element slechts gekeken hoeft te worden of het *complement* (het getal dat nodig is om `target` te bereiken) al eerder is voorgekomen.

---

### 4. Aanpak

De oplossing maakt gebruik van een **hashmap (dictionary)** om eerder bezochte getallen op te slaan, samen met hun index. Hierdoor kan in constante tijd ((O(1))) worden gecontroleerd of een complement bestaat.

#### Stappen:

1. **Validatie van invoer**
   Met `assert`-statements wordt gecontroleerd of de invoer voldoet aan de gestelde constraints.
2. **Initialisatie van datastructuur**
   Een lege dictionary `seen` wordt aangemaakt.
3. **Iteratie door de lijst**
   Voor elk element `num` op index `i`:

   * Bereken het complement:
     [
     complement = target - num
     ]
   * Controleer of dit complement al bestaat in `seen`
   * Zo ja: retourneer de indices
   * Zo nee: sla het huidige getal en de index op in `seen`

---

### 5. Procesbeschrijving

Aanvankelijk was het probleem conceptueel lastig, omdat de logica van het opslaan en terugvinden van eerder verwerkte waarden niet direct duidelijk was. Door de oplossing meerdere malen opnieuw te implementeren en te analyseren, werd het onderliggende principe inzichtelijk:
namelijk dat elk getal slechts één keer hoeft te worden bekeken, zolang eerdere waarden efficiënt worden opgeslagen.

---

### 6. Implementatie (Eigen Code)

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        # Validatie van constraints
        assert -10**9 <= target <= 10**9
        assert 2 <= len(nums) <= 10**4
        for x in nums:
            assert -10**9 <= x <= 10**9

        # Hashmap voor eerder geziene getallen
        seen = {}
        for i, num in enumerate(nums):
            oppr = target - num
            if oppr in seen:
                return [seen[oppr], i]
            seen[num] = i
```

---

### 7. Vergelijking met AI-oplossing

De AI-oplossing is functioneel identiek aan de eigen implementatie. Het verschil zit voornamelijk in:

* Naamgeving (`complement` i.p.v. `oppr`)
* Iets explicietere commentaarregels

Algoritmisch en qua efficiëntie zijn beide oplossingen gelijkwaardig.

---

### 8. Complexiteitsanalyse

* **Tijdcomplexiteit:**
  [
  O(n)
  ]
  Elke invoerwaarde wordt exact één keer verwerkt.

* **Ruimtecomplexiteit:**
  [
  O(n)
  ]
  In het slechtste geval worden alle elementen opgeslagen in de dictionary.

---

### 9. Conclusie

Door het gebruik van een hashmap kan het *Two Sum*-probleem efficiënt worden opgelost binnen lineaire tijd. Deze aanpak is aanzienlijk beter dan een brute-force methode en vormt een belangrijk voorbeeld van hoe geschikte datastructuren de prestaties van algoritmen drastisch kunnen verbeteren. Het herhaald implementeren en analyseren van de oplossing droeg bij aan een dieper begrip van het algoritmische denkproces.

<details>
    <summary>Hand verslag</summary>
    # Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
Oplossen van dit probleem is niet lastig maar alleen als je snapt. ik vond het moeilijk in het begit, tot dat ik snapte hoe Ai heeft het opgelost. Ik heb deze opdracht vaak opnieuw gedaan tot het ik snapte.

## procces
Het oplossing was eerste je checkt of het inputs voldoen aan het gestelde eisen, dan maak je dic `seen`. Deze dic bewaart alle mogelijke getallen zoals `target = 6, numbers = [3, 2, 4]` na het checken als ze aan de gestelde eisen voldoen, gaan we loop op het numbers lopen en soren we i het index getal en n het getal zelf, dan trek je het getal af van target (sla je het in `oppr`) en check je als het output van het `oppr` in `seen` want als het getal in `seen` is dan kunnen we het index van het getal hallen en het getal van `oppr`

# My Code

```python3 []
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        assert -10**9 <= target <= 10**9
        assert 2 <= len(nums) <= 10**4
        for x in nums:
            assert -10**9 <= x <= 10**9

      
        seen = {}
        for i, num in enumerate(nums):
            oppr = target - num
            if oppr in seen:
                return [seen[oppr], i]
            seen[num] = i 

```

# Ai Code
```python3 []
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Validatie van constraints
        assert -10**9 <= target <= 10**9
        assert 2 <= len(nums) <= 10**4
        for x in nums:
            assert -10**9 <= x <= 10**9

        # Gebruik een hashmap (dictionary) voor snelle lookup
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
```



</details>

