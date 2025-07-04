import kagglehub
import pandas as pd


# Download latest version
path = kagglehub.dataset_download("Cornell-University/arxiv")

print("Path to dataset files:", path)


df = pd.read_json(path +  "/arxiv-metadata-oai-snapshot.json", chunksize=1000, lines=True)

