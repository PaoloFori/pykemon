
from Character import Character
from BaseStats import BaseStats
from MN import MN
pokedex ={
    1 : Character('bulbasaur', ['grass', 'poison'], BaseStats(45, 49, 49, 45, 65), [MN['tackle'], MN['razor leaf']]),
    4 : Character('charmander', ['fire'], BaseStats(39, 52, 43, 65, 50), [MN['tackle'], MN['ember']]),
    7 : Character('squirtle', ['water'], BaseStats(44, 48, 65, 43, 50), [MN['tackle'], MN['water gun']]) 
}
