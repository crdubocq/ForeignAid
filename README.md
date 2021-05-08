# US Foreign Aid distribution 

### Summary

This project uses a range of visualization to explore data from US Foreign Aid.


### Input Data

The input data is **us_foreign_aid_complete.csv** from USAID Foreign Aid Explorer (FAE). It contains records from 1946 to 2020. The full database contains many columns including Countries, Regions, Development Assistance Category (DAC), Channel, Agency, Current and Constant Ammounts, Fiscal Year, among others. For the sake of this investigation, I produced a sample sixe of the dataset and only chose the columns I needed to work with. Once my scripts were complete, I used the the full dataset to produce more accurate results. 

### Aid.py

In this script I first cleaned the dataset from unwanted material and from that produce a csv file to use in later scripts. Since I was starting to work with the dataset I wanted to learn more about its contents so I sought to explore which were the Top 10 country recepients of aid, the Top 10 federal agencies deliverin aid, and the Top 10 DAC. This resulted in 3 PNG files of bar graphs portraying these results. 

### Heatmap.py

After indetifying these Top 10 categories, I wondered how these interacted with each other. For this I developemt two heatmaps: one on the relationship between Region and DAC Category, and another for Countries and DAC. 

### Time.py 

Since ientifying Afghanistan as a top recepient of Governance DAC, I wonder how much of it began since 2001, and how much of Afghanistan aid makes up the whole of US Foreign aid. For this I reduce the dataset to only records after 1980. 