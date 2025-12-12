{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27ddb9dc-92bd-4c08-aac1-0b96d356cd8c",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "Prefect flow to orchestrate the pipeline locally.\n",
    "Stages:\n",
    "- load_data\n",
    "- eda\n",
    "- preprocess\n",
    "- train\n",
    "- evaluate\n",
    "\"\"\"\n",
    "from prefect import flow, task\n",
    "import subprocess\n",
    "\n",
    "@task\n",
    "def load_data():\n",
    "    subprocess.check_call([\"python\", \"src/data/load_data.py\"])\n",
    "    return \"data/raw/placementdata.csv\"\n",
    "\n",
    "@task\n",
    "def eda():\n",
    "    subprocess.check_call([\"python\", \"src/eda.py\"])\n",
    "    return \"reports/eda_summary.txt\"\n",
    "\n",
    "@task\n",
    "def preprocess():\n",
    "    subprocess.check_call([\"python\", \"src/preprocess.py\"])\n",
    "    return \"data/processed\"\n",
    "\n",
    "@task\n",
    "def train():\n",
    "    subprocess.check_call([\"python\", \"src/train.py\"])\n",
    "    return \"models/model.joblib\"\n",
    "\n",
    "@task\n",
    "def evaluate():\n",
    "    subprocess.check_call([\"python\", \"src/evaluate.py\"])\n",
    "    return \"reports/evidently_report.html\"\n",
    "\n",
    "@flow\n",
    "def full_pipeline():\n",
    "    raw = load_data()\n",
    "    e = eda()\n",
    "    p = preprocess()\n",
    "    m = train()\n",
    "    r = evaluate()\n",
    "    return {\"raw\": raw, \"eda\": e, \"processed\": p, \"model\": m, \"report\": r}\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    print(full_pipeline())\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
