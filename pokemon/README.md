### Potentially interesting questions

Pokemon fanboy questions:
- team of 4-6 Pokemons to finish the game easily (constraint-solve type effectiveness)
- what makes a pokemon legendary?
- trends and correlations between/within "power", stats, and types
- type and stats distribution over generations
- widget/card summarizing fun Pokemon stats (generation introduced,

Amateur competitor questions: 
- typical team compositions
- typical moveset for a given Pokemon
- theoretical type effectiveness vs practical battle win rate (eg flying beats ice)
- widget/card providing best IV split, nature, moveset for a Pokemon

Semi-pro competitor questions:
- the chance that my opponent's Pokemon carries X move or Y item.
- how the meta has changed over time, so I can anticipate future changes.


### Existing questions/findings/viz

EDA [GgPlot ‘Em All ](https://towardsdatascience.com/exploratory-analysis-of-pokemons-using-r-8600229346fb)
- data: 41 columns. 
- high atk for fighting, high def for steel and rock pokemon (heatmap of x=type, y=stat, heat=avg value of this stats for this type)
- atk inversely correlated with spatk (heatmap of correl between stats)
- flying type Pokemon are highly effective against the ice type Pokemon while fire type Pokemon are not (type effectiveness heatmap)
- bunch of EDA of types and stats, split by gen, type, legendary. Correl of stats with lin fit.

[EDA](https://inmachineswetrust.com/posts/exploring-pokemon-dataset/)
- no type1=flying, but tons of Normal/Flying
- EDA types, introductions by gen, type1-type2 crosstab
- Slaking is strongest pokemon if normalizing stats
- bug is weak, dragon strong (even without leg), flying fast, rock/steel def (used type's median instead of mean)
- correl between stats
- used seaborn

[what makes a pokemon legendary?](https://www.datacamp.com/projects/712)
- feature importance with DT/RF 

[predict catch rate from stats and body](https://www.kaggle.com/jonathanbouchet/pokemon-data-clusters/data)
- lin reg, r2=.5
- compare catch rate, gender, stats between body types

[predict win rate from battle stats](https://www.kaggle.com/jonathanbouchet/pokemon-battles)
- use difference in stats between the 2 opponents to predict winner
- used GBM, SVM, around 90% accuracy.
- decision tree shows diff in speed biggest predictor. AUC=.948

[pie plot](https://www.kaggle.com/gurarako/visualization-using-seaborn-pokemon-part-1)
- also type crosstab

[radar plot of the 6 stats of each pokemon](https://public.tableau.com/profile/julien.marmiesse#!/vizhome/Pokemon-GottaAnalyseThemAll/Pokemon-GottaAnalyseThemAll), in tableau


### Datasets

https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6
721 pokemons
Columns: Name 	Type 1 	Type 2 	Total 	HP 	Attack 	Defense 	Sp. Atk 	Sp. Def 	Speed 	Generation 	Legendary

https://www.kaggle.com/rounakbanik/pokemon
41 columns x 802 pokemons

https://www.kaggle.com/jonathanbouchet/pokemon-data-clusters/report

https://github.com/veekun/pokedex - all possible data from gen 1-7

https://www.kaggle.com/abcsds/pokemongo
151 pokemons
Pokemon No. Name Type 1 Type 2 Max CP Max HP Image URL

https://www.smogon.com/stats/ with [FAQ](https://www.smogon.com/forums/threads/official-smogon-university-usage-statistics-discussion-thread-mk-3.3591776/#post-7171782)