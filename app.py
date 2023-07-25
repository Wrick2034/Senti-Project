from flask import Flask,render_template
import pandas as pd
import senti

# Configuration for the app
app = Flask(__name__)

# Controller for index page
@app.route('/',methods=['GET','POST'])
def index():
    df=pd.read_csv('Restaurant_Reviews.tsv',sep='\t')
    df['sentiment'] = df['Review'].apply(senti.get_sentiment)
    return render_template('index.html',df=df)

if __name__ == "__main__":
    app.debug=True
    app.run()