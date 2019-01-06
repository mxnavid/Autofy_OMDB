import json
import requests


# Return JSON Info of Movie (1 API Request)
def getMovieJSON(imdbID):
	movieLink = "http://www.omdbapi.com/?i=" + str(imdbID)+ "&apikey=KEYYYYYYYYY"
	resp = requests.get(url=movieLink)
	data = resp.json()
	return data

# Return parsed JSON
def handleJSON(jsonData):
	dumpJSON = json.dumps(jsonData)
	parsedJSON = json.loads(dumpJSON)
	return parsedJSON


def getTitle(data):
	dst = data['Title']
	dst = dst.replace(".", "_")
	dst = dst.replace(":", "_")
	dst = dst.replace("'","")
	return dst
	


def getYear(data):
	return (data['Year'])


def getCountry(data):
	return (data['Country'])

def getDuration(data):
	startRemoving = " min"
	time = (data['Runtime'])
	finalTime = time.split(startRemoving,1)[0] # Extracts the Value in Mins Only
	return finalTime	


def getDirector(data):
	return (data['Director'])

def getActors(data):
	return (data['Actors'])

def getDescription(data):
	return (data['Plot'])

def main():
	data = getMovieJSON('tt3104988')
	parsed = handleJSON(data)
	print(getTitle(parsed))
	print(getYear(parsed))
	print(getCountry(parsed))
	print(getDuration(parsed))
	print(getDirector(parsed))
	print(getActors(parsed))
	print(getDescription(parsed))

	title = getTitle(parsed)
	year = getYear(parsed)
	country = getYear(parsed)
	

	movieInfo = [title, year, ]


if __name__ == "__main__":
	main()