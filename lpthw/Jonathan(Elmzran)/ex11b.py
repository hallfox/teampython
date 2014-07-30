print "What is your favorite book?",
fav_book = raw_input()
print "Who is your favorite author?",
fav_author = raw_input()
print "What is your favorite book genre?",
fav_genre = raw_input()
print "How many books do you read a month on average?",
book_number = int(raw_input())

print "So, your favorite book is %s, favorite author is %s, and favorite genre is %s." % (
	fav_book, fav_author, fav_genre)
print "You also read %d books per month on average." % book_number