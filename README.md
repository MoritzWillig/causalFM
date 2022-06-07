# Can Foundation Models Talk Causality?

# Installation
The usual libs (numpy, matplotlib, ...). Also `transformers` for the OPT model.
```
conda create -n fm python=3.8
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
pip install transformers
pip install rtpt
pip install openai
pip install aleph_alpha_client
pip install wrapt
```

# Process
0. Create an openAI and aleph-alpha account and store your keys in a file under `./keys/openai` and `./keys/aleph_alpha`.
1. Generate queries. Write/modify and run: `./generate_DATASET.py`
   1. Queries are stored in the `queries/` folder. `dataset_questions.txt` contains a human readable form. `dataset_full.pkl` contains meta information about the used template and variables.
   2. Note: The order of the queries is assumed to be unchanged throughout the process.
2. Adjust `active_apis` and `datasets` variables in `./query_questions.py`. The script will query all specified datasets from all given APIs.
   1. The OPT-30B model needs ~65GB of GPU RAM ... so use the newer machines. Default download dir: `~/.cache/huggingface/`. (Loading the model into memory takes around 15 minutes on a DGX).
   2. Responses are stored under `./queries/API_DATASET/IDX.txt`.
   3. Already recorded queries are kept on rerunning the skipped.
3. Classify the answers using `add_summary.py`. Again adjust `from_apis` and `datasets` and run the script.
   0. (Not needed for non-datasets queries, like `intuitive_physics` or `causal_chains`)
   1. The script auto classifies answers starting with 'yes' or 'no'.
   2. For all other answers the intention has to be entered manually.
   3. Once all answers of a dataset are classifier a `summary.txt` is written to the dataset folder.
   4. Have a look at the bottom of the script (line 95) for explanations of the different categories.
   5. The auto classification classifies with 'y', 'n', 'uqy', 'uqn'.
   6. The fine grained labels aren't that important. All 'yes' ('y', 'ye', 'yo', ...), 'no' ('n', 'ne', ..) and 'undefined/uncertain' ('u', 'x', ...) answers will be grouped together later on.
4. Run one of the `present_*.py` scripts.
   * Results are stored under `./evaluations/`.
   * `present_base_graphs.py` - Visualizes all positive ('yes') edges grouped by API and question template.
   * `present_stability_graphs.py` - Counts the number of predicted edges when altering the question template.
   * `present_wording_stability_graphs.py` - Displays the differences in connectivity when changing variable wordings.
   * `present_common_datasets.py` - Stores queries and answers into a single json file.
