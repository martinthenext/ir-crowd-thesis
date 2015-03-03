for i in `seq 1 100`;
do
  echo $i >&2;
  python accuracytofile.py >> results/accuracies_1_to_5_topic_20780_est_gp_for_all_nugget_0.3.csv    
done 
