import geocoder
import pandas as pd


class Find_Latitude_Longitude():
    def __init__(self):
        pass
    def findLocation(self,api,data,toExcel):
        latitudeLongitude = []
        latitude = []
        longitude = []
        locationName = []
        for i in data:
            g = geocoder.google(i, key=api)
            latitudeLongitude.append(g.latlng)
            print(i)
            locationName.append(i)

        x = 0
        for a in latitudeLongitude:
            if a != None:
                latitude.append(latitudeLongitude[x][0])
                longitude.append(latitudeLongitude[x][1])
                x += 1
            else:
                latitude.append(None)
                longitude.append(None)
                x += 1

        data = {"Location": locationName, "Latitude": latitude, "Longitude": longitude}
        df = pd.DataFrame(data)
        print("---------------------------------")
        print(df)


        if toExcel == True:

            outputName = input("Give file name: ")
            df.to_excel(outputName + ".xlsx")
            print("File Created!\n " + outputName + ".xlsx")


    def useExcel(self,excelFile,column):


            try:

                file = pd.read_excel(excelFile)

                df = pd.DataFrame(file)

                print(df.head())
                print("---------------------------------")

            except FileNotFoundError:
                print("File Not Found!")
            except IsADirectoryError:
                print("This is not an excel file!")
            data = []
            for i in range(len(file.index)):
                data.append(file.loc[[i], column].values[0])
                i += 1


            return data





fll = Find_Latitude_Longitude()


