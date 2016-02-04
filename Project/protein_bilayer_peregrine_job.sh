#! /bin/bash 
#SBATCH --time 16:00:00 
#SBATCH --nodes=4 
#SBATCH --ntasks-per-node=12 
#SBATCH --job-name=VDAC1_test 
#SBATCH --output=VDAC1_test.out 
#SBATCH --mem=1000 

module load GROMACS/5.0.4-goolfc-2.7.11-avx2-hybrid 
cd $HOME/Protein_Bilayer_Sim/ 
srun cluster_run.tpr
