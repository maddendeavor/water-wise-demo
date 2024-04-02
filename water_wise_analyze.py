import yaml
import pandas as pd
import matplotlib.pyplot as plt

yaml_file_name = "computed.yaml"
results_dict = dict()

with open(yaml_file_name) as stream:
    try:
        results_dict = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

service_df_dict = {}
for cloud in results_dict["tree"]["children"]:
    for region in results_dict["tree"]["children"][cloud]["children"]:
        service_df_dict[cloud + "_" + region] = pd.DataFrame(results_dict["tree"]["children"][cloud]["children"][region]["outputs"])

for metric in ["water", "carbon", "cpu/energy"]:
    fig, ax = plt.subplots()
    for key, service_df in service_df_dict.items():
        print(key)
        print(service_df)
        ax.plot(pd.to_datetime(service_df["timestamp"]), service_df[metric], label=key)

    ax.set_title(f"app_{metric}_consumption")
    ax.set_xlabel("time")
    ax.set_ylabel(metric)
    plt.xticks(rotation=90)
    plt.legend()
    plt.savefig(f"results_{metric.replace('/', '-')}.png", dpi=1200, bbox_inches="tight")