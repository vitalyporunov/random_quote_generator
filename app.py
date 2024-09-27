from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for Flask session handling

# Sample quotes list
quotes = [
    "Be yourself; everyone else is already taken. – Oscar Wilde",
    "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. – Albert Einstein",
    "So many books, so little time. – Frank Zappa",
    "A room without books is like a body without a soul. – Marcus Tullius Cicero",
    "Be the change that you wish to see in the world. – Mahatma Gandhi",
    "In three words I can sum up everything I've learned about life: it goes on. – Robert Frost",
    "If you tell the truth, you don't have to remember anything. – Mark Twain",
    "Without music, life would be a mistake. – Friedrich Nietzsche",
    "We accept the love we think we deserve. – Stephen Chbosky",
    "The only way out of the labyrinth of suffering is to forgive. – John Green",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky",
    "Success is not how high you have climbed, but how you make a positive difference to the world. – Roy T. Bennett",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. – Ralph Waldo Emerson",
    "Happiness is not something ready-made. It comes from your own actions. – Dalai Lama",
    "You only live once, but if you do it right, once is enough. – Mae West",
    "Be the hero of your own story. – Joe Rogan",
    "It is never too late to be what you might have been. – George Eliot",
    "What we think, we become. – Buddha",
    "All our dreams can come true, if we have the courage to pursue them. – Walt Disney",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The best revenge is massive success. – Frank Sinatra",
    "Act as if what you do makes a difference. It does. – William James",
    "An unexamined life is not worth living. – Socrates",
    "To live is the rarest thing in the world. Most people exist, that is all. – Oscar Wilde",
    "The purpose of our lives is to be happy. – Dalai Lama",
    "Doubt kills more dreams than failure ever will. – Suzy Kassem",
    "Happiness depends upon ourselves. – Aristotle",
    "Go confidently in the direction of your dreams. Live the life you have imagined. – Henry David Thoreau",
    "It always seems impossible until it’s done. – Nelson Mandela",
    "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. – Buddha",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. – Ralph Waldo Emerson",
    "Keep your face always toward the sunshine—and shadows will fall behind you. – Walt Whitman",
    "Challenges are what make life interesting, and overcoming them is what makes life meaningful. – Joshua J. Marine",
    "You must be the change you wish to see in the world. – Mahatma Gandhi",
    "To succeed in life, you need two things: ignorance and confidence. – Mark Twain",
    "Opportunities don't happen. You create them. – Chris Grosser",
    "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
    "Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs",
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "The biggest adventure you can take is to live the life of your dreams. – Oprah Winfrey",
    "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
    "In the middle of every difficulty lies opportunity. – Albert Einstein",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "Everything you’ve ever wanted is on the other side of fear. – George Addair",
    "Dream big and dare to fail. – Norman Vaughan",
    "The secret of getting ahead is getting started. – Mark Twain",
    "The harder you work for something, the greater you'll feel when you achieve it. – Unknown",
    "Don't stop when you're tired. Stop when you're done. – Unknown",
    "It's not whether you get knocked down, it's whether you get up. – Vince Lombardi",
    "You don't have to be great to start, but you have to start to be great. – Zig Ziglar",
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "If you are working on something that you really care about, you don’t have to be pushed. The vision pulls you. – Steve Jobs",
    "The only place where success comes before work is in the dictionary. – Vidal Sassoon",
    "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. – James Cameron",
    "Don’t be afraid to give up the good to go for the great. – John D. Rockefeller",
    "It always seems impossible until it’s done. – Nelson Mandela",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. – Zig Ziglar",
    "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
    "The only thing standing between you and your goal is the story you keep telling yourself as to why you can’t achieve it. – Jordan Belfort",
    "You don't always need a plan. Sometimes you just need to breathe, trust, let go, and see what happens. – Mandy Hale",
    "The question isn’t who is going to let me; it’s who is going to stop me. – Ayn Rand",
    "Great things never came from comfort zones. – Neil Strauss",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt",
    "Don’t be afraid to give up the good to go for the great. – John D. Rockefeller",
    "Success is walking from failure to failure with no loss of enthusiasm. – Winston Churchill",
    "Fall seven times and stand up eight. – Japanese Proverb",
    "The man who has confidence in himself gains the confidence of others. – Hasidic Proverb",
    "A champion is defined not by their wins, but by how they can recover when they fall. – Serena Williams",
    "Whether you think you can or think you can’t, you’re right. – Henry Ford",
    "Don’t wish it were easier. Wish you were better. – Jim Rohn",
    "Work like there is someone working twenty-four hours a day to take it all away from you. – Mark Cuban",
    "There are no shortcuts to any place worth going. – Beverly Sills",
    "Be so good they can’t ignore you. – Steve Martin",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "It’s not about how bad you want it. It’s about how hard you’re willing to work for it. – Unknown",
    "I find that the harder I work, the more luck I seem to have. – Thomas Jefferson",
    "Opportunities don’t happen, you create them. – Chris Grosser",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Do one thing every day that scares you. – Eleanor Roosevelt",
    "Don't be pushed by your problems. Be led by your dreams. – Ralph Waldo Emerson",
    "When everything seems to be going against you, remember that the airplane takes off against the wind, not with it. – Henry Ford",
    "I would rather die of passion than of boredom. – Vincent van Gogh",
    "Strive not to be a success, but rather to be of value. – Albert Einstein",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. – Nelson Mandela",
    "I have not failed. I've just found 10,000 ways that won't work. – Thomas Edison",
    "Success is the sum of small efforts, repeated day in and day out. – Robert Collier",
    "If you want to lift yourself up, lift up someone else. – Booker T. Washington",
    "If you're not willing to risk the usual, you will have to settle for the ordinary. – Jim Rohn",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. – Christian D. Larson",
    "The most effective way to do it, is to do it. – Amelia Earhart",
    "If you want to achieve greatness stop asking for permission. – Unknown",
    "If opportunity doesn’t knock, build a door. – Milton Berle",
]

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Random quote route
@app.route('/quotes')
def show_quotes():
    random_quote = random.choice(quotes)
    return render_template('quotes.html', quote=random_quote)

# Route to mark a quote as favorite
@app.route('/favorite/<quote>')
def favorite_quote(quote):
    if 'favorites' not in session:
        session['favorites'] = []
    
    favorites = session['favorites']
    
    if quote not in favorites:
        favorites.append(quote)
        session['favorites'] = favorites  # Save to session
    return redirect(url_for('show_favorites'))

# Display favorite quotes
@app.route('/favorites')
def show_favorites():
    favorites = session.get('favorites', [])
    return render_template('favorites.html', favorites=favorites)

# Submit a new quote
@app.route('/submit', methods=['GET', 'POST'])
def submit_quote():
    if request.method == 'POST':
        new_quote = request.form['quote']
        if new_quote:
            quotes.append(new_quote)
            return redirect(url_for('show_quotes'))
    return render_template('submit.html')

# About route
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
