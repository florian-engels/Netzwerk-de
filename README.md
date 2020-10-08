# Netzwerk-de

1. Zu Beginn klone dieses Repository.

2. Klone das Git Repository PyPSA-eur.

3. Installiere Anaconda oder Miniconda:
https://docs.conda.io/projects/conda/en/latest/user-guide/install/

4. Führe nun die initialize.sh Datei auf dem pypsa-eur repository aus.

5. Kopiere (und ersetze) die config.yaml Datei aus dem Netzwerk_de repo in das pypsa-eur repo.

6. Erstelle ein Beispielnetz von 4 Knoten mithilfe der make_network.sh Datei, ebenfalls auf dem pypsa-eur repository.

7. Kopiere die Csv's SolarTest, WindTest und LoadDataTest, sowie die Python Skripte "CutandPrepareData.py" und "PowerFlowOptimization.py" in den ordner ".../pypsa-eur/networks".

8. Wenn im Terminal das Environment pypsa-eur noch nicht aktiviert ist, aktiviere dies mittels "conda activate pypsa-eur". Sollte es zu Problemen kommen, muss evtl zuerst "conda init <SHELL_NAME>" ausgeführt werden. (ShellName ist hier gleich zsh?) Danach das Terminal schließen und wieder öffnen und erneut "conda activate pypsa-eur" eingeben.

9. Führe die runOptimization.sh Datei im Odner ".../pypsa-eur/networks" aus.
Im ersten Schritt werden mithilfe des Python Scripts die Daten vom Fraunhofer Institut zum Import in die richtige Form gebracht.
Im zweiten Schritt wird ein Linear optimal power flow angestoßen. Die neuen Csv's finden sich im Ordner "Solution".




## Vorsicht!

Falls es einen Fehler der Form
`assert results['Solver'][0]['Status'].key == 'ok', "Solver returned non-optimally: {}".format(results)
AttributeError: 'SolverStatus' object has no attribute 'key'`

gibt, so liegt das an einem aktuellen (09.07.20) Bug in pypsa:
https://github.com/PyPSA/PyPSA/issues/186

das kann gelöst werden, indem man in pypsa-eur env die zugehörigen Pakete downgraded:

`mamba install -c conda-forge pyomo=5.6.9 pyutilib=5.8.0`
