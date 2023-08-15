# FLL
![FLL-4](https://github.com/senihergordugumde/FLL/assets/85408428/a5c0368a-946f-499a-b19a-d131080e07fe)

A simple tool that i wrote with python give easiness for find latitude and longitude locations from an excel table or python list. For example this locations may like this( “İstanbul”, “İstanbul/Sefaköy”, “Sevim Sk. no: 12”, “Pera Müzesi” )


# Install

Install use pip
```
pip install -i https://test.pypi.org/simple/ fll
```


# Requirements

FLL is using Pandas, Openpyxl and Geocoder libraries.

```
pip install -r requirements.txt
```


# How to use

First of all we must create an object from FLL.

```
fll = fll.Find_Latitude_Longitude()
```
Basically we have 2 methods. Maybe you want to use your python list. So you can try this.
```
fll.findLocation(api, data, toExcel)
```

- api = "Api that taken from Google"

- data = Your data list in python

- toExcel = It's a boolean variable. Do you want an excel file? If yes try True or 1
  
----
Another situation. If you want to use data in excel file you can use this method.


```
data = fll.useExcel(excelFile, column)
```
```
fll.findLocation(api, data, toExcel)
```

#### Explain

- excelFile = "Your excel file location"
  
- column = "Column names which includes your data"


