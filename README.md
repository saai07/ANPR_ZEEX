<H1 align="center">ANPR</H1>


## Steps to run Code

- Clone the repository
```
https://github.com/saai07/ANPR_ZEEX
```

- Goto the cloned folder.
```
cd ANPR_ZEEX
```
- Install the dependecies
```
pip install -e '.[dev]'

```

- Setting the Directory.
```
cd ultralytics/yolo/v8/detect
```

- Download the Weights from the Google Drive
```
gdown "https://drive.google.com/uc?export=download&id=1vllvvS4jXzwPe7lA7hXjbrHCHAzcq4Zl"
```
- Download the Sample Video from the Google Drive for testing
```
gdown "https://drive.google.com/uc?export=download&id=1BOSEPsKj6hSAs5pvd88GNhlk5KPeAJce"


- Run the code with mentioned command below.

```
python predict.py model='best.pt' source='demo.mp4'
```








