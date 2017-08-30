from os import path
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

class EventCloud(WordCloud):
    def __init__(self, image_name="girl.jpg", png_path="./cloudpng/", data_path="./datacount"):
        self.image_name = image_name
        self.png_path = png_path
        self.data_path = data_path

    def to_png(self, data, filename="example"):
        d = path.dirname(__file__)
        girl_coloring = imread(path.join(d, self.image_name))
        wc = WordCloud(
                font_path='simsun.ttc',
                background_color="white",
                max_words=3000,
                mask=girl_coloring,
                max_font_size=1000,
                random_state=50,
                width=800,
                height=400
        )

        # generate word cloud
        # wc.generate(text)
        wc.generate_from_frequencies(data)

        # generate color from image
        image_colors = ImageColorGenerator(girl_coloring)
        wc.to_file(path.join(self.png_path+filename+".png"))
