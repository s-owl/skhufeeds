from crawlers.models import Source, NewsFeed
import datetime

src1 = Source()
src1.name = "NYT"
src1.url = "https://www.nytimes.com/"
src1.desc = "The New York Times"
src1.save()

feed1_1 = NewsFeed()
feed1_1.time = datetime.datetime.utcnow()
feed1_1.title = "Example Article"
feed1_1.summary = "Example Article Summary"
feed1_1.url = "https://nyti.ms/2uZFtPE"
feed1_1.source = src1
feed1_1.save()

feed1_2 = NewsFeed()
feed1_2.time = datetime.datetime.utcnow()
feed1_2.title = "Example Article 2"
feed1_2.summary = "Example Article Summary 2"
feed1_2.url = "https://nyti.ms/2v2Qznb"
feed1_2.source = src1
feed1_2.save()

src2 = Source()
src2.name = "Engadget"
src2.url = "https://www.engadget.com/"
src2.desc = "The original home for technology news and reviews"
src2.save()

feed2_1 = NewsFeed()
feed2_1.time = datetime.datetime.utcnow()
feed2_1.title = "Example Article"
feed2_1.summary = "Example Article Summary"
feed2_1.url = "https://www.engadget.com/video/59947aab83b51f47e16392ce"
feed2_1.source = src2
feed2_1.save()

feed2_2 = NewsFeed()
feed2_2.time = datetime.datetime.utcnow()
feed2_2.title = "Example Article 2"
feed2_2.summary = "Example Article Summary 2"
feed2_2.url = "https://www.engadget.com/2017/08/16/your-timely-reminder-not-all-hacking-requires-a-computer/"
feed2_2.source = src2
