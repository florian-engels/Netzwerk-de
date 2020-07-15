# Netzwerk-de

1. Zu Beginn klone dieses Repository.

2. Klone das Git Repository PyPSA-eur.

3. Installiere Anaconda oder Miniconda:
https://docs.conda.io/projects/conda/en/latest/user-guide/install/

4. Führe nun die initialize.sh Datei auf dem pypsa-eur repository aus.

5. Erstelle ein Beispielnetz von 5 Knoten mithilfe der make_network.sh Datei, ebenfalls auf dem pypsa-eur repository.

6. Führe das Python Script "Admittance Matrix" im Ordner ".../pypsa-eur/results/networks" aus. 
Hier entsteht nun eine Admittance Matrix.


## Vorsicht!

Falls es einen Fehler der Form
`assert results['Solver'][0]['Status'].key == 'ok', "Solver returned non-optimally: {}".format(results)
AttributeError: 'SolverStatus' object has no attribute 'key'`

gibt, so liegt das an einem aktuellen (09.07.20) Bug in pypsa:
https://github.com/PyPSA/PyPSA/issues/186

das kann gelöst werden, indem man in pypsa-eur env die zugehörigen Pakete downgraded:

`mamba install -c conda-forge pyomo=5.6.9 pyutilib=5.8.0`
