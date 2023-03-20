num_trials = 100
seed = 1

with open("run_models.ps1", "w") as f:
    for dataset in ["support", "gbsg", "metabric"]:
        if dataset == "support":
            f.write(f"python generate_config.py --basic_model_config_file configs/support.json --num_trials {num_trials} --starting_trial 0 --random_seed 0" + "\n")
        
        else:
            f.write(f"python generate_config.py --num_trials {num_trials} --starting_trial 0 --random_seed 0" + "\n")

        for t in range(num_trials):

            for s in range(1, 11):
                train_string = f"python main.py --save_model --save_log --dataset {dataset} --path data/{dataset} --split {s} --seed {seed} --model_config_file data/hp_configs/support__{t}__model.json --train_config_file data/hp_configs/support__{t}__train.json  > C:/Users/jbuzz/repos/Survival-MDN/output/{dataset}/split{s}/model_{t}_train.txt"
                eval_string = f"python main.py --evaluate --dataset {dataset} --path data/{dataset} --split {s} --seed {seed} --model_config_file data/hp_configs/support__{t}__model.json --train_config_file data/hp_configs/support__{t}__train.json > C:/Users/jbuzz/repos/Survival-MDN/output/{dataset}/split{s}/model_{t}_eval.json"
                f.write(train_string + "\n" + f"echo 'finished dataset {dataset} model {t} split {s}'" + "\n" + eval_string + "\n")
        
        f.write(" \n \n \n \n")

