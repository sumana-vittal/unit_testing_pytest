to generate xml report
pytest -rA --junitxml="report1.xml"

to generate html report
first install : pip install pytest-html
then : pytest --html=htmlreport.html

parallel testing
 pip install pytest-xdist
