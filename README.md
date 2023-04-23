# Machine Learning for Healthcare Research Reproducibility Challenge
## OMSCS CSE6250 Spring 2023

### Contributors

Jessica Buzzelli, Xi Lu

### Credit
Code sourced from the [Survival-MDN](https://github.com/XintianHan/Survival-MDN) and [SODEN](https://github.com/jiaqima/SODEN) repos.

More information on the models and how to use the subrepositories can be found in the corresponding READMEs: [Survival-MDN](https://github.com/jessicabuzzelli/bdh-reproducibility-challenge/tree/main/Survival-MDN#readme), [SODEN](https://github.com/jessicabuzzelli/bdh-reproducibility-challenge/tree/main/SODEN#readme).

### Usage

Experiments from this course project were run from the Survival MDN repository with minor edits to accomodate unclear package versions. 

To reproduce our experiments (assumes Windows machine with a dedicated GPU):
1. `pip install -r requirements.txt` (primary dependencies: numpy, pandas, lifelines, torch)
2. `cd Survival-MDN`
3. `python generate_model_runner.py` to populate `run_models.ps1`
4. Run `run_models.ps1` to generate model config and run 100 experiments on each of the 3 datasets' 10 folds

Per `generate_model_runner.py`, model training and evaluation output are saved to `Survival-MDN/output/{dataset}/{split}`. 

To generate tables featured in the final report, run `helpers/parse_outputs.ipynb` and `helpers/label_distribution.ipynb`; outputs will be saved to the `helpers/` directory as `appendix_A.txt`, `results.txt` (model evaluation statistics), and `train_durations.txt` (time-to-train statistics by dataset).