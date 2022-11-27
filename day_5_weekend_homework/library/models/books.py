from models.book import Book


book1 = Book("Brief Answers to the Big Questions", "Stephen Hawkin", "Autobiography", False, )
book2 = Book("The Power of Now", "Eckhart Tolle", "Self-help", False)
book3 = Book("F**k It, the ultimate spiritual way", "John C. Parking", "Self-help/Psychology", True)

books = [book1, book2, book3]

text1 = "The world-famous cosmologist and #1 bestselling author of A Brief History of Time leaves us with his final thoughts on the universe's biggest questions in this brilliant posthumous work. Is there a God? How did it all begin? Can we predict the future? What is inside a black hole? Is there other intelligent life in the universe? Will artificial intelligence outsmart us? How do we shape the future? Will we survive on Earth? Should we colonise space? Is time travel possible? Throughout his extraordinary career, Stephen Hawking expanded our understanding of the universe and unravelled some of its greatest mysteries. But even as his theoretical work on black holes, imaginary time and multiple histories took his mind to the furthest reaches of space, Hawking always believed that science could also be used to fix the problems on our planet. And now, as we face potentially catastrophic changes here on Earth - from climate change to dwindling natural resources to the threat of artificial super-intelligence - Stephen Hawking turns his attention to the most urgent issues for humankind. Wide-ranging, intellectually stimulating, passionately argued, and infused with his characteristic humour, BRIEF ANSWERS TO THE BIG QUESTIONS, the final book from one of the greatest minds in history, is a personal view on the challenges we face as a human race, and where we, as a planet, are heading next. A percentage of all royalties will go to charity."
text2 = "The bestselling self-help book of its generation - which has now sold over a million copies in the UK alone. Eckhart Tolle demonstrates how to live a healthier and happier life by living in the present moment. To make the journey into The Power of Now we will need to leave our analytical mind and its false created self, the ego, behind. Although the journey is challenging, Eckhart Tolle offers simple language and a question and answer format to show us how to silence our thoughts and create a liberated life. Surrender to the present moment, where problems do not exist. It is here we find our joy, are able to embrace our true selves and discover that we are already complete and perfect. If we are able to be fully present and take each step in the Now we will be opening ourselves to the transforming experience of The Power of Now."
text3 = "'Everyone can relate to F**k It.' - The Times | Saying Fuck It is like a massage for the mind: relaxing you, releasing tension, allowing you to give up on things that aren't working. Just starting to say Fuck It can transform your life. And John C. Parkin argues that saying Fuck It is a spiritual act: that it is the perfect western expression of the eastern ideas of letting go, giving up and finding real freedom by realising that things don't matter so much, if at all. This is the Fuck It way."

texts = [text1, text2, text3]

def add_new_book(new_book):
    books.append(new_book)

def remove_book(book):
    books.remove(book)
