from django.shortcuts import render

def home(request):
	template = "home.html"
	context = {
		"title": "Guess Your Favorite Animal"
	}
	return render(request, template, context)

def car(request):
	template = "car.html"
	context = {
		"title": "Which is your favorite car?"
	}
	return render(request, template, context)

def piano(request):
	template = "piano.html"
	context = {
		"title": "Which is your favorite piano?"
	}
	return render(request, template, context)

def plant(request):
	template = "plant.html"
	context = {
		"title": "Which is your favorite plant?"
	}
	return render(request, template, context)

def country(request):
	template = "country.html"
	context = {
		"title": "Which is your favorite country?"
	}
	return render(request, template, context)

def london(request):
	template = "london.html"
	context = {
		"title": "!!ERROR!!",
		"statement": "London is a city, not a country!"
	}
	return render(request, template, context)

def sarawak(request):
	template = "sarawak.html"
	context = {
		"title": "!!ERROR!!",
		"statement": "Sarawak is a state, not a country!"
	}
	return render(request, template, context)

def cartoon(request):
	template = "cartoon.html"
	context = {
		"title": "Which is your favorite cartoon?"
	}
	return render(request, template, context)

def videop(request):
	template = "videop.html"
	context = {
		"title": "I like Pink Panther too!\
				Still remember the Pink Panther song?"
	}
	return render(request, template, context)

def videof(request):
	template = "videof.html"
	context = {
		"title": "Yeshhhh Flintstone is the coolest!\
				Especially it's iconic theme song!"
	}
	return render(request, template, context)

def videos(request):
	template = "videos.html"
	context = {
		"title": "Scooooooooobyyydooooooo! Woooohoooohooohooooo!"
	}
	return render(request, template, context)


def preguess(request):
	template = "preguess.html"
	context = {
		"title": "Okay. I think I've already gotten the answer.\
				 Your favorite animal is... ..."
	}
	return render(request, template, context)

def guess(request):
	template = "guess.html"
	context = {
		"title": "Baboon!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	}
	return render(request, template, context)

def pregift(request):
	template = "pregift.html"
	context = {
		"title": "Hahahahahaha! Guess what? I can't actually guess\
				your favorite animal! But that's not the point of \
				this game. The point of this game is that I have \
				something special for you..."
	}
	return render(request, template, context)

def gift(request):
	template = "gift.html"
	context = {
		"title": "Happy Birthday Papa!"
	}
	return render(request, template, context)


