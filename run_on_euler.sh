bsub -R "rusage[mem=8000]" -W 0:30 -n 1 -o results/output -e results/accuracies "python oneaccuracy.py"
# bsub -R "rusage[mem=16000]" -W 0:30 -n 1 -o results/accuracies -e results/errors "python oneaccuracy.py"
# bsub -R "rusage[mem=8000]" -W 4:00 -n 8 -N -B -u mdavtyan@student.ethz.ch "python experiments.py" 
