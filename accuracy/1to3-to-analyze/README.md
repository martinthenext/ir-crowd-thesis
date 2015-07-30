# Appending experimental results to the analysis file

Analysis is performed on the file `seq-1to3.filtered.tsv`, where all the experimental results from generating accuracy sequences live. To add new experimental results to this file you need to filter the errors (MATLAB seg faults, etc) out from it and append it to the orinial file.

## Example

```


$ cp seq-1to3.filtered.tsv seq-1to3.filtered.tsv.backup
$ ./../filter-to-stdout.py seq-1to3.stderr-27053.tsv >> seq-1to3.filtered.tsv

```
