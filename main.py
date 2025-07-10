import kagglehub

# Download latest version
path = kagglehub.dataset_download("sowmyabarla/parkinsons-augmented-handwriting-dataset")

print("Path to dataset files:", path)
