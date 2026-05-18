In python, install:

"pip install duckdb pandas"

To communicate with DBBackEnd

submit your json file with the following details.

Action: getProjects or pushUpdates or LoadProgress
	For getProjects
Column: * (for all columns), or name of your CSV column from CData.csv file
Criteria Column: Your CSV Column name
Criteria: What you want your row to contain

Example for getProjects:
	"Action": "getProjects", "Column": ["Start Date", "End Date"], "Criteria Column": "Project Name", "Criteria": "Paint Doors"