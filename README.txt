Igor 2 is a financial data interpreter/visualization tool

users must download and place respective SEC/EDGAR data in the available python path for proper execution
https://www.sec.gov/dera/data/financial-statement-data-sets.html


#########################################################################
COPIED FROM SEC.GOV
#########################################################################


1.SUB is   identifies all the EDGAR submissions in the data set, with each row having the unique (primary) keyadsh,  a 20 character EDGAR Accession Number with dashes in positions 11 and 14.

2.TAG is a data set of all tags used in the submissions, both standard and custom.  A unique key of each row is a combination of these fields:
  1)tag – tag used by the filer
  2)version –   if a standard tag, the taxonomy of origin, otherwise equal to adsh.

3.NUM is a data set of all numeric XBRL facts presented on the primary financial statements. A   unique key of each row is a combination of the following fields:
  1)adsh-  EDGAR accession number   
  2)tag – tag used by the filer
  3)version –   if a standard tag, the  taxonomy of origin, otherwise equal to adsh.
  4)ddate -  period end date
  5)qtrs -  duration in number of quarters
  6)uom - unit of measure  
  7)coreg - coregistrant of the parent company registrant (if applicable)

4.PRE is a data set that  provides the text assigned by the filer to each line item in the primary financial statements, the order in which the line item appeared, and the tag assigned to it.  A unique key of each row is a combination of the following fields:
  1)adsh – EDGAR accession number
  2)report –   sequential number of report within the statements
  3)line –   sequential number of line within a report.
