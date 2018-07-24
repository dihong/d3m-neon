# [Formatting NEON data with D3M]
This project converts all data from NEON data science evaluation into D3M format.
It is necessary to [download](https://www.ecodse.org/) a copy of the data before running the scripts.
There are 4 different types of data: RSdata, Task1, Task2, and Task3.
Each type of the data needs to be run separately, following the instructions below.
The ouputs are json files specifying D3M schema of the corresponding data.
For more information about the NEON data science evaluation project, please visit [here](https://www.ecodse.org/)

## RSdata
Convert RSdata to D3M format.
```bash
cd neon/ECODSEdataset/RSdata
bash convert.sh
```

## Task1
Convert Task1 data to D3M format.
```bash
cd neon/ECODSEdataset/Task1
bash convert.sh
```

## Task2
Convert Task2 data to D3M format.
```bash
cd neon/ECODSEdataset/Task2
bash convert.sh
```

## Task3
Convert Task3 data to D3M format.
```bash
cd neon/ECODSEdataset/Task3
bash convert.sh
```
