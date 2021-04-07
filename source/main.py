from omegaconf import OmegaConf


def fit(params):
    print("Fitting with the following parameters:\n", OmegaConf.to_yaml(params))


def predict(params):
    print("Predicting with the following parameters:\n", OmegaConf.to_yaml(params))


def dev_run(params):
    print("Dev run with the following parameters:\n", OmegaConf.to_yaml(params))


@hydra.main(config_path="configs/", config_name="config.yaml")
def perform_tasks(params):
    os.chdir(hydra.utils.get_original_cwd())
    if "fit" in params.tasks:
        fit(params)
    if "predict" in params.tasks:
        predict(params)
    if "dev_run" in params.tasks:
        dev_run(params)


if __name__ == '__main__':
    perform_tasks()
