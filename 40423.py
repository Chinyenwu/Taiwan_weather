import numpy as np
#import matplotlib.pyplot as plt
import csv
import math
# import matplotlib.pyplot as plt

list2010 = [];
list2011 = [];
list2012 = [];
list2013 = [];
list2014 = [];
list2015 = [];
list2016 = [];
list2017 = [];
list2018 = [];
list2019 = [];
list2020 = [];
list2021 = [];
list2022 = [];
#天氣資料
with open('1基隆市_基隆/466940-2016-03.csv' , newline = '') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows :
		list2010.append(row)

with open('2台北市_台北/466920-2016-03.csv' , newline = '') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows :
		list2011.append(row)
		
with open('3桃園市_新屋/467050-2016-03.csv' , newline = '') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows :
		list2012.append(row)

with open('4新竹市_新竹/467571-2016-03.csv' , newline = '') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows :
		list2013.append(row)

with open('5台中市_台中/467490-2016-03.csv' , newline = '') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows :
		list2014.append(row)

with open('6嘉義市_嘉義/467480-2016-03.csv' , newline = '') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows :
		list2015.append(row)
		
with open('7台南市_台南/467410-2016-03.csv' , newline = '') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows :
		list2016.append(row)
		
with open('8高雄市_高雄/467440-2016-03.csv' , newline = '') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows :
		list2017.append(row)

with open('9屏東市_恆春/467590-2016-03.csv' , newline = '') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows :
		list2018.append(row)
		
with open('10台東縣_台東/467660-2016-03.csv' , newline = '') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows :
		list2019.append(row)

with open('11花蓮縣_花蓮/466990-2016-03.csv' , newline = '') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows :
		list2020.append(row)
		
with open('12宜蘭縣_宜蘭/467080-2016-03.csv' , newline = '') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows :
		list2021.append(row)
		
with open('13南投縣_日月潭/467650-2016-03.csv' , newline = '') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows :
		list2022.append(row)
	
#這裡做氣溫計算	
rate = 0.00000000005;
b1=b2=b3=1.0;

WL2 = [[float(0.01) for i in range(9)] for j in range(6)];
WH2 = [[float(0.01) for i in range(9)] for j in range(9)];
WL3 = [[float(0.01) for i in range(6)] for j in range(9)];

errr = 50
err=err1=err2=err3=err4=err5=err6=err7=err8=err9=err10=err11=err12=err13 = 3.0;
errtm  = 0;
while errr >  1.71:
	for i in range(1,32,1):

		HL2= [float(0) for i in range(9)];
		HL22= [float(0) for i in range(9)];
		HL3= [float(0) for i in range(6)];
		ERRH2 = [float(0) for i in range(9)];
		ERRH22 = [float(0) for i in range(9)];
		ERRH3 = [float(0) for i in range(6)];	
		
		for j in range(9):
			output = b1+float(list2010[i][1])*WL2[0][j]+float(list2010[i][3])*WL2[1][j]+float(list2010[i][5])*WL2[2][j]+float(list2010[i][7])*WL2[3][j]+float(list2010[i][13])*WL2[4][j]+float(list2010[i][14])*WL2[5][j];
			HL2[j]=(1/(1+math.exp(output)));
			
		for j in range(9):
			output = b2+HL2[0]*WH2[0][j]+HL2[1]*WH2[1][j]+HL2[2]*WH2[2][j]+HL2[3]*WH2[3][j]+HL2[4]*WH2[4][j]+HL2[5]*WH2[5][j]+HL2[6]*WH2[6][j]+HL2[7]*WH2[7][j]+HL2[8]*WH2[8][j];
			HL22[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22[0]*WL3[0][j]+HL22[1]*WL3[1][j]+HL22[2]*WL3[2][j]+HL22[3]*WL3[3][j]+HL22[4]*WL3[4][j]+HL22[5]*WL3[5][j]+HL22[6]*WL3[6][j]+HL22[7]*WL3[7][j]+HL22[8]*WL3[8][j];
			HL3[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			ERRH3[j]=(HL3[j]*(1-HL3[j])*(HL3[j]-float(list2010[i][8])));				

		for j in range(9):
			ERRH22[j]=(HL22[j]*(1-HL22[j])*(WL3[j][0]*ERRH3[0]+WL3[j][1]*ERRH3[1]+WL3[j][2]*ERRH3[2]+WL3[j][3]*ERRH3[3]+WL3[j][4]*ERRH3[4]+WL3[j][5]*ERRH3[5]));
			
		for j in range(9):		
			ERRH2[j]=(HL2[j]*(1-HL2[j])*(WH2[j][0]*ERRH22[0]+WH2[j][1]*ERRH22[1]+WL3[j][2]*ERRH22[2]+WH2[j][3]*ERRH22[3]+WH2[j][4]*ERRH22[4]+WH2[j][5]*ERRH22[5]+WH2[j][6]*ERRH22[6]+WH2[j][7]*ERRH22[7]+WH2[j][8]*ERRH22[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2010[i][1]);
				elif j == 1:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2010[i][3]);
				elif j == 2:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2010[i][5]);
				elif j == 3:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2010[i][7]);
				elif j == 4:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2010[i][13]);
				elif j == 5:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2010[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2010[i][1]);
				elif j == 1:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2010[i][3]);
				elif j == 2:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2010[i][5]);
				elif j == 3:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2010[i][7]);
				elif j == 4:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2010[i][13]);
				elif j == 5:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2010[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2010[i][1]);
				elif j == 1:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2010[i][3]);
				elif j == 2:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2010[i][5]);
				elif j == 3:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2010[i][7]);
				elif j == 4:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2010[i][13]);
				elif j == 5:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2010[i][14]); 	

		for j in range(9):
			output = b1+float(list2011[i][1])*WL2[0][j]+float(list2011[i][3])*WL2[1][j]+float(list2011[i][5])*WL2[2][j]+float(list2011[i][7])*WL2[3][j]+float(list2011[i][13])*WL2[4][j]+float(list2011[i][14])*WL2[5][j];
			HL2[j]=(1/(1+math.exp(output)));
			
		for j in range(9):
			output = b2+HL2[0]*WH2[0][j]+HL2[1]*WH2[1][j]+HL2[2]*WH2[2][j]+HL2[3]*WH2[3][j]+HL2[4]*WH2[4][j]+HL2[5]*WH2[5][j]+HL2[6]*WH2[6][j]+HL2[7]*WH2[7][j]+HL2[8]*WH2[8][j];
			HL22[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22[0]*WL3[0][j]+HL22[1]*WL3[1][j]+HL22[2]*WL3[2][j]+HL22[3]*WL3[3][j]+HL22[4]*WL3[4][j]+HL22[5]*WL3[5][j]+HL22[6]*WL3[6][j]+HL22[7]*WL3[7][j]+HL22[8]*WL3[8][j];
			HL3[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			ERRH3[j]=(HL3[j]*(1-HL3[j])*(HL3[j]-float(list2011[i][8])));				


		for j in range(9):
			ERRH22[j]=(HL22[j]*(1-HL22[j])*(WL3[j][0]*ERRH3[0]+WL3[j][1]*ERRH3[1]+WL3[j][2]*ERRH3[2]+WL3[j][3]*ERRH3[3]+WL3[j][4]*ERRH3[4]+WL3[j][5]*ERRH3[5]));
				
		for j in range(9):
			ERRH2[j]=(HL2[j]*(1-HL2[j])*(WH2[j][0]*ERRH22[0]+WH2[j][1]*ERRH22[1]+WL3[j][2]*ERRH22[2]+WH2[j][3]*ERRH22[3]+WH2[j][4]*ERRH22[4]+WH2[j][5]*ERRH22[5]+WH2[j][6]*ERRH22[6]+WH2[j][7]*ERRH22[7]+WH2[j][8]*ERRH22[8]));	
			
		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2011[i][1]);
				elif j == 1:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2011[i][3]);
				elif j == 2:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2011[i][5]);
				elif j == 3:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2011[i][7]);
				elif j == 4:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2011[i][13]);
				elif j == 5:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2011[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2011[i][1]);
				elif j == 1:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2011[i][3]);
				elif j == 2:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2011[i][5]);
				elif j == 3:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2011[i][7]);
				elif j == 4:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2011[i][13]);
				elif j == 5:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2011[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2011[i][1]);
				elif j == 1:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2011[i][3]);
				elif j == 2:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2011[i][5]);
				elif j == 3:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2011[i][7]);
				elif j == 4:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2011[i][13]);
				elif j == 5:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2011[i][14]);		

		for j in range(9):
			output = b1+float(list2012[i][1])*WL2[0][j]+float(list2012[i][3])*WL2[1][j]+float(list2012[i][5])*WL2[2][j]+float(list2012[i][7])*WL2[3][j]+float(list2012[i][13])*WL2[4][j]+float(list2012[i][14])*WL2[5][j];
			HL2[j]=(1/(1+math.exp(output)));
			
		for j in range(9):
			output = b2+HL2[0]*WH2[0][j]+HL2[1]*WH2[1][j]+HL2[2]*WH2[2][j]+HL2[3]*WH2[3][j]+HL2[4]*WH2[4][j]+HL2[5]*WH2[5][j]+HL2[6]*WH2[6][j]+HL2[7]*WH2[7][j]+HL2[8]*WH2[8][j];
			HL22[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22[0]*WL3[0][j]+HL22[1]*WL3[1][j]+HL22[2]*WL3[2][j]+HL22[3]*WL3[3][j]+HL22[4]*WL3[4][j]+HL22[5]*WL3[5][j]+HL22[6]*WL3[6][j]+HL22[7]*WL3[7][j]+HL22[8]*WL3[8][j];
			HL3[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			ERRH3[j]=(HL3[j]*(1-HL3[j])*(HL3[j]-float(list2012[i][8])));				


		for j in range(9):
			ERRH22[j]=(HL22[j]*(1-HL22[j])*(WL3[j][0]*ERRH3[0]+WL3[j][1]*ERRH3[1]+WL3[j][2]*ERRH3[2]+WL3[j][3]*ERRH3[3]+WL3[j][4]*ERRH3[4]+WL3[j][5]*ERRH3[5]));
				
		for j in range(9):
			ERRH2[j]=(HL2[j]*(1-HL2[j])*(WH2[j][0]*ERRH22[0]+WH2[j][1]*ERRH22[1]+WL3[j][2]*ERRH22[2]+WH2[j][3]*ERRH22[3]+WH2[j][4]*ERRH22[4]+WH2[j][5]*ERRH22[5]+WH2[j][6]*ERRH22[6]+WH2[j][7]*ERRH22[7]+WH2[j][8]*ERRH22[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2012[i][1]);
				elif j == 1:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2012[i][3]);
				elif j == 2:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2012[i][5]);
				elif j == 3:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2012[i][7]);
				elif j == 4:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2012[i][13]);
				elif j == 5:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2012[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2012[i][1]);
				elif j == 1:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2012[i][3]);
				elif j == 2:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2012[i][5]);
				elif j == 3:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2012[i][7]);
				elif j == 4:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2012[i][13]);
				elif j == 5:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2012[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2012[i][1]);
				elif j == 1:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2012[i][3]);
				elif j == 2:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2012[i][5]);
				elif j == 3:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2012[i][7]);
				elif j == 4:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2012[i][13]);
				elif j == 5:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2012[i][14]);		
					
		for j in range(9):
			output = b1+float(list2013[i][1])*WL2[0][j]+float(list2013[i][3])*WL2[1][j]+float(list2013[i][5])*WL2[2][j]+float(list2013[i][7])*WL2[3][j]+float(list2013[i][13])*WL2[4][j]+float(list2013[i][14])*WL2[5][j];
			HL2[j]=(1/(1+math.exp(output)));
			
		for j in range(9):
			output = b2+HL2[0]*WH2[0][j]+HL2[1]*WH2[1][j]+HL2[2]*WH2[2][j]+HL2[3]*WH2[3][j]+HL2[4]*WH2[4][j]+HL2[5]*WH2[5][j]+HL2[6]*WH2[6][j]+HL2[7]*WH2[7][j]+HL2[8]*WH2[8][j];
			HL22[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22[0]*WL3[0][j]+HL22[1]*WL3[1][j]+HL22[2]*WL3[2][j]+HL22[3]*WL3[3][j]+HL22[4]*WL3[4][j]+HL22[5]*WL3[5][j]+HL22[6]*WL3[6][j]+HL22[7]*WL3[7][j]+HL22[8]*WL3[8][j];
			HL3[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			ERRH3[j]=(HL3[j]*(1-HL3[j])*(HL3[j]-float(list2013[i][8])));				
	

		for j in range(9):
			ERRH22[j]=(HL22[j]*(1-HL22[j])*(WL3[j][0]*ERRH3[0]+WL3[j][1]*ERRH3[1]+WL3[j][2]*ERRH3[2]+WL3[j][3]*ERRH3[3]+WL3[j][4]*ERRH3[4]+WL3[j][5]*ERRH3[5]));
				
		for j in range(9):
			ERRH2[j]=(HL2[j]*(1-HL2[j])*(WH2[j][0]*ERRH22[0]+WH2[j][1]*ERRH22[1]+WL3[j][2]*ERRH22[2]+WH2[j][3]*ERRH22[3]+WH2[j][4]*ERRH22[4]+WH2[j][5]*ERRH22[5]+WH2[j][6]*ERRH22[6]+WH2[j][7]*ERRH22[7]+WH2[j][8]*ERRH22[8]));						

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2013[i][1]);
				elif j == 1:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2013[i][3]);
				elif j == 2:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2013[i][5]);
				elif j == 3:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2013[i][7]);
				elif j == 4:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2013[i][13]);
				elif j == 5:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2013[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2013[i][1]);
				elif j == 1:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2013[i][3]);
				elif j == 2:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2013[i][5]);
				elif j == 3:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2013[i][7]);
				elif j == 4:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2013[i][13]);
				elif j == 5:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2013[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2013[i][1]);
				elif j == 1:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2013[i][3]);
				elif j == 2:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2013[i][5]);
				elif j == 3:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2013[i][7]);
				elif j == 4:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2013[i][13]);
				elif j == 5:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2013[i][14]);	
					
		for j in range(9):
			output = b1+float(list2014[i][1])*WL2[0][j]+float(list2014[i][3])*WL2[1][j]+float(list2014[i][5])*WL2[2][j]+float(list2014[i][7])*WL2[3][j]+float(list2014[i][13])*WL2[4][j]+float(list2014[i][14])*WL2[5][j];
			HL2[j]=(1/(1+math.exp(output)));
			
		for j in range(9):
			output = b2+HL2[0]*WH2[0][j]+HL2[1]*WH2[1][j]+HL2[2]*WH2[2][j]+HL2[3]*WH2[3][j]+HL2[4]*WH2[4][j]+HL2[5]*WH2[5][j]+HL2[6]*WH2[6][j]+HL2[7]*WH2[7][j]+HL2[8]*WH2[8][j];
			HL22[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22[0]*WL3[0][j]+HL22[1]*WL3[1][j]+HL22[2]*WL3[2][j]+HL22[3]*WL3[3][j]+HL22[4]*WL3[4][j]+HL22[5]*WL3[5][j]+HL22[6]*WL3[6][j]+HL22[7]*WL3[7][j]+HL22[8]*WL3[8][j];
			HL3[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			ERRH3[j]=(HL3[j]*(1-HL3[j])*(HL3[j]-float(list2014[i][8])));				
	

		for j in range(9):
			ERRH22[j]=(HL22[j]*(1-HL22[j])*(WL3[j][0]*ERRH3[0]+WL3[j][1]*ERRH3[1]+WL3[j][2]*ERRH3[2]+WL3[j][3]*ERRH3[3]+WL3[j][4]*ERRH3[4]+WL3[j][5]*ERRH3[5]));
				
		for j in range(9):
			ERRH2[j]=(HL2[j]*(1-HL2[j])*(WH2[j][0]*ERRH22[0]+WH2[j][1]*ERRH22[1]+WL3[j][2]*ERRH22[2]+WH2[j][3]*ERRH22[3]+WH2[j][4]*ERRH22[4]+WH2[j][5]*ERRH22[5]+WH2[j][6]*ERRH22[6]+WH2[j][7]*ERRH22[7]+WH2[j][8]*ERRH22[8]));				

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2014[i][1]);
				elif j == 1:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2014[i][3]);
				elif j == 2:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2014[i][5]);
				elif j == 3:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2014[i][7]);
				elif j == 4:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2014[i][13]);
				elif j == 5:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2014[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2014[i][1]);
				elif j == 1:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2014[i][3]);
				elif j == 2:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2014[i][5]);
				elif j == 3:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2014[i][7]);
				elif j == 4:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2014[i][13]);
				elif j == 5:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2014[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2014[i][1]);
				elif j == 1:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2014[i][3]);
				elif j == 2:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2014[i][5]);
				elif j == 3:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2014[i][7]);
				elif j == 4:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2014[i][13]);
				elif j == 5:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2014[i][14]);
					
		for j in range(9):
			output = b1+float(list2015[i][1])*WL2[0][j]+float(list2015[i][3])*WL2[1][j]+float(list2015[i][5])*WL2[2][j]+float(list2015[i][7])*WL2[3][j]+float(list2015[i][13])*WL2[4][j]+float(list2015[i][14])*WL2[5][j];
			HL2[j]=(1/(1+math.exp(output)));
			
		for j in range(9):
			output = b2+HL2[0]*WH2[0][j]+HL2[1]*WH2[1][j]+HL2[2]*WH2[2][j]+HL2[3]*WH2[3][j]+HL2[4]*WH2[4][j]+HL2[5]*WH2[5][j]+HL2[6]*WH2[6][j]+HL2[7]*WH2[7][j]+HL2[8]*WH2[8][j];
			HL22[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22[0]*WL3[0][j]+HL22[1]*WL3[1][j]+HL22[2]*WL3[2][j]+HL22[3]*WL3[3][j]+HL22[4]*WL3[4][j]+HL22[5]*WL3[5][j]+HL22[6]*WL3[6][j]+HL22[7]*WL3[7][j]+HL22[8]*WL3[8][j];
			HL3[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			ERRH3[j]=(HL3[j]*(1-HL3[j])*(HL3[j]-float(list2015[i][8])));				
	

		for j in range(9):
			ERRH22[j]=(HL22[j]*(1-HL22[j])*(WL3[j][0]*ERRH3[0]+WL3[j][1]*ERRH3[1]+WL3[j][2]*ERRH3[2]+WL3[j][3]*ERRH3[3]+WL3[j][4]*ERRH3[4]+WL3[j][5]*ERRH3[5]));
				
		for j in range(9):
			ERRH2[j]=(HL2[j]*(1-HL2[j])*(WH2[j][0]*ERRH22[0]+WH2[j][1]*ERRH22[1]+WL3[j][2]*ERRH22[2]+WH2[j][3]*ERRH22[3]+WH2[j][4]*ERRH22[4]+WH2[j][5]*ERRH22[5]+WH2[j][6]*ERRH22[6]+WH2[j][7]*ERRH22[7]+WH2[j][8]*ERRH22[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2015[i][1]);
				elif j == 1:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2015[i][3]);
				elif j == 2:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2015[i][5]);
				elif j == 3:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2015[i][7]);
				elif j == 4:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2015[i][13]);
				elif j == 5:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2015[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2015[i][1]);
				elif j == 1:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2015[i][3]);
				elif j == 2:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2015[i][5]);
				elif j == 3:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2015[i][7]);
				elif j == 4:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2015[i][13]);
				elif j == 5:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2015[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2015[i][1]);
				elif j == 1:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2015[i][3]);
				elif j == 2:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2015[i][5]);
				elif j == 3:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2015[i][7]);
				elif j == 4:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2015[i][13]);
				elif j == 5:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2015[i][14]);
					
		for j in range(9):
			output = b1+float(list2016[i][1])*WL2[0][j]+float(list2016[i][3])*WL2[1][j]+float(list2016[i][5])*WL2[2][j]+float(list2016[i][7])*WL2[3][j]+float(list2016[i][13])*WL2[4][j]+float(list2016[i][14])*WL2[5][j];
			HL2[j]=(1/(1+math.exp(output)));
			
		for j in range(9):
			output = b2+HL2[0]*WH2[0][j]+HL2[1]*WH2[1][j]+HL2[2]*WH2[2][j]+HL2[3]*WH2[3][j]+HL2[4]*WH2[4][j]+HL2[5]*WH2[5][j]+HL2[6]*WH2[6][j]+HL2[7]*WH2[7][j]+HL2[8]*WH2[8][j];
			HL22[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22[0]*WL3[0][j]+HL22[1]*WL3[1][j]+HL22[2]*WL3[2][j]+HL22[3]*WL3[3][j]+HL22[4]*WL3[4][j]+HL22[5]*WL3[5][j]+HL22[6]*WL3[6][j]+HL22[7]*WL3[7][j]+HL22[8]*WL3[8][j];
			HL3[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			ERRH3[j]=(HL3[j]*(1-HL3[j])*(HL3[j]-float(list2016[i][8])));				
	

		for j in range(9):
			ERRH22[j]=(HL22[j]*(1-HL22[j])*(WL3[j][0]*ERRH3[0]+WL3[j][1]*ERRH3[1]+WL3[j][2]*ERRH3[2]+WL3[j][3]*ERRH3[3]+WL3[j][4]*ERRH3[4]+WL3[j][5]*ERRH3[5]));
				
		for j in range(9):
			ERRH2[j]=(HL2[j]*(1-HL2[j])*(WH2[j][0]*ERRH22[0]+WH2[j][1]*ERRH22[1]+WL3[j][2]*ERRH22[2]+WH2[j][3]*ERRH22[3]+WH2[j][4]*ERRH22[4]+WH2[j][5]*ERRH22[5]+WH2[j][6]*ERRH22[6]+WH2[j][7]*ERRH22[7]+WH2[j][8]*ERRH22[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2016[i][1]);
				elif j == 1:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2016[i][3]);
				elif j == 2:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2016[i][5]);
				elif j == 3:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2016[i][7]);
				elif j == 4:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2016[i][13]);
				elif j == 5:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2016[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2016[i][1]);
				elif j == 1:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2016[i][3]);
				elif j == 2:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2016[i][5]);
				elif j == 3:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2016[i][7]);
				elif j == 4:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2016[i][13]);
				elif j == 5:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2016[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2016[i][1]);
				elif j == 1:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2016[i][3]);
				elif j == 2:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2016[i][5]);
				elif j == 3:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2016[i][7]);
				elif j == 4:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2016[i][13]);
				elif j == 5:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2016[i][14]);
					
		for j in range(9):
			output = b1+float(list2017[i][1])*WL2[0][j]+float(list2017[i][3])*WL2[1][j]+float(list2017[i][5])*WL2[2][j]+float(list2017[i][7])*WL2[3][j]+float(list2017[i][13])*WL2[4][j]+float(list2017[i][14])*WL2[5][j];
			HL2[j]=(1/(1+math.exp(output)));
			
		for j in range(9):
			output = b2+HL2[0]*WH2[0][j]+HL2[1]*WH2[1][j]+HL2[2]*WH2[2][j]+HL2[3]*WH2[3][j]+HL2[4]*WH2[4][j]+HL2[5]*WH2[5][j]+HL2[6]*WH2[6][j]+HL2[7]*WH2[7][j]+HL2[8]*WH2[8][j];
			HL22[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22[0]*WL3[0][j]+HL22[1]*WL3[1][j]+HL22[2]*WL3[2][j]+HL22[3]*WL3[3][j]+HL22[4]*WL3[4][j]+HL22[5]*WL3[5][j]+HL22[6]*WL3[6][j]+HL22[7]*WL3[7][j]+HL22[8]*WL3[8][j];
			HL3[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			ERRH3[j]=(HL3[j]*(1-HL3[j])*(HL3[j]-float(list2017[i][8])));				


		for j in range(9):
			ERRH22[j]=(HL22[j]*(1-HL22[j])*(WL3[j][0]*ERRH3[0]+WL3[j][1]*ERRH3[1]+WL3[j][2]*ERRH3[2]+WL3[j][3]*ERRH3[3]+WL3[j][4]*ERRH3[4]+WL3[j][5]*ERRH3[5]));
				
		for j in range(9):
			ERRH2[j]=(HL2[j]*(1-HL2[j])*(WH2[j][0]*ERRH22[0]+WH2[j][1]*ERRH22[1]+WL3[j][2]*ERRH22[2]+WH2[j][3]*ERRH22[3]+WH2[j][4]*ERRH22[4]+WH2[j][5]*ERRH22[5]+WH2[j][6]*ERRH22[6]+WH2[j][7]*ERRH22[7]+WH2[j][8]*ERRH22[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2017[i][1]);
				elif j == 1:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2017[i][3]);
				elif j == 2:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2017[i][5]);
				elif j == 3:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2017[i][7]);
				elif j == 4:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2017[i][13]);
				elif j == 5:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2017[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2017[i][1]);
				elif j == 1:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2017[i][3]);
				elif j == 2:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2017[i][5]);
				elif j == 3:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2017[i][7]);
				elif j == 4:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2017[i][13]);
				elif j == 5:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2017[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2017[i][1]);
				elif j == 1:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2017[i][3]);
				elif j == 2:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2017[i][5]);
				elif j == 3:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2017[i][7]);
				elif j == 4:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2017[i][13]);
				elif j == 5:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2017[i][14]);
					
		for j in range(9):
			output = b1+float(list2018[i][1])*WL2[0][j]+float(list2018[i][3])*WL2[1][j]+float(list2018[i][5])*WL2[2][j]+float(list2018[i][7])*WL2[3][j]+float(list2018[i][13])*WL2[4][j]+float(list2018[i][14])*WL2[5][j];
			HL2[j]=(1/(1+math.exp(output)));
			
		for j in range(9):
			output = b2+HL2[0]*WH2[0][j]+HL2[1]*WH2[1][j]+HL2[2]*WH2[2][j]+HL2[3]*WH2[3][j]+HL2[4]*WH2[4][j]+HL2[5]*WH2[5][j]+HL2[6]*WH2[6][j]+HL2[7]*WH2[7][j]+HL2[8]*WH2[8][j];
			HL22[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22[0]*WL3[0][j]+HL22[1]*WL3[1][j]+HL22[2]*WL3[2][j]+HL22[3]*WL3[3][j]+HL22[4]*WL3[4][j]+HL22[5]*WL3[5][j]+HL22[6]*WL3[6][j]+HL22[7]*WL3[7][j]+HL22[8]*WL3[8][j];
			HL3[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			ERRH3[j]=(HL3[j]*(1-HL3[j])*(HL3[j]-float(list2018[i][8])));				
	

		for j in range(9):
			ERRH22[j]=(HL22[j]*(1-HL22[j])*(WL3[j][0]*ERRH3[0]+WL3[j][1]*ERRH3[1]+WL3[j][2]*ERRH3[2]+WL3[j][3]*ERRH3[3]+WL3[j][4]*ERRH3[4]+WL3[j][5]*ERRH3[5]));
				
		for j in range(9):
			ERRH2[j]=(HL2[j]*(1-HL2[j])*(WH2[j][0]*ERRH22[0]+WH2[j][1]*ERRH22[1]+WL3[j][2]*ERRH22[2]+WH2[j][3]*ERRH22[3]+WH2[j][4]*ERRH22[4]+WH2[j][5]*ERRH22[5]+WH2[j][6]*ERRH22[6]+WH2[j][7]*ERRH22[7]+WH2[j][8]*ERRH22[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2018[i][1]);
				elif j == 1:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2018[i][3]);
				elif j == 2:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2018[i][5]);
				elif j == 3:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2018[i][7]);
				elif j == 4:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2018[i][13]);
				elif j == 5:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2018[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2018[i][1]);
				elif j == 1:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2018[i][3]);
				elif j == 2:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2018[i][5]);
				elif j == 3:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2018[i][7]);
				elif j == 4:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2018[i][13]);
				elif j == 5:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2018[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2018[i][1]);
				elif j == 1:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2018[i][3]);
				elif j == 2:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2018[i][5]);
				elif j == 3:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2018[i][7]);
				elif j == 4:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2018[i][13]);
				elif j == 5:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2018[i][14]);
					
		for j in range(9):
			output = b1+float(list2019[i][1])*WL2[0][j]+float(list2019[i][3])*WL2[1][j]+float(list2019[i][5])*WL2[2][j]+float(list2019[i][7])*WL2[3][j]+float(list2019[i][13])*WL2[4][j]+float(list2019[i][14])*WL2[5][j];
			HL2[j]=(1/(1+math.exp(output)));
			
		for j in range(9):
			output = b2+HL2[0]*WH2[0][j]+HL2[1]*WH2[1][j]+HL2[2]*WH2[2][j]+HL2[3]*WH2[3][j]+HL2[4]*WH2[4][j]+HL2[5]*WH2[5][j]+HL2[6]*WH2[6][j]+HL2[7]*WH2[7][j]+HL2[8]*WH2[8][j];
			HL22[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22[0]*WL3[0][j]+HL22[1]*WL3[1][j]+HL22[2]*WL3[2][j]+HL22[3]*WL3[3][j]+HL22[4]*WL3[4][j]+HL22[5]*WL3[5][j]+HL22[6]*WL3[6][j]+HL22[7]*WL3[7][j]+HL22[8]*WL3[8][j];
			HL3[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			ERRH3[j]=(HL3[j]*(1-HL3[j])*(HL3[j]-float(list2019[i][8])));				


		for j in range(9):
			ERRH22[j]=(HL22[j]*(1-HL22[j])*(WL3[j][0]*ERRH3[0]+WL3[j][1]*ERRH3[1]+WL3[j][2]*ERRH3[2]+WL3[j][3]*ERRH3[3]+WL3[j][4]*ERRH3[4]+WL3[j][5]*ERRH3[5]));
				
		for j in range(9):
			ERRH2[j]=(HL2[j]*(1-HL2[j])*(WH2[j][0]*ERRH22[0]+WH2[j][1]*ERRH22[1]+WL3[j][2]*ERRH22[2]+WH2[j][3]*ERRH22[3]+WH2[j][4]*ERRH22[4]+WH2[j][5]*ERRH22[5]+WH2[j][6]*ERRH22[6]+WH2[j][7]*ERRH22[7]+WH2[j][8]*ERRH22[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2019[i][1]);
				elif j == 1:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2019[i][3]);
				elif j == 2:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2019[i][5]);
				elif j == 3:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2019[i][7]);
				elif j == 4:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2019[i][13]);
				elif j == 5:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2019[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2019[i][1]);
				elif j == 1:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2019[i][3]);
				elif j == 2:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2019[i][5]);
				elif j == 3:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2019[i][7]);
				elif j == 4:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2019[i][13]);
				elif j == 5:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2019[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2019[i][1]);
				elif j == 1:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2019[i][3]);
				elif j == 2:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2019[i][5]);
				elif j == 3:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2019[i][7]);
				elif j == 4:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2019[i][13]);
				elif j == 5:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2019[i][14]);
				
		for j in range(9):
			output = b1+float(list2020[i][1])*WL2[0][j]+float(list2020[i][3])*WL2[1][j]+float(list2020[i][5])*WL2[2][j]+float(list2020[i][7])*WL2[3][j]+float(list2020[i][13])*WL2[4][j]+float(list2020[i][14])*WL2[5][j];
			HL2[j]=(1/(1+math.exp(output)));
			
		for j in range(9):
			output = b2+HL2[0]*WH2[0][j]+HL2[1]*WH2[1][j]+HL2[2]*WH2[2][j]+HL2[3]*WH2[3][j]+HL2[4]*WH2[4][j]+HL2[5]*WH2[5][j]+HL2[6]*WH2[6][j]+HL2[7]*WH2[7][j]+HL2[8]*WH2[8][j];
			HL22[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22[0]*WL3[0][j]+HL22[1]*WL3[1][j]+HL22[2]*WL3[2][j]+HL22[3]*WL3[3][j]+HL22[4]*WL3[4][j]+HL22[5]*WL3[5][j]+HL22[6]*WL3[6][j]+HL22[7]*WL3[7][j]+HL22[8]*WL3[8][j];
			HL3[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			ERRH3[j]=(HL3[j]*(1-HL3[j])*(HL3[j]-float(list2020[i][8])));				
	

		for j in range(9):
			ERRH22[j]=(HL22[j]*(1-HL22[j])*(WL3[j][0]*ERRH3[0]+WL3[j][1]*ERRH3[1]+WL3[j][2]*ERRH3[2]+WL3[j][3]*ERRH3[3]+WL3[j][4]*ERRH3[4]+WL3[j][5]*ERRH3[5]));
				
		for j in range(9):
			ERRH2[j]=(HL2[j]*(1-HL2[j])*(WH2[j][0]*ERRH22[0]+WH2[j][1]*ERRH22[1]+WL3[j][2]*ERRH22[2]+WH2[j][3]*ERRH22[3]+WH2[j][4]*ERRH22[4]+WH2[j][5]*ERRH22[5]+WH2[j][6]*ERRH22[6]+WH2[j][7]*ERRH22[7]+WH2[j][8]*ERRH22[8]));				

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2020[i][1]);
				elif j == 1:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2020[i][3]);
				elif j == 2:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2020[i][5]);
				elif j == 3:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2020[i][7]);
				elif j == 4:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2020[i][13]);
				elif j == 5:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2020[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2020[i][1]);
				elif j == 1:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2020[i][3]);
				elif j == 2:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2020[i][5]);
				elif j == 3:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2020[i][7]);
				elif j == 4:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2020[i][13]);
				elif j == 5:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2020[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2020[i][1]);
				elif j == 1:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2020[i][3]);
				elif j == 2:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2020[i][5]);
				elif j == 3:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2020[i][7]);
				elif j == 4:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2020[i][13]);
				elif j == 5:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2020[i][14]);

		for j in range(9):
			output = b1+float(list2021[i][1])*WL2[0][j]+float(list2021[i][3])*WL2[1][j]+float(list2021[i][5])*WL2[2][j]+float(list2021[i][7])*WL2[3][j]+float(list2021[i][13])*WL2[4][j]+float(list2021[i][14])*WL2[5][j];
			HL2[j]=(1/(1+math.exp(output)));
			
		for j in range(9):
			output = b2+HL2[0]*WH2[0][j]+HL2[1]*WH2[1][j]+HL2[2]*WH2[2][j]+HL2[3]*WH2[3][j]+HL2[4]*WH2[4][j]+HL2[5]*WH2[5][j]+HL2[6]*WH2[6][j]+HL2[7]*WH2[7][j]+HL2[8]*WH2[8][j];
			HL22[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22[0]*WL3[0][j]+HL22[1]*WL3[1][j]+HL22[2]*WL3[2][j]+HL22[3]*WL3[3][j]+HL22[4]*WL3[4][j]+HL22[5]*WL3[5][j]+HL22[6]*WL3[6][j]+HL22[7]*WL3[7][j]+HL22[8]*WL3[8][j];
			HL3[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			ERRH3[j]=(HL3[j]*(1-HL3[j])*(HL3[j]-float(list2021[i][8])));				
	

		for j in range(9):
			ERRH22[j]=(HL22[j]*(1-HL22[j])*(WL3[j][0]*ERRH3[0]+WL3[j][1]*ERRH3[1]+WL3[j][2]*ERRH3[2]+WL3[j][3]*ERRH3[3]+WL3[j][4]*ERRH3[4]+WL3[j][5]*ERRH3[5]));
				
		for j in range(9):
			ERRH2[j]=(HL2[j]*(1-HL2[j])*(WH2[j][0]*ERRH22[0]+WH2[j][1]*ERRH22[1]+WL3[j][2]*ERRH22[2]+WH2[j][3]*ERRH22[3]+WH2[j][4]*ERRH22[4]+WH2[j][5]*ERRH22[5]+WH2[j][6]*ERRH22[6]+WH2[j][7]*ERRH22[7]+WH2[j][8]*ERRH22[8]));			

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2021[i][1]);
				elif j == 1:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2021[i][3]);
				elif j == 2:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2021[i][5]);
				elif j == 3:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2021[i][7]);
				elif j == 4:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2021[i][13]);
				elif j == 5:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2021[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2021[i][1]);
				elif j == 1:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2021[i][3]);
				elif j == 2:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2021[i][5]);
				elif j == 3:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2021[i][7]);
				elif j == 4:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2021[i][13]);
				elif j == 5:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2021[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2021[i][1]);
				elif j == 1:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2021[i][3]);
				elif j == 2:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2021[i][5]);
				elif j == 3:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2021[i][7]);
				elif j == 4:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2021[i][13]);
				elif j == 5:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2021[i][14]);
					
		for j in range(9):
			output = b1+float(list2022[i][1])*WL2[0][j]+float(list2022[i][3])*WL2[1][j]+float(list2022[i][5])*WL2[2][j]+float(list2022[i][7])*WL2[3][j]+float(list2022[i][13])*WL2[4][j]+float(list2022[i][14])*WL2[5][j];
			HL2[j]=(1/(1+math.exp(output)));
			
		for j in range(9):
			output = b2+HL2[0]*WH2[0][j]+HL2[1]*WH2[1][j]+HL2[2]*WH2[2][j]+HL2[3]*WH2[3][j]+HL2[4]*WH2[4][j]+HL2[5]*WH2[5][j]+HL2[6]*WH2[6][j]+HL2[7]*WH2[7][j]+HL2[8]*WH2[8][j];
			HL22[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22[0]*WL3[0][j]+HL22[1]*WL3[1][j]+HL22[2]*WL3[2][j]+HL22[3]*WL3[3][j]+HL22[4]*WL3[4][j]+HL22[5]*WL3[5][j]+HL22[6]*WL3[6][j]+HL22[7]*WL3[7][j]+HL22[8]*WL3[8][j];
			HL3[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			ERRH3[j]=(HL3[j]*(1-HL3[j])*(HL3[j]-float(list2022[i][8])));				


		for j in range(9):
			ERRH22[j]=(HL22[j]*(1-HL22[j])*(WL3[j][0]*ERRH3[0]+WL3[j][1]*ERRH3[1]+WL3[j][2]*ERRH3[2]+WL3[j][3]*ERRH3[3]+WL3[j][4]*ERRH3[4]+WL3[j][5]*ERRH3[5]));
				
		for j in range(9):
			ERRH2[j]=(HL2[j]*(1-HL2[j])*(WH2[j][0]*ERRH22[0]+WH2[j][1]*ERRH22[1]+WL3[j][2]*ERRH22[2]+WH2[j][3]*ERRH22[3]+WH2[j][4]*ERRH22[4]+WH2[j][5]*ERRH22[5]+WH2[j][6]*ERRH22[6]+WH2[j][7]*ERRH22[7]+WH2[j][8]*ERRH22[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2022[i][1]);
				elif j == 1:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2022[i][3]);
				elif j == 2:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2022[i][5]);
				elif j == 3:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2022[i][7]);
				elif j == 4:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2022[i][13]);
				elif j == 5:
					WL2[j][k]=WL2[j][k]+rate*ERRH2[k]*float(list2022[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2022[i][1]);
				elif j == 1:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2022[i][3]);
				elif j == 2:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2022[i][5]);
				elif j == 3:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2022[i][7]);
				elif j == 4:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2022[i][13]);
				elif j == 5:
					WH2[j][k]=WH2[j][k]+rate*ERRH22[k]*float(list2022[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2022[i][1]);
				elif j == 1:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2022[i][3]);
				elif j == 2:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2022[i][5]);
				elif j == 3:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2022[i][7]);
				elif j == 4:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2022[i][13]);
				elif j == 5:
					WL3[j][k]=WL3[j][k]+rate*ERRH3[k]*float(list2022[i][14]);
					
	err=err1=err2=err3=err4=err5=err6=err7=err8=err9=err10=err11=err12=err13 = 0.0;
	
	for l in range(1,31,1):
		err1 = err1 + (b1+float(list2010[l][1])*WL3[0][0]+float(list2010[l][3])*WL3[1][0]+float(list2010[l][5])*WL3[2][0]+float(list2010[l][7])*WL3[3][0]+float(list2010[l][13])*WL3[4][0]+float(list2010[l][14])*WL3[5][0])-float(list2010[l][8]);
	#print("err of max temperature in 基隆 is %.4f"%(err1/31));
	for l in range(1,32,1):
		err2 = err2 + (b1+float(list2011[l][1])*WL3[0][0]+float(list2011[l][3])*WL3[1][0]+float(list2011[l][5])*WL3[2][0]+float(list2011[l][7])*WL3[3][0]+float(list2011[l][13])*WL3[4][0]+float(list2011[l][14])*WL3[5][0])-float(list2011[l][8]);
	#print("err of max temperature in 台北 is %.4f"%(err2/31));
	for l in range(1,32,1):
		err3 = err3 + (b1+float(list2012[l][1])*WL3[0][0]+float(list2012[l][3])*WL3[1][0]+float(list2012[l][5])*WL3[2][0]+float(list2012[l][7])*WL3[3][0]+float(list2012[l][13])*WL3[4][0]+float(list2012[l][14])*WL3[5][0])-float(list2012[l][8]);
	#print("err of max temperature in 桃園 is %.4f"%(err3/31));
	for l in range(1,32,1):
		err4 = err4 + (b1+float(list2013[l][1])*WL3[0][0]+float(list2013[l][3])*WL3[1][0]+float(list2013[l][5])*WL3[2][0]+float(list2013[l][7])*WL3[3][0]+float(list2013[l][13])*WL3[4][0]+float(list2013[l][14])*WL3[5][0])-float(list2013[l][8]);
	#print("err of max temperature in 新竹 is %.4f"%(err4/31));	
	for l in range(1,32,1):
		err5 = err5 + (b1+float(list2015[l][1])*WL3[0][0]+float(list2015[l][3])*WL3[1][0]+float(list2015[l][5])*WL3[2][0]+float(list2014[l][7])*WL3[3][0]+float(list2014[l][13])*WL3[4][0]+float(list2014[l][14])*WL3[5][0])-float(list2014[l][8]);
	#print("err of max temperature in 台中 is %.4f"%(err5/31));
	for l in range(1,32,1):
		err6 = err6 + (b1+float(list2015[l][1])*WL3[0][0]+float(list2015[l][3])*WL3[1][0]+float(list2015[l][5])*WL3[2][0]+float(list2015[l][7])*WL3[3][0]+float(list2015[l][13])*WL3[4][0]+float(list2015[l][14])*WL3[5][0])-float(list2015[l][8]);
	#print("err of max temperature in 嘉義 is %.4f"%(err6/31));	
	for l in range(1,32,1):
		err7 = err7 + (b1+float(list2016[l][1])*WL3[0][0]+float(list2016[l][3])*WL3[1][0]+float(list2016[l][5])*WL3[2][0]+float(list2016[l][7])*WL3[3][0]+float(list2016[l][13])*WL3[4][0]+float(list2016[l][14])*WL3[5][0])-float(list2016[l][8]);
	#print("err of max temperature in 台南 is %.4f"%(err7/31));
	for l in range(1,32,1):
		err8 = err8 + (b1+float(list2017[l][1])*WL3[0][0]+float(list2017[l][3])*WL3[1][0]+float(list2017[l][5])*WL3[2][0]+float(list2017[l][7])*WL3[3][0]+float(list2017[l][13])*WL3[4][0]+float(list2017[l][14])*WL3[5][0])-float(list2017[l][8]);
	#print("err of max temperature in 高雄 is %.4f"%(err8/31));
	for l in range(1,32,1):
		err9 = err9 + (b1+float(list2018[l][1])*WL3[0][0]+float(list2018[l][3])*WL3[1][0]+float(list2018[l][5])*WL3[2][0]+float(list2018[l][7])*WL3[3][0]+float(list2018[l][13])*WL3[4][0]+float(list2018[l][14])*WL3[5][0])-float(list2018[l][8]);
	#print("err of max temperature in 屏東 is %.4f"%(err9/31));	
	for l in range(1,32,1):
		err10 = err10 + (b1+float(list2019[l][1])*WL3[0][0]+float(list2019[l][3])*WL3[1][0]+float(list2019[l][5])*WL3[2][0]+float(list2019[l][7])*WL3[3][0]+float(list2019[l][13])*WL3[4][0]+float(list2019[l][14])*WL3[5][0])-float(list2019[l][8]);
	#print("err of max temperature in 台東 is %.4f"%(err10/31));	
	for l in range(1,32,1):
		err11 = err11 + (b1+float(list2020[l][1])*WL3[0][0]+float(list2020[l][3])*WL3[1][0]+float(list2020[l][5])*WL3[2][0]+float(list2020[l][7])*WL3[3][0]+float(list2020[l][13])*WL3[4][0]+float(list2020[l][14])*WL3[5][0])-float(list2020[l][8]);
	#print("err of max temperature in 花蓮 is %.4f"%(err11/31));	
	for l in range(1,32,1):
		err12 = err12 + (b1+float(list2021[l][1])*WL3[0][0]+float(list2021[l][3])*WL3[1][0]+float(list2021[l][5])*WL3[2][0]+float(list2021[l][7])*WL3[3][0]+float(list2021[l][13])*WL3[4][0]+float(list2021[l][14])*WL3[5][0])-float(list2021[l][8]);
	#print("err of max temperature in 宜蘭 is %.4f"%(err12/31));	
	for l in range(1,32,1):
		err13 = err13 + (b1+float(list2022[l][1])*WL3[0][0]+float(list2022[l][3])*WL3[1][0]+float(list2022[l][5])*WL3[2][0]+float(list2022[l][7])*WL3[3][0]+float(list2022[l][13])*WL3[4][0]+float(list2022[l][14])*WL3[5][0])-float(list2022[l][8]);
	#print("err of max temperature in 日月潭 is %.4f"%(err13/31));	
	#err = err1+err2+err3+err4+err5+err6+err7+err8+err9+err10+err11+err12+err13
	#err = err/403;
	errr = abs(err1)+abs(err2)+abs(err3)+abs(err4)+abs(err5)+abs(err6)+abs(err7)+abs(err8)+abs(err9)+abs(err10)+abs(err11)+abs(err12)+abs(err13)
	errr = errr/403;
	#err = abs(err);
	#print(errr);
	#rate = rate/1.08;
	
	#print(rate);
print("=======================================================================");	#這裡做溫度輸出
print("err of max temperature in Taiwan is %.4f"%(errr));
for l in range(1,32,1):
	errtm = errtm  + (b1+float(list2010[l][1])*WL3[0][0]+float(list2010[l][3])*WL3[1][0]+float(list2010[l][5])*WL3[2][0]+float(list2010[l][7])*WL3[3][0]+float(list2010[l][13])*WL3[4][0]+float(list2010[l][14])*WL3[5][0])-float(list2010[l][8]);
errtm  = errtm /31;
print("err of max temperature in 基隆 is %.4f"%(errtm));

for l in range(1,32,1):
	errtm = errtm  + (b1+float(list2011[l][1])*WL3[0][0]+float(list2011[l][3])*WL3[1][0]+float(list2011[l][5])*WL3[2][0]+float(list2011[l][7])*WL3[3][0]+float(list2011[l][13])*WL3[4][0]+float(list2011[l][14])*WL3[5][0])-float(list2011[l][8]);
errtm  = errtm /31;
print("err of max temperature in 台北 is %.4f"%(errtm));

for l in range(1,32,1):
	errtm = errtm  + (b1+float(list2012[l][1])*WL3[0][0]+float(list2012[l][3])*WL3[1][0]+float(list2012[l][5])*WL3[2][0]+float(list2012[l][7])*WL3[3][0]+float(list2012[l][13])*WL3[4][0]+float(list2012[l][14])*WL3[5][0])-float(list2012[l][8]);
errtm  = errtm /31;
print("err of max temperature in 桃園 is %.4f"%(errtm));

for l in range(1,32,1):
	errtm = errtm  + (b1+float(list2013[l][1])*WL3[0][0]+float(list2013[l][3])*WL3[1][0]+float(list2013[l][5])*WL3[2][0]+float(list2013[l][7])*WL3[3][0]+float(list2013[l][13])*WL3[4][0]+float(list2013[l][14])*WL3[5][0])-float(list2013[l][8]);
errtm  = errtm /31;
print("err of max temperature in 新竹 is %.4f"%(errtm));

for l in range(1,32,1):
	errtm = errtm  + (b1+float(list2014[l][1])*WL3[0][0]+float(list2014[l][3])*WL3[1][0]+float(list2014[l][5])*WL3[2][0]+float(list2014[l][7])*WL3[3][0]+float(list2014[l][13])*WL3[4][0]+float(list2014[l][14])*WL3[5][0])-float(list2014[l][8]);
errtm  = errtm /31;
print("err of max temperature in 台中 is %.4f"%(errtm));

for l in range(1,32,1):
	errtm = errtm  + (b1+float(list2015[l][1])*WL3[0][0]+float(list2015[l][3])*WL3[1][0]+float(list2015[l][5])*WL3[2][0]+float(list2015[l][7])*WL3[3][0]+float(list2015[l][13])*WL3[4][0]+float(list2015[l][14])*WL3[5][0])-float(list2015[l][8]);
errtm  = errtm /31;
print("err of max temperature in 嘉義 is %.4f"%(errtm));

for l in range(1,32,1):
	errtm = errtm  + (b1+float(list2016[l][1])*WL3[0][0]+float(list2016[l][3])*WL3[1][0]+float(list2016[l][5])*WL3[2][0]+float(list2016[l][7])*WL3[3][0]+float(list2016[l][13])*WL3[4][0]+float(list2016[l][14])*WL3[5][0])-float(list2016[l][8]);
errtm  = errtm /31;
print("err of max temperature in 台南 is %.4f"%(errtm));

for l in range(1,32,1):
	errtm = errtm  + (b1+float(list2017[l][1])*WL3[0][0]+float(list2017[l][3])*WL3[1][0]+float(list2017[l][5])*WL3[2][0]+float(list2017[l][7])*WL3[3][0]+float(list2017[l][13])*WL3[4][0]+float(list2017[l][14])*WL3[5][0])-float(list2017[l][8]);
errtm  = errtm /31;
print("err of max temperature in 高雄 is %.4f"%(errtm));

for l in range(1,32,1):
	errtm = errtm  + (b1+float(list2018[l][1])*WL3[0][0]+float(list2018[l][3])*WL3[1][0]+float(list2018[l][5])*WL3[2][0]+float(list2018[l][7])*WL3[3][0]+float(list2018[l][13])*WL3[4][0]+float(list2018[l][14])*WL3[5][0])-float(list2018[l][8]);
errtm  = errtm /31;
print("err of max temperature in 屏東 is %.4f"%(errtm));

for l in range(1,32,1):
	errtm = errtm  + (b1+float(list2019[l][1])*WL3[0][0]+float(list2019[l][3])*WL3[1][0]+float(list2019[l][5])*WL3[2][0]+float(list2019[l][7])*WL3[3][0]+float(list2019[l][13])*WL3[4][0]+float(list2019[l][14])*WL3[5][0])-float(list2019[l][8]);
errtm  = errtm /31;
print("err of max temperature in 台東 is %.4f"%(errtm));

for l in range(1,32,1):
	errtm = errtm  + (b1+float(list2020[l][1])*WL3[0][0]+float(list2020[l][3])*WL3[1][0]+float(list2020[l][5])*WL3[2][0]+float(list2020[l][7])*WL3[3][0]+float(list2020[l][13])*WL3[4][0]+float(list2020[l][14])*WL3[5][0])-float(list2020[l][8]);
errtm  = errtm /31;
print("err of max temperature in 花蓮 is %.4f"%(errtm));

for l in range(1,32,1):
	errtm = errtm  + (b1+float(list2021[l][1])*WL3[0][0]+float(list2021[l][3])*WL3[1][0]+float(list2021[l][5])*WL3[2][0]+float(list2021[l][7])*WL3[3][0]+float(list2021[l][13])*WL3[4][0]+float(list2021[l][14])*WL3[5][0])-float(list2021[l][8]);
errtm  = errtm /31;
print("err of max temperature in 宜蘭 is %.4f"%(errtm));

for l in range(1,32,1):
	errtm = errtm  + (b1+float(list2022[l][1])*WL3[0][0]+float(list2022[l][3])*WL3[1][0]+float(list2022[l][5])*WL3[2][0]+float(list2022[l][7])*WL3[3][0]+float(list2022[l][13])*WL3[4][0]+float(list2022[l][14])*WL3[5][0])-float(list2022[l][8]);
errtm  = errtm /31;
print("err of max temperature in 日月潭 is %.4f"%(errtm));

for l in range(1,32,1):
	sum = (b1+float(list2011[l][1])*WL3[0][0]+float(list2011[l][3])*WL3[1][0]+float(list2011[l][5])*WL3[2][0]+float(list2011[l][7])*WL3[3][0]+float(list2011[l][13])*WL3[4][0]+float(list2011[l][14])*WL3[5][0]);
	print("temperature in 台北 day %.0f is %.4f"%(l,sum));

#print(WL3);
'''
print("WL2",WL2);
print("WL3",WL3);
print("HL2",HL2);
print("HL3",HL3);
print("ERRH2",ERRH2);
print("ERRH3",ERRH3);
print("HL2=%.4f"%(HL2[3]));
'''

#這裡做風速自算
rateWS = 0.000000004;
b1WS=b2WS=b3WS=1.0;

WL2WS = [[float(0.03) for i in range(9)] for j in range(6)];
WH2WS = [[float(0.02) for i in range(9)] for j in range(9)];
WL3WS = [[float(0.01) for i in range(6)] for j in range(9)];

errr = 50
err=err1=err2=err3=err4=err5=err6=err7=err8=err9=err10=err11=err12=err13 = 3.0;
errWS  = 0;
while  errr >  1:
	for i in range(1,32,1):

		HL2WS= [float(0) for i in range(9)];
		HL22WS= [float(0) for i in range(9)];
		HL3WS= [float(0) for i in range(6)];
		ERRH2WS = [float(0) for i in range(9)];
		ERRH22WS = [float(0) for i in range(9)];
		ERRH3WS = [float(0) for i in range(6)];	
		
		for j in range(9):
			output = b1WS+float(list2010[i][1])*WL2WS[0][j]+float(list2010[i][3])*WL2WS[1][j]+float(list2010[i][5])*WL2WS[2][j]+float(list2010[i][7])*WL2WS[3][j]+float(list2010[i][13])*WL2WS[4][j]+float(list2010[i][14])*WL2WS[5][j];
			HL2WS[j]=(1/(1+math.exp(output)));
		
		for j in range(9):
			output = b2WS+HL2WS[0]*WH2WS[0][j]+HL2WS[1]*WH2WS[1][j]+HL2WS[2]*WH2WS[2][j]+HL2WS[3]*WH2WS[3][j]+HL2WS[4]*WH2WS[4][j]+HL2WS[5]*WH2WS[5][j]+HL2WS[6]*WH2WS[6][j]+HL2WS[7]*WH2WS[7][j]+HL2WS[8]*WH2WS[8][j];
			HL22WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22WS[0]*WL3WS[0][j]+HL22WS[1]*WL3WS[1][j]+HL22WS[2]*WL3WS[2][j]+HL22WS[3]*WL3WS[3][j]+HL22WS[4]*WL3WS[4][j]+HL22WS[5]*WL3WS[5][j]+HL22WS[6]*WL3WS[6][j]+HL22WS[7]*WL3WS[7][j]+HL22WS[8]*WL3WS[8][j];
			HL3WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):		
			ERRH3WS[j]=(HL3WS[j]*(1-HL3WS[j])*(HL3WS[j]-float(list2010[i][16])));				

		for j in range(9):
			ERRH22WS[j]=(HL22WS[j]*(1-HL22WS[j])*(WL3WS[j][0]*ERRH3WS[0]+WL3WS[j][1]*ERRH3WS[1]+WL3WS[j][2]*ERRH3WS[2]+WL3WS[j][3]*ERRH3WS[3]+WL3WS[j][4]*ERRH3WS[4]+WL3WS[j][5]*ERRH3WS[5]));
			
		for j in range(9):		
			ERRH2WS[j]=(HL2WS[j]*(1-HL2WS[j])*(WH2WS[j][0]*ERRH22WS[0]+WH2WS[j][1]*ERRH22WS[1]+WL3WS[j][2]*ERRH22WS[2]+WH2WS[j][3]*ERRH22WS[3]+WH2WS[j][4]*ERRH22WS[4]+WH2WS[j][5]*ERRH22WS[5]+WH2WS[j][6]*ERRH22WS[6]+WH2WS[j][7]*ERRH22WS[7]+WH2WS[j][8]*ERRH22WS[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2010[i][1]);
				elif j == 1:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2010[i][3]);
				elif j == 2:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2010[i][5]);
				elif j == 3:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2010[i][7]);
				elif j == 4:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2010[i][13]);
				elif j == 5:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2010[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2010[i][1]);
				elif j == 1:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2010[i][3]);
				elif j == 2:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2010[i][5]);
				elif j == 3:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2010[i][7]);
				elif j == 4:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2010[i][13]);
				elif j == 5:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2010[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2010[i][1]);
				elif j == 1:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2010[i][3]);
				elif j == 2:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2010[i][5]);
				elif j == 3:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2010[i][7]);
				elif j == 4:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2010[i][13]);
				elif j == 5:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2010[i][14]); 	

		for j in range(9):
			output = b1WS+float(list2011[i][1])*WL2WS[0][j]+float(list2011[i][3])*WL2WS[1][j]+float(list2011[i][5])*WL2WS[2][j]+float(list2011[i][7])*WL2WS[3][j]+float(list2011[i][13])*WL2WS[4][j]+float(list2011[i][14])*WL2WS[5][j];
			HL2WS[j]=(1/(1+math.exp(output)));
		
		for j in range(9):
			output = b2WS+HL2WS[0]*WH2WS[0][j]+HL2WS[1]*WH2WS[1][j]+HL2WS[2]*WH2WS[2][j]+HL2WS[3]*WH2WS[3][j]+HL2WS[4]*WH2WS[4][j]+HL2WS[5]*WH2WS[5][j]+HL2WS[6]*WH2WS[6][j]+HL2WS[7]*WH2WS[7][j]+HL2WS[8]*WH2WS[8][j];
			HL22WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22WS[0]*WL3WS[0][j]+HL22WS[1]*WL3WS[1][j]+HL22WS[2]*WL3WS[2][j]+HL22WS[3]*WL3WS[3][j]+HL22WS[4]*WL3WS[4][j]+HL22WS[5]*WL3WS[5][j]+HL22WS[6]*WL3WS[6][j]+HL22WS[7]*WL3WS[7][j]+HL22WS[8]*WL3WS[8][j];
			HL3WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
				ERRH3WS[j]=(HL3WS[j]*(1-HL3WS[j])*(HL3WS[j]-float(list2011[i][16])));				


		for j in range(9):
			ERRH22WS[j]=(HL22WS[j]*(1-HL22WS[j])*(WL3WS[j][0]*ERRH3WS[0]+WL3WS[j][1]*ERRH3WS[1]+WL3WS[j][2]*ERRH3WS[2]+WL3WS[j][3]*ERRH3WS[3]+WL3WS[j][4]*ERRH3WS[4]+WL3WS[j][5]*ERRH3WS[5]));
			
		for j in range(9):		
			ERRH2WS[j]=(HL2WS[j]*(1-HL2WS[j])*(WH2WS[j][0]*ERRH22WS[0]+WH2WS[j][1]*ERRH22WS[1]+WL3WS[j][2]*ERRH22WS[2]+WH2WS[j][3]*ERRH22WS[3]+WH2WS[j][4]*ERRH22WS[4]+WH2WS[j][5]*ERRH22WS[5]+WH2WS[j][6]*ERRH22WS[6]+WH2WS[j][7]*ERRH22WS[7]+WH2WS[j][8]*ERRH22WS[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2011[i][1]);
				elif j == 1:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2011[i][3]);
				elif j == 2:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2011[i][5]);
				elif j == 3:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2011[i][7]);
				elif j == 4:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2011[i][13]);
				elif j == 5:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2011[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2011[i][1]);
				elif j == 1:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2011[i][3]);
				elif j == 2:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2011[i][5]);
				elif j == 3:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2011[i][7]);
				elif j == 4:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2011[i][13]);
				elif j == 5:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2011[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2011[i][1]);
				elif j == 1:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2011[i][3]);
				elif j == 2:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2011[i][5]);
				elif j == 3:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2011[i][7]);
				elif j == 4:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2011[i][13]);
				elif j == 5:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2011[i][14]); 	

		for j in range(9):
			output = b1WS+float(list2012[i][1])*WL2WS[0][j]+float(list2012[i][3])*WL2WS[1][j]+float(list2012[i][5])*WL2WS[2][j]+float(list2012[i][7])*WL2WS[3][j]+float(list2012[i][13])*WL2WS[4][j]+float(list2012[i][14])*WL2WS[5][j];
			HL2WS[j]=(1/(1+math.exp(output)));
		
		for j in range(9):
			output = b2WS+HL2WS[0]*WH2WS[0][j]+HL2WS[1]*WH2WS[1][j]+HL2WS[2]*WH2WS[2][j]+HL2WS[3]*WH2WS[3][j]+HL2WS[4]*WH2WS[4][j]+HL2WS[5]*WH2WS[5][j]+HL2WS[6]*WH2WS[6][j]+HL2WS[7]*WH2WS[7][j]+HL2WS[8]*WH2WS[8][j];
			HL22WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22WS[0]*WL3WS[0][j]+HL22WS[1]*WL3WS[1][j]+HL22WS[2]*WL3WS[2][j]+HL22WS[3]*WL3WS[3][j]+HL22WS[4]*WL3WS[4][j]+HL22WS[5]*WL3WS[5][j]+HL22WS[6]*WL3WS[6][j]+HL22WS[7]*WL3WS[7][j]+HL22WS[8]*WL3WS[8][j];
			HL3WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
				ERRH3WS[j]=(HL3WS[j]*(1-HL3WS[j])*(HL3WS[j]-float(list2012[i][16])));				


		for j in range(9):
			ERRH22WS[j]=(HL22WS[j]*(1-HL22WS[j])*(WL3WS[j][0]*ERRH3WS[0]+WL3WS[j][1]*ERRH3WS[1]+WL3WS[j][2]*ERRH3WS[2]+WL3WS[j][3]*ERRH3WS[3]+WL3WS[j][4]*ERRH3WS[4]+WL3WS[j][5]*ERRH3WS[5]));
			
		for j in range(9):		
			ERRH2WS[j]=(HL2WS[j]*(1-HL2WS[j])*(WH2WS[j][0]*ERRH22WS[0]+WH2WS[j][1]*ERRH22WS[1]+WL3WS[j][2]*ERRH22WS[2]+WH2WS[j][3]*ERRH22WS[3]+WH2WS[j][4]*ERRH22WS[4]+WH2WS[j][5]*ERRH22WS[5]+WH2WS[j][6]*ERRH22WS[6]+WH2WS[j][7]*ERRH22WS[7]+WH2WS[j][8]*ERRH22WS[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2012[i][1]);
				elif j == 1:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2012[i][3]);
				elif j == 2:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2012[i][5]);
				elif j == 3:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2012[i][7]);
				elif j == 4:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2012[i][13]);
				elif j == 5:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2012[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2012[i][1]);
				elif j == 1:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2012[i][3]);
				elif j == 2:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2012[i][5]);
				elif j == 3:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2012[i][7]);
				elif j == 4:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2012[i][13]);
				elif j == 5:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2012[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2012[i][1]);
				elif j == 1:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2012[i][3]);
				elif j == 2:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2012[i][5]);
				elif j == 3:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2012[i][7]);
				elif j == 4:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2012[i][13]);
				elif j == 5:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2012[i][14]); 	
					
		for j in range(9):
			output = b1WS+float(list2013[i][1])*WL2WS[0][j]+float(list2013[i][3])*WL2WS[1][j]+float(list2013[i][5])*WL2WS[2][j]+float(list2013[i][7])*WL2WS[3][j]+float(list2013[i][13])*WL2WS[4][j]+float(list2013[i][14])*WL2WS[5][j];
			HL2WS[j]=(1/(1+math.exp(output)));
		
		for j in range(9):
			output = b2WS+HL2WS[0]*WH2WS[0][j]+HL2WS[1]*WH2WS[1][j]+HL2WS[2]*WH2WS[2][j]+HL2WS[3]*WH2WS[3][j]+HL2WS[4]*WH2WS[4][j]+HL2WS[5]*WH2WS[5][j]+HL2WS[6]*WH2WS[6][j]+HL2WS[7]*WH2WS[7][j]+HL2WS[8]*WH2WS[8][j];
			HL22WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22WS[0]*WL3WS[0][j]+HL22WS[1]*WL3WS[1][j]+HL22WS[2]*WL3WS[2][j]+HL22WS[3]*WL3WS[3][j]+HL22WS[4]*WL3WS[4][j]+HL22WS[5]*WL3WS[5][j]+HL22WS[6]*WL3WS[6][j]+HL22WS[7]*WL3WS[7][j]+HL22WS[8]*WL3WS[8][j];
			HL3WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			if err1 > 0 :
				ERRH3WS[j]=(HL3WS[j]*(1-HL3WS[j])*(HL3WS[j]-float(list2013[i][16])));				
			else :
				ERRH3WS[j]=(HL3WS[j]*(1-HL3WS[j])*(float(list2013[i][16])-HL3WS[j]));	

		for j in range(9):
			ERRH22WS[j]=(HL22WS[j]*(1-HL22WS[j])*(WL3WS[j][0]*ERRH3WS[0]+WL3WS[j][1]*ERRH3WS[1]+WL3WS[j][2]*ERRH3WS[2]+WL3WS[j][3]*ERRH3WS[3]+WL3WS[j][4]*ERRH3WS[4]+WL3WS[j][5]*ERRH3WS[5]));
			
		for j in range(9):		
			ERRH2WS[j]=(HL2WS[j]*(1-HL2WS[j])*(WH2WS[j][0]*ERRH22WS[0]+WH2WS[j][1]*ERRH22WS[1]+WL3WS[j][2]*ERRH22WS[2]+WH2WS[j][3]*ERRH22WS[3]+WH2WS[j][4]*ERRH22WS[4]+WH2WS[j][5]*ERRH22WS[5]+WH2WS[j][6]*ERRH22WS[6]+WH2WS[j][7]*ERRH22WS[7]+WH2WS[j][8]*ERRH22WS[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2013[i][1]);
				elif j == 1:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2013[i][3]);
				elif j == 2:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2013[i][5]);
				elif j == 3:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2013[i][7]);
				elif j == 4:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2013[i][13]);
				elif j == 5:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2013[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2013[i][1]);
				elif j == 1:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2013[i][3]);
				elif j == 2:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2013[i][5]);
				elif j == 3:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2013[i][7]);
				elif j == 4:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2013[i][13]);
				elif j == 5:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2013[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2013[i][1]);
				elif j == 1:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2013[i][3]);
				elif j == 2:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2013[i][5]);
				elif j == 3:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2013[i][7]);
				elif j == 4:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2013[i][13]);
				elif j == 5:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2013[i][14]); 	

		for j in range(9):
			output = b1WS+float(list2014[i][1])*WL2WS[0][j]+float(list2014[i][3])*WL2WS[1][j]+float(list2014[i][5])*WL2WS[2][j]+float(list2014[i][7])*WL2WS[3][j]+float(list2014[i][13])*WL2WS[4][j]+float(list2014[i][14])*WL2WS[5][j];
			HL2WS[j]=(1/(1+math.exp(output)));
		
		for j in range(9):
			output = b2WS+HL2WS[0]*WH2WS[0][j]+HL2WS[1]*WH2WS[1][j]+HL2WS[2]*WH2WS[2][j]+HL2WS[3]*WH2WS[3][j]+HL2WS[4]*WH2WS[4][j]+HL2WS[5]*WH2WS[5][j]+HL2WS[6]*WH2WS[6][j]+HL2WS[7]*WH2WS[7][j]+HL2WS[8]*WH2WS[8][j];
			HL22WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22WS[0]*WL3WS[0][j]+HL22WS[1]*WL3WS[1][j]+HL22WS[2]*WL3WS[2][j]+HL22WS[3]*WL3WS[3][j]+HL22WS[4]*WL3WS[4][j]+HL22WS[5]*WL3WS[5][j]+HL22WS[6]*WL3WS[6][j]+HL22WS[7]*WL3WS[7][j]+HL22WS[8]*WL3WS[8][j];
			HL3WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
				ERRH3WS[j]=(HL3WS[j]*(1-HL3WS[j])*(HL3WS[j]-float(list2014[i][16])));				

		for j in range(9):
			ERRH22WS[j]=(HL22WS[j]*(1-HL22WS[j])*(WL3WS[j][0]*ERRH3WS[0]+WL3WS[j][1]*ERRH3WS[1]+WL3WS[j][2]*ERRH3WS[2]+WL3WS[j][3]*ERRH3WS[3]+WL3WS[j][4]*ERRH3WS[4]+WL3WS[j][5]*ERRH3WS[5]));
			
		for j in range(9):		
			ERRH2WS[j]=(HL2WS[j]*(1-HL2WS[j])*(WH2WS[j][0]*ERRH22WS[0]+WH2WS[j][1]*ERRH22WS[1]+WL3WS[j][2]*ERRH22WS[2]+WH2WS[j][3]*ERRH22WS[3]+WH2WS[j][4]*ERRH22WS[4]+WH2WS[j][5]*ERRH22WS[5]+WH2WS[j][6]*ERRH22WS[6]+WH2WS[j][7]*ERRH22WS[7]+WH2WS[j][8]*ERRH22WS[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2014[i][1]);
				elif j == 1:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2014[i][3]);
				elif j == 2:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2014[i][5]);
				elif j == 3:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2014[i][7]);
				elif j == 4:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2014[i][13]);
				elif j == 5:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2014[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2014[i][1]);
				elif j == 1:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2014[i][3]);
				elif j == 2:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2014[i][5]);
				elif j == 3:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2014[i][7]);
				elif j == 4:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2014[i][13]);
				elif j == 5:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2014[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2014[i][1]);
				elif j == 1:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2014[i][3]);
				elif j == 2:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2014[i][5]);
				elif j == 3:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2014[i][7]);
				elif j == 4:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2014[i][13]);
				elif j == 5:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2014[i][14]); 	

		for j in range(9):
			output = b1WS+float(list2015[i][1])*WL2WS[0][j]+float(list2015[i][3])*WL2WS[1][j]+float(list2015[i][5])*WL2WS[2][j]+float(list2015[i][7])*WL2WS[3][j]+float(list2015[i][13])*WL2WS[4][j]+float(list2015[i][14])*WL2WS[5][j];
			HL2WS[j]=(1/(1+math.exp(output)));
		
		for j in range(9):
			output = b2WS+HL2WS[0]*WH2WS[0][j]+HL2WS[1]*WH2WS[1][j]+HL2WS[2]*WH2WS[2][j]+HL2WS[3]*WH2WS[3][j]+HL2WS[4]*WH2WS[4][j]+HL2WS[5]*WH2WS[5][j]+HL2WS[6]*WH2WS[6][j]+HL2WS[7]*WH2WS[7][j]+HL2WS[8]*WH2WS[8][j];
			HL22WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22WS[0]*WL3WS[0][j]+HL22WS[1]*WL3WS[1][j]+HL22WS[2]*WL3WS[2][j]+HL22WS[3]*WL3WS[3][j]+HL22WS[4]*WL3WS[4][j]+HL22WS[5]*WL3WS[5][j]+HL22WS[6]*WL3WS[6][j]+HL22WS[7]*WL3WS[7][j]+HL22WS[8]*WL3WS[8][j];
			HL3WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
				ERRH3WS[j]=(HL3WS[j]*(1-HL3WS[j])*(HL3WS[j]-float(list2015[i][16])));				

		for j in range(9):
			ERRH22WS[j]=(HL22WS[j]*(1-HL22WS[j])*(WL3WS[j][0]*ERRH3WS[0]+WL3WS[j][1]*ERRH3WS[1]+WL3WS[j][2]*ERRH3WS[2]+WL3WS[j][3]*ERRH3WS[3]+WL3WS[j][4]*ERRH3WS[4]+WL3WS[j][5]*ERRH3WS[5]));
			
		for j in range(9):		
			ERRH2WS[j]=(HL2WS[j]*(1-HL2WS[j])*(WH2WS[j][0]*ERRH22WS[0]+WH2WS[j][1]*ERRH22WS[1]+WL3WS[j][2]*ERRH22WS[2]+WH2WS[j][3]*ERRH22WS[3]+WH2WS[j][4]*ERRH22WS[4]+WH2WS[j][5]*ERRH22WS[5]+WH2WS[j][6]*ERRH22WS[6]+WH2WS[j][7]*ERRH22WS[7]+WH2WS[j][8]*ERRH22WS[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2015[i][1]);
				elif j == 1:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2015[i][3]);
				elif j == 2:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2015[i][5]);
				elif j == 3:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2015[i][7]);
				elif j == 4:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2015[i][13]);
				elif j == 5:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2015[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2015[i][1]);
				elif j == 1:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2015[i][3]);
				elif j == 2:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2015[i][5]);
				elif j == 3:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2015[i][7]);
				elif j == 4:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2015[i][13]);
				elif j == 5:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2015[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2015[i][1]);
				elif j == 1:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2015[i][3]);
				elif j == 2:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2015[i][5]);
				elif j == 3:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2015[i][7]);
				elif j == 4:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2015[i][13]);
				elif j == 5:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2015[i][14]); 	

		for j in range(9):
			output = b1WS+float(list2016[i][1])*WL2WS[0][j]+float(list2016[i][3])*WL2WS[1][j]+float(list2016[i][5])*WL2WS[2][j]+float(list2016[i][7])*WL2WS[3][j]+float(list2016[i][13])*WL2WS[4][j]+float(list2016[i][14])*WL2WS[5][j];
			HL2WS[j]=(1/(1+math.exp(output)));
		
		for j in range(9):
			output = b2WS+HL2WS[0]*WH2WS[0][j]+HL2WS[1]*WH2WS[1][j]+HL2WS[2]*WH2WS[2][j]+HL2WS[3]*WH2WS[3][j]+HL2WS[4]*WH2WS[4][j]+HL2WS[5]*WH2WS[5][j]+HL2WS[6]*WH2WS[6][j]+HL2WS[7]*WH2WS[7][j]+HL2WS[8]*WH2WS[8][j];
			HL22WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22WS[0]*WL3WS[0][j]+HL22WS[1]*WL3WS[1][j]+HL22WS[2]*WL3WS[2][j]+HL22WS[3]*WL3WS[3][j]+HL22WS[4]*WL3WS[4][j]+HL22WS[5]*WL3WS[5][j]+HL22WS[6]*WL3WS[6][j]+HL22WS[7]*WL3WS[7][j]+HL22WS[8]*WL3WS[8][j];
			HL3WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
				ERRH3WS[j]=(HL3WS[j]*(1-HL3WS[j])*(HL3WS[j]-float(list2016[i][16])));				

		for j in range(9):
			ERRH22WS[j]=(HL22WS[j]*(1-HL22WS[j])*(WL3WS[j][0]*ERRH3WS[0]+WL3WS[j][1]*ERRH3WS[1]+WL3WS[j][2]*ERRH3WS[2]+WL3WS[j][3]*ERRH3WS[3]+WL3WS[j][4]*ERRH3WS[4]+WL3WS[j][5]*ERRH3WS[5]));
			
		for j in range(9):		
			ERRH2WS[j]=(HL2WS[j]*(1-HL2WS[j])*(WH2WS[j][0]*ERRH22WS[0]+WH2WS[j][1]*ERRH22WS[1]+WL3WS[j][2]*ERRH22WS[2]+WH2WS[j][3]*ERRH22WS[3]+WH2WS[j][4]*ERRH22WS[4]+WH2WS[j][5]*ERRH22WS[5]+WH2WS[j][6]*ERRH22WS[6]+WH2WS[j][7]*ERRH22WS[7]+WH2WS[j][8]*ERRH22WS[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2016[i][1]);
				elif j == 1:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2016[i][3]);
				elif j == 2:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2016[i][5]);
				elif j == 3:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2016[i][7]);
				elif j == 4:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2016[i][13]);
				elif j == 5:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2016[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2016[i][1]);
				elif j == 1:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2016[i][3]);
				elif j == 2:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2016[i][5]);
				elif j == 3:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2016[i][7]);
				elif j == 4:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2016[i][13]);
				elif j == 5:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2016[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2016[i][1]);
				elif j == 1:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2016[i][3]);
				elif j == 2:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2016[i][5]);
				elif j == 3:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2016[i][7]);
				elif j == 4:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2016[i][13]);
				elif j == 5:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2016[i][14]); 	

		for j in range(9):
			output = b1WS+float(list2017[i][1])*WL2WS[0][j]+float(list2017[i][3])*WL2WS[1][j]+float(list2017[i][5])*WL2WS[2][j]+float(list2017[i][7])*WL2WS[3][j]+float(list2017[i][13])*WL2WS[4][j]+float(list2017[i][14])*WL2WS[5][j];
			HL2WS[j]=(1/(1+math.exp(output)));
		
		for j in range(9):
			output = b2WS+HL2WS[0]*WH2WS[0][j]+HL2WS[1]*WH2WS[1][j]+HL2WS[2]*WH2WS[2][j]+HL2WS[3]*WH2WS[3][j]+HL2WS[4]*WH2WS[4][j]+HL2WS[5]*WH2WS[5][j]+HL2WS[6]*WH2WS[6][j]+HL2WS[7]*WH2WS[7][j]+HL2WS[8]*WH2WS[8][j];
			HL22WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22WS[0]*WL3WS[0][j]+HL22WS[1]*WL3WS[1][j]+HL22WS[2]*WL3WS[2][j]+HL22WS[3]*WL3WS[3][j]+HL22WS[4]*WL3WS[4][j]+HL22WS[5]*WL3WS[5][j]+HL22WS[6]*WL3WS[6][j]+HL22WS[7]*WL3WS[7][j]+HL22WS[8]*WL3WS[8][j];
			HL3WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
				ERRH3WS[j]=(HL3WS[j]*(1-HL3WS[j])*(HL3WS[j]-float(list2017[i][16])));				

		for j in range(9):
			ERRH22WS[j]=(HL22WS[j]*(1-HL22WS[j])*(WL3WS[j][0]*ERRH3WS[0]+WL3WS[j][1]*ERRH3WS[1]+WL3WS[j][2]*ERRH3WS[2]+WL3WS[j][3]*ERRH3WS[3]+WL3WS[j][4]*ERRH3WS[4]+WL3WS[j][5]*ERRH3WS[5]));
			
		for j in range(9):		
			ERRH2WS[j]=(HL2WS[j]*(1-HL2WS[j])*(WH2WS[j][0]*ERRH22WS[0]+WH2WS[j][1]*ERRH22WS[1]+WL3WS[j][2]*ERRH22WS[2]+WH2WS[j][3]*ERRH22WS[3]+WH2WS[j][4]*ERRH22WS[4]+WH2WS[j][5]*ERRH22WS[5]+WH2WS[j][6]*ERRH22WS[6]+WH2WS[j][7]*ERRH22WS[7]+WH2WS[j][8]*ERRH22WS[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2017[i][1]);
				elif j == 1:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2017[i][3]);
				elif j == 2:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2017[i][5]);
				elif j == 3:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2017[i][7]);
				elif j == 4:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2017[i][13]);
				elif j == 5:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2017[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2017[i][1]);
				elif j == 1:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2017[i][3]);
				elif j == 2:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2017[i][5]);
				elif j == 3:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2017[i][7]);
				elif j == 4:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2017[i][13]);
				elif j == 5:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2017[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2017[i][1]);
				elif j == 1:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2017[i][3]);
				elif j == 2:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2017[i][5]);
				elif j == 3:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2017[i][7]);
				elif j == 4:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2017[i][13]);
				elif j == 5:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2017[i][14]); 	

		for j in range(9):
			output = b1WS+float(list2018[i][1])*WL2WS[0][j]+float(list2018[i][3])*WL2WS[1][j]+float(list2018[i][5])*WL2WS[2][j]+float(list2018[i][7])*WL2WS[3][j]+float(list2018[i][13])*WL2WS[4][j]+float(list2018[i][14])*WL2WS[5][j];
			HL2WS[j]=(1/(1+math.exp(output)));
		
		for j in range(9):
			output = b2WS+HL2WS[0]*WH2WS[0][j]+HL2WS[1]*WH2WS[1][j]+HL2WS[2]*WH2WS[2][j]+HL2WS[3]*WH2WS[3][j]+HL2WS[4]*WH2WS[4][j]+HL2WS[5]*WH2WS[5][j]+HL2WS[6]*WH2WS[6][j]+HL2WS[7]*WH2WS[7][j]+HL2WS[8]*WH2WS[8][j];
			HL22WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22WS[0]*WL3WS[0][j]+HL22WS[1]*WL3WS[1][j]+HL22WS[2]*WL3WS[2][j]+HL22WS[3]*WL3WS[3][j]+HL22WS[4]*WL3WS[4][j]+HL22WS[5]*WL3WS[5][j]+HL22WS[6]*WL3WS[6][j]+HL22WS[7]*WL3WS[7][j]+HL22WS[8]*WL3WS[8][j];
			HL3WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
				ERRH3WS[j]=(HL3WS[j]*(1-HL3WS[j])*(HL3WS[j]-float(list2018[i][16])));					

		for j in range(9):
			ERRH22WS[j]=(HL22WS[j]*(1-HL22WS[j])*(WL3WS[j][0]*ERRH3WS[0]+WL3WS[j][1]*ERRH3WS[1]+WL3WS[j][2]*ERRH3WS[2]+WL3WS[j][3]*ERRH3WS[3]+WL3WS[j][4]*ERRH3WS[4]+WL3WS[j][5]*ERRH3WS[5]));
			
		for j in range(9):		
			ERRH2WS[j]=(HL2WS[j]*(1-HL2WS[j])*(WH2WS[j][0]*ERRH22WS[0]+WH2WS[j][1]*ERRH22WS[1]+WL3WS[j][2]*ERRH22WS[2]+WH2WS[j][3]*ERRH22WS[3]+WH2WS[j][4]*ERRH22WS[4]+WH2WS[j][5]*ERRH22WS[5]+WH2WS[j][6]*ERRH22WS[6]+WH2WS[j][7]*ERRH22WS[7]+WH2WS[j][8]*ERRH22WS[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2018[i][1]);
				elif j == 1:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2018[i][3]);
				elif j == 2:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2018[i][5]);
				elif j == 3:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2018[i][7]);
				elif j == 4:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2018[i][13]);
				elif j == 5:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2018[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2018[i][1]);
				elif j == 1:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2018[i][3]);
				elif j == 2:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2018[i][5]);
				elif j == 3:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2018[i][7]);
				elif j == 4:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2018[i][13]);
				elif j == 5:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2018[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2018[i][1]);
				elif j == 1:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2018[i][3]);
				elif j == 2:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2018[i][5]);
				elif j == 3:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2018[i][7]);
				elif j == 4:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2018[i][13]);
				elif j == 5:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2018[i][14]); 	

		for j in range(9):
			output = b1WS+float(list2019[i][1])*WL2WS[0][j]+float(list2019[i][3])*WL2WS[1][j]+float(list2019[i][5])*WL2WS[2][j]+float(list2019[i][7])*WL2WS[3][j]+float(list2019[i][13])*WL2WS[4][j]+float(list2019[i][14])*WL2WS[5][j];
			HL2WS[j]=(1/(1+math.exp(output)));
		
		for j in range(9):
			output = b2WS+HL2WS[0]*WH2WS[0][j]+HL2WS[1]*WH2WS[1][j]+HL2WS[2]*WH2WS[2][j]+HL2WS[3]*WH2WS[3][j]+HL2WS[4]*WH2WS[4][j]+HL2WS[5]*WH2WS[5][j]+HL2WS[6]*WH2WS[6][j]+HL2WS[7]*WH2WS[7][j]+HL2WS[8]*WH2WS[8][j];
			HL22WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22WS[0]*WL3WS[0][j]+HL22WS[1]*WL3WS[1][j]+HL22WS[2]*WL3WS[2][j]+HL22WS[3]*WL3WS[3][j]+HL22WS[4]*WL3WS[4][j]+HL22WS[5]*WL3WS[5][j]+HL22WS[6]*WL3WS[6][j]+HL22WS[7]*WL3WS[7][j]+HL22WS[8]*WL3WS[8][j];
			HL3WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
				ERRH3WS[j]=(HL3WS[j]*(1-HL3WS[j])*(HL3WS[j]-float(list2019[i][16])));					

		for j in range(9):
			ERRH22WS[j]=(HL22WS[j]*(1-HL22WS[j])*(WL3WS[j][0]*ERRH3WS[0]+WL3WS[j][1]*ERRH3WS[1]+WL3WS[j][2]*ERRH3WS[2]+WL3WS[j][3]*ERRH3WS[3]+WL3WS[j][4]*ERRH3WS[4]+WL3WS[j][5]*ERRH3WS[5]));
			
		for j in range(9):		
			ERRH2WS[j]=(HL2WS[j]*(1-HL2WS[j])*(WH2WS[j][0]*ERRH22WS[0]+WH2WS[j][1]*ERRH22WS[1]+WL3WS[j][2]*ERRH22WS[2]+WH2WS[j][3]*ERRH22WS[3]+WH2WS[j][4]*ERRH22WS[4]+WH2WS[j][5]*ERRH22WS[5]+WH2WS[j][6]*ERRH22WS[6]+WH2WS[j][7]*ERRH22WS[7]+WH2WS[j][8]*ERRH22WS[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2019[i][1]);
				elif j == 1:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2019[i][3]);
				elif j == 2:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2019[i][5]);
				elif j == 3:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2019[i][7]);
				elif j == 4:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2019[i][13]);
				elif j == 5:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2019[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2019[i][1]);
				elif j == 1:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2019[i][3]);
				elif j == 2:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2019[i][5]);
				elif j == 3:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2019[i][7]);
				elif j == 4:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2019[i][13]);
				elif j == 5:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2019[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2019[i][1]);
				elif j == 1:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2019[i][3]);
				elif j == 2:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2019[i][5]);
				elif j == 3:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2019[i][7]);
				elif j == 4:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2019[i][13]);
				elif j == 5:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2019[i][14]); 	

		for j in range(9):
			output = b1WS+float(list2020[i][1])*WL2WS[0][j]+float(list2020[i][3])*WL2WS[1][j]+float(list2020[i][5])*WL2WS[2][j]+float(list2020[i][7])*WL2WS[3][j]+float(list2020[i][13])*WL2WS[4][j]+float(list2020[i][14])*WL2WS[5][j];
			HL2WS[j]=(1/(1+math.exp(output)));
		
		for j in range(9):
			output = b2WS+HL2WS[0]*WH2WS[0][j]+HL2WS[1]*WH2WS[1][j]+HL2WS[2]*WH2WS[2][j]+HL2WS[3]*WH2WS[3][j]+HL2WS[4]*WH2WS[4][j]+HL2WS[5]*WH2WS[5][j]+HL2WS[6]*WH2WS[6][j]+HL2WS[7]*WH2WS[7][j]+HL2WS[8]*WH2WS[8][j];
			HL22WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22WS[0]*WL3WS[0][j]+HL22WS[1]*WL3WS[1][j]+HL22WS[2]*WL3WS[2][j]+HL22WS[3]*WL3WS[3][j]+HL22WS[4]*WL3WS[4][j]+HL22WS[5]*WL3WS[5][j]+HL22WS[6]*WL3WS[6][j]+HL22WS[7]*WL3WS[7][j]+HL22WS[8]*WL3WS[8][j];
			HL3WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
				ERRH3WS[j]=(HL3WS[j]*(1-HL3WS[j])*(HL3WS[j]-float(list2020[i][16])));				

		for j in range(9):
			ERRH22WS[j]=(HL22WS[j]*(1-HL22WS[j])*(WL3WS[j][0]*ERRH3WS[0]+WL3WS[j][1]*ERRH3WS[1]+WL3WS[j][2]*ERRH3WS[2]+WL3WS[j][3]*ERRH3WS[3]+WL3WS[j][4]*ERRH3WS[4]+WL3WS[j][5]*ERRH3WS[5]));
			
		for j in range(9):		
			ERRH2WS[j]=(HL2WS[j]*(1-HL2WS[j])*(WH2WS[j][0]*ERRH22WS[0]+WH2WS[j][1]*ERRH22WS[1]+WL3WS[j][2]*ERRH22WS[2]+WH2WS[j][3]*ERRH22WS[3]+WH2WS[j][4]*ERRH22WS[4]+WH2WS[j][5]*ERRH22WS[5]+WH2WS[j][6]*ERRH22WS[6]+WH2WS[j][7]*ERRH22WS[7]+WH2WS[j][8]*ERRH22WS[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2020[i][1]);
				elif j == 1:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2020[i][3]);
				elif j == 2:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2020[i][5]);
				elif j == 3:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2020[i][7]);
				elif j == 4:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2020[i][13]);
				elif j == 5:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2020[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2020[i][1]);
				elif j == 1:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2020[i][3]);
				elif j == 2:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2020[i][5]);
				elif j == 3:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2020[i][7]);
				elif j == 4:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2020[i][13]);
				elif j == 5:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2020[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2020[i][1]);
				elif j == 1:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2020[i][3]);
				elif j == 2:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2020[i][5]);
				elif j == 3:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2020[i][7]);
				elif j == 4:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2020[i][13]);
				elif j == 5:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2020[i][14]); 	

		for j in range(9):
			output = b1WS+float(list2021[i][1])*WL2WS[0][j]+float(list2021[i][3])*WL2WS[1][j]+float(list2021[i][5])*WL2WS[2][j]+float(list2021[i][7])*WL2WS[3][j]+float(list2021[i][13])*WL2WS[4][j]+float(list2021[i][14])*WL2WS[5][j];
			HL2WS[j]=(1/(1+math.exp(output)));
		
		for j in range(9):
			output = b2WS+HL2WS[0]*WH2WS[0][j]+HL2WS[1]*WH2WS[1][j]+HL2WS[2]*WH2WS[2][j]+HL2WS[3]*WH2WS[3][j]+HL2WS[4]*WH2WS[4][j]+HL2WS[5]*WH2WS[5][j]+HL2WS[6]*WH2WS[6][j]+HL2WS[7]*WH2WS[7][j]+HL2WS[8]*WH2WS[8][j];
			HL22WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22WS[0]*WL3WS[0][j]+HL22WS[1]*WL3WS[1][j]+HL22WS[2]*WL3WS[2][j]+HL22WS[3]*WL3WS[3][j]+HL22WS[4]*WL3WS[4][j]+HL22WS[5]*WL3WS[5][j]+HL22WS[6]*WL3WS[6][j]+HL22WS[7]*WL3WS[7][j]+HL22WS[8]*WL3WS[8][j];
			HL3WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
				ERRH3WS[j]=(HL3WS[j]*(1-HL3WS[j])*(HL3WS[j]-float(list2021[i][16])));					

		for j in range(9):
			ERRH22WS[j]=(HL22WS[j]*(1-HL22WS[j])*(WL3WS[j][0]*ERRH3WS[0]+WL3WS[j][1]*ERRH3WS[1]+WL3WS[j][2]*ERRH3WS[2]+WL3WS[j][3]*ERRH3WS[3]+WL3WS[j][4]*ERRH3WS[4]+WL3WS[j][5]*ERRH3WS[5]));
			
		for j in range(9):		
			ERRH2WS[j]=(HL2WS[j]*(1-HL2WS[j])*(WH2WS[j][0]*ERRH22WS[0]+WH2WS[j][1]*ERRH22WS[1]+WL3WS[j][2]*ERRH22WS[2]+WH2WS[j][3]*ERRH22WS[3]+WH2WS[j][4]*ERRH22WS[4]+WH2WS[j][5]*ERRH22WS[5]+WH2WS[j][6]*ERRH22WS[6]+WH2WS[j][7]*ERRH22WS[7]+WH2WS[j][8]*ERRH22WS[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2021[i][1]);
				elif j == 1:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2021[i][3]);
				elif j == 2:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2021[i][5]);
				elif j == 3:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2021[i][7]);
				elif j == 4:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2021[i][13]);
				elif j == 5:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2021[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2021[i][1]);
				elif j == 1:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2021[i][3]);
				elif j == 2:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2021[i][5]);
				elif j == 3:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2021[i][7]);
				elif j == 4:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2021[i][13]);
				elif j == 5:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2021[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2021[i][1]);
				elif j == 1:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2021[i][3]);
				elif j == 2:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2021[i][5]);
				elif j == 3:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2021[i][7]);
				elif j == 4:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2021[i][13]);
				elif j == 5:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2021[i][14]); 		
					
		for j in range(9):
			output = b1WS+float(list2022[i][1])*WL2WS[0][j]+float(list2022[i][3])*WL2WS[1][j]+float(list2022[i][5])*WL2WS[2][j]+float(list2022[i][7])*WL2WS[3][j]+float(list2022[i][13])*WL2WS[4][j]+float(list2022[i][14])*WL2WS[5][j];
			HL2WS[j]=(1/(1+math.exp(output)));
		
		for j in range(9):
			output = b2WS+HL2WS[0]*WH2WS[0][j]+HL2WS[1]*WH2WS[1][j]+HL2WS[2]*WH2WS[2][j]+HL2WS[3]*WH2WS[3][j]+HL2WS[4]*WH2WS[4][j]+HL2WS[5]*WH2WS[5][j]+HL2WS[6]*WH2WS[6][j]+HL2WS[7]*WH2WS[7][j]+HL2WS[8]*WH2WS[8][j];
			HL22WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
			output = b3+HL22WS[0]*WL3WS[0][j]+HL22WS[1]*WL3WS[1][j]+HL22WS[2]*WL3WS[2][j]+HL22WS[3]*WL3WS[3][j]+HL22WS[4]*WL3WS[4][j]+HL22WS[5]*WL3WS[5][j]+HL22WS[6]*WL3WS[6][j]+HL22WS[7]*WL3WS[7][j]+HL22WS[8]*WL3WS[8][j];
			HL3WS[j]=(1/(1+math.exp(output)));
			
		for j in range(6):
				ERRH3WS[j]=(HL3WS[j]*(1-HL3WS[j])*(HL3WS[j]-float(list2022[i][16])));					

		for j in range(9):
			ERRH22WS[j]=(HL22WS[j]*(1-HL22WS[j])*(WL3WS[j][0]*ERRH3WS[0]+WL3WS[j][1]*ERRH3WS[1]+WL3WS[j][2]*ERRH3WS[2]+WL3WS[j][3]*ERRH3WS[3]+WL3WS[j][4]*ERRH3WS[4]+WL3WS[j][5]*ERRH3WS[5]));
			
		for j in range(9):		
			ERRH2WS[j]=(HL2WS[j]*(1-HL2WS[j])*(WH2WS[j][0]*ERRH22WS[0]+WH2WS[j][1]*ERRH22WS[1]+WL3WS[j][2]*ERRH22WS[2]+WH2WS[j][3]*ERRH22WS[3]+WH2WS[j][4]*ERRH22WS[4]+WH2WS[j][5]*ERRH22WS[5]+WH2WS[j][6]*ERRH22WS[6]+WH2WS[j][7]*ERRH22WS[7]+WH2WS[j][8]*ERRH22WS[8]));					

		for j in range(6):
			for k in range(9):			
				if j == 0:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2022[i][1]);
				elif j == 1:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2022[i][3]);
				elif j == 2:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2022[i][5]);
				elif j == 3:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2022[i][7]);
				elif j == 4:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2022[i][13]);
				elif j == 5:
					WL2WS[j][k]=WL2WS[j][k]+rateWS*ERRH2WS[k]*float(list2022[i][14]);

		for j in range(9):
			for k in range(9):			
				if j == 0:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2022[i][1]);
				elif j == 1:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2022[i][3]);
				elif j == 2:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2022[i][5]);
				elif j == 3:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2022[i][7]);
				elif j == 4:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2022[i][13]);
				elif j == 5:
					WH2WS[j][k]=WH2WS[j][k]+rateWS*ERRH22WS[k]*float(list2022[i][14]);					
			
		for j in range(9):
			for k in range(6):			
				if j == 0:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2022[i][1]);
				elif j == 1:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2022[i][3]);
				elif j == 2:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2022[i][5]);
				elif j == 3:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2022[i][7]);
				elif j == 4:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2022[i][13]);
				elif j == 5:
					WL3WS[j][k]=WL3WS[j][k]+rateWS*ERRH3WS[k]*float(list2022[i][14]); 	

	err=err1=err2=err3=err4=err5=err6=err7=err8=err9=err10=err11=err12=err13 = 0.0;
	for l in range(1,32,1):
		err1 = err1 + (b1WS+float(list2010[l][1])*WL3WS[0][0]+float(list2010[l][3])*WL3WS[1][0]+float(list2010[l][5])*WL3WS[2][0]+float(list2010[l][7])*WL3WS[3][0]+float(list2010[l][13])*WL3WS[4][0]+float(list2010[l][14])*WL3WS[5][0])-float(list2010[l][16]);

	for l in range(1,32,1):
		err2 = err2 + (b1WS+float(list2011[l][1])*WL3WS[0][0]+float(list2011[l][3])*WL3WS[1][0]+float(list2011[l][5])*WL3WS[2][0]+float(list2011[l][7])*WL3WS[3][0]+float(list2011[l][13])*WL3WS[4][0]+float(list2011[l][14])*WL3WS[5][0])-float(list2011[l][16]);

	for l in range(1,32,1):
		err3 = err3 + (b1WS+float(list2012[l][1])*WL3WS[0][0]+float(list2012[l][3])*WL3WS[1][0]+float(list2012[l][5])*WL3WS[2][0]+float(list2012[l][7])*WL3WS[3][0]+float(list2012[l][13])*WL3WS[4][0]+float(list2012[l][14])*WL3WS[5][0])-float(list2012[l][16]);

	for l in range(1,32,1):
		err4 = err4 + (b1WS+float(list2013[l][1])*WL3WS[0][0]+float(list2013[l][3])*WL3WS[1][0]+float(list2013[l][5])*WL3WS[2][0]+float(list2013[l][7])*WL3WS[3][0]+float(list2013[l][13])*WL3WS[4][0]+float(list2013[l][14])*WL3WS[5][0])-float(list2013[l][16]);

	for l in range(1,32,1):
		err5 = err5 + (b1WS+float(list2014[l][1])*WL3WS[0][0]+float(list2014[l][3])*WL3WS[1][0]+float(list2014[l][5])*WL3WS[2][0]+float(list2014[l][7])*WL3WS[3][0]+float(list2014[l][13])*WL3WS[4][0]+float(list2014[l][14])*WL3WS[5][0])-float(list2014[l][16]);

	for l in range(1,32,1):
		err6 = err6 + (b1WS+float(list2015[l][1])*WL3WS[0][0]+float(list2015[l][3])*WL3WS[1][0]+float(list2015[l][5])*WL3WS[2][0]+float(list2015[l][7])*WL3WS[3][0]+float(list2015[l][13])*WL3WS[4][0]+float(list2015[l][14])*WL3WS[5][0])-float(list2015[l][16]);
		
	for l in range(1,32,1):
		err7 = err7 + (b1WS+float(list2016[l][1])*WL3WS[0][0]+float(list2016[l][3])*WL3WS[1][0]+float(list2016[l][5])*WL3WS[2][0]+float(list2016[l][7])*WL3WS[3][0]+float(list2016[l][13])*WL3WS[4][0]+float(list2016[l][14])*WL3WS[5][0])-float(list2016[l][16]);
		
	for l in range(1,32,1):
		err8 = err8 + (b1WS+float(list2017[l][1])*WL3WS[0][0]+float(list2017[l][3])*WL3WS[1][0]+float(list2017[l][5])*WL3WS[2][0]+float(list2017[l][7])*WL3WS[3][0]+float(list2017[l][13])*WL3WS[4][0]+float(list2017[l][14])*WL3WS[5][0])-float(list2017[l][16]);

	for l in range(1,32,1):
		err9 = err9 + (b1WS+float(list2018[l][1])*WL3WS[0][0]+float(list2018[l][3])*WL3WS[1][0]+float(list2018[l][5])*WL3WS[2][0]+float(list2018[l][7])*WL3WS[3][0]+float(list2018[l][13])*WL3WS[4][0]+float(list2018[l][14])*WL3WS[5][0])-float(list2018[l][16]);

	for l in range(1,32,1):
		err10 = err10 + (b1WS+float(list2019[l][1])*WL3WS[0][0]+float(list2019[l][3])*WL3WS[1][0]+float(list2019[l][5])*WL3WS[2][0]+float(list2019[l][7])*WL3WS[3][0]+float(list2019[l][13])*WL3WS[4][0]+float(list2019[l][14])*WL3WS[5][0])-float(list2019[l][16]);

	for l in range(1,32,1):
		err11 = err11 + (b1WS+float(list2020[l][1])*WL3WS[0][0]+float(list2020[l][3])*WL3WS[1][0]+float(list2020[l][5])*WL3WS[2][0]+float(list2020[l][7])*WL3WS[3][0]+float(list2020[l][13])*WL3WS[4][0]+float(list2020[l][14])*WL3WS[5][0])-float(list2020[l][16]);

	for l in range(1,32,1):
		err12 = err12 + (b1WS+float(list2021[l][1])*WL3WS[0][0]+float(list2021[l][3])*WL3WS[1][0]+float(list2021[l][5])*WL3WS[2][0]+float(list2021[l][7])*WL3WS[3][0]+float(list2021[l][13])*WL3WS[4][0]+float(list2021[l][14])*WL3WS[5][0])-float(list2021[l][16]);

	for l in range(1,32,1):
		err13 = err13 + (b1WS+float(list2022[l][1])*WL3WS[0][0]+float(list2022[l][3])*WL3WS[1][0]+float(list2022[l][5])*WL3WS[2][0]+float(list2022[l][7])*WL3WS[3][0]+float(list2022[l][13])*WL3WS[4][0]+float(list2022[l][14])*WL3WS[5][0])-float(list2022[l][16]);	

	errr = abs(err1)+abs(err2)+abs(err3)+abs(err4)+abs(err5)+abs(err6)+abs(err7)+abs(err8)+abs(err9)+abs(err10)+abs(err11)+abs(err12)+abs(err13)
	errr = errr/403;
	#err = abs(err);
	#print(errr);
	#rate = rate/1.05;


print("=======================================================================");	#這裡做風速輸出
print("err of max windspeed in Taiwan is %.4f"%(errr));
for l in range(1,32,1):
	errWS = errWS  + (b1WS+float(list2010[l][1])*WL3WS[0][0]+float(list2010[l][3])*WL3WS[1][0]+float(list2010[l][5])*WL3WS[2][0]+float(list2010[l][7])*WL3WS[3][0]+float(list2010[l][13])*WL3WS[4][0]+float(list2010[l][14])*WL3WS[5][0])-float(list2010[l][16]);
errWS  = errWS /31;
print("err of max windspeed in 基隆 is %.4f"%(errWS));

for l in range(1,32,1):
	errWS = errWS  + (b1WS+float(list2011[l][1])*WL3WS[0][0]+float(list2011[l][3])*WL3WS[1][0]+float(list2011[l][5])*WL3WS[2][0]+float(list2011[l][7])*WL3WS[3][0]+float(list2011[l][13])*WL3WS[4][0]+float(list2011[l][14])*WL3WS[5][0])-float(list2011[l][16]);
errWS  = errWS /31;
print("err of max windspeed in 台北 is %.4f"%(errWS));

for l in range(1,32,1):
	errtm = errtm  + (b1WS+float(list2012[l][1])*WL3WS[0][0]+float(list2012[l][3])*WL3WS[1][0]+float(list2012[l][5])*WL3WS[2][0]+float(list2012[l][7])*WL3WS[3][0]+float(list2012[l][13])*WL3WS[4][0]+float(list2012[l][14])*WL3WS[5][0])-float(list2012[l][16]);
errWS  = errWS /31;
print("err of max windspeed in 桃園 is %.4f"%(errWS));

for l in range(1,32,1):
	errWS = errWS  + (b1WS+float(list2013[l][1])*WL3WS[0][0]+float(list2013[l][3])*WL3WS[1][0]+float(list2013[l][5])*WL3WS[2][0]+float(list2013[l][7])*WL3WS[3][0]+float(list2013[l][13])*WL3WS[4][0]+float(list2013[l][14])*WL3WS[5][0])-float(list2013[l][16]);
errWS  = errWS /31;
print("err of max windspeed in 新竹 is %.4f"%(errWS));

for l in range(1,32,1):
	errWS = errWS  + (b1WS+float(list2014[l][1])*WL3WS[0][0]+float(list2014[l][3])*WL3WS[1][0]+float(list2014[l][5])*WL3WS[2][0]+float(list2014[l][7])*WL3WS[3][0]+float(list2014[l][13])*WL3WS[4][0]+float(list2014[l][14])*WL3WS[5][0])-float(list2014[l][16]);
errWS  = errWS /31;
print("err of max windspeed in 台中 is %.4f"%(errWS));

for l in range(1,32,1):
	errWS = errWS  + (b1WS+float(list2015[l][1])*WL3WS[0][0]+float(list2015[l][3])*WL3WS[1][0]+float(list2015[l][5])*WL3WS[2][0]+float(list2015[l][7])*WL3WS[3][0]+float(list2015[l][13])*WL3WS[4][0]+float(list2015[l][14])*WL3WS[5][0])-float(list2015[l][16]);
errWS  = errWS /31;
print("err of max windspeed in 嘉義 is %.4f"%(errWS));

for l in range(1,32,1):
	errWS = errWS  + (b1WS+float(list2016[l][1])*WL3WS[0][0]+float(list2016[l][3])*WL3WS[1][0]+float(list2016[l][5])*WL3WS[2][0]+float(list2016[l][7])*WL3WS[3][0]+float(list2016[l][13])*WL3WS[4][0]+float(list2016[l][14])*WL3WS[5][0])-float(list2016[l][16]);
errWS  = errWS /31;
print("err of max windspeed in 台南 is %.4f"%(errWS));

for l in range(1,32,1):
	errWS = errWS  + (b1WS+float(list2017[l][1])*WL3WS[0][0]+float(list2017[l][3])*WL3WS[1][0]+float(list2017[l][5])*WL3WS[2][0]+float(list2017[l][7])*WL3WS[3][0]+float(list2017[l][13])*WL3WS[4][0]+float(list2017[l][14])*WL3WS[5][0])-float(list2017[l][16]);
errWS  = errWS /31;
print("err of max windspeed in 高雄 is %.4f"%(errWS));

for l in range(1,32,1):
	errWS = errWS  + (b1WS+float(list2018[l][1])*WL3WS[0][0]+float(list2018[l][3])*WL3WS[1][0]+float(list2018[l][5])*WL3WS[2][0]+float(list2018[l][7])*WL3WS[3][0]+float(list2018[l][13])*WL3WS[4][0]+float(list2018[l][14])*WL3WS[5][0])-float(list2018[l][16]);
errWS  = errWS /31;
print("err of max windspeed in 屏東 is %.4f"%(errWS));

for l in range(1,32,1):
	errWS = errWS  + (b1WS+float(list2019[l][1])*WL3WS[0][0]+float(list2019[l][3])*WL3WS[1][0]+float(list2019[l][5])*WL3WS[2][0]+float(list2019[l][7])*WL3WS[3][0]+float(list2019[l][13])*WL3WS[4][0]+float(list2019[l][14])*WL3WS[5][0])-float(list2019[l][16]);
errWS  = errWS /31;
print("err of max windspeed in 台東 is %.4f"%(errWS));

for l in range(1,32,1):
	errWS = errWS  + (b1WS+float(list2020[l][1])*WL3WS[0][0]+float(list2020[l][3])*WL3WS[1][0]+float(list2020[l][5])*WL3WS[2][0]+float(list2020[l][7])*WL3WS[3][0]+float(list2020[l][13])*WL3WS[4][0]+float(list2020[l][14])*WL3WS[5][0])-float(list2020[l][16]);
errWS  = errWS /31;
print("err of max windspeed in 花蓮 is %.4f"%(errWS));

for l in range(1,32,1):
	errWS = errWS  + (b1WS+float(list2021[l][1])*WL3WS[0][0]+float(list2021[l][3])*WL3WS[1][0]+float(list2021[l][5])*WL3WS[2][0]+float(list2021[l][7])*WL3WS[3][0]+float(list2021[l][13])*WL3WS[4][0]+float(list2021[l][14])*WL3WS[5][0])-float(list2021[l][16]);
errWS  = errWS /31;
print("err of max windspeed in 宜蘭 is %.4f"%(errWS));

for l in range(1,32,1):
	errWS = errWS  + (b1WS+float(list2022[l][1])*WL3WS[0][0]+float(list2022[l][3])*WL3WS[1][0]+float(list2022[l][5])*WL3WS[2][0]+float(list2022[l][7])*WL3WS[3][0]+float(list2022[l][13])*WL3WS[4][0]+float(list2022[l][14])*WL3WS[5][0])-float(list2022[l][16]);
errWS  = errWS /31;
print("err of max windspeed in 日月潭 is %.4f"%(errWS));

for l in range(1,32,1):
	sum=b1WS+(float(list2011[l][1])*WL3WS[0][0]+float(list2011[l][3])*WL3WS[1][0]+float(list2011[l][5])*WL3WS[2][0]+float(list2011[l][7])*WL3WS[3][0]+float(list2011[l][13])*WL3WS[4][0]+float(list2011[l][14])*WL3WS[5][0]);
	print("windspeed in 台北 day%.0f is %.4f"%(l,sum));
