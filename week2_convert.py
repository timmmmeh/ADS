def convert(string):
	string_and_int = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6, '7':7, '8':8, '9':9}
	if(len(string) == 1):
		return string_and_int[string]
	else
		return convert(string[-1]) + (convert[:-1] * 10)

