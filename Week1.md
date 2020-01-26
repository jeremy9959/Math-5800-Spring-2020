## Goals for January 27 - February 3

To summarize, the goals for this week are:

- [to form some preliminary working groups](#groups)
- [for each participant to create a github site](#github)
- [to create an initial list of resources and references and document them on that site](#references)

There is also a reading assignment:

[What is data science? Chapter 1 of Doing Data Science by O'Neill and Schutt](https://learning.oreilly.com/library/view/doing-data-science/9781449363871/ch01.html).  UConn NetID required -- Available through the UConn Library.


### <a name="groups"></a> Form some preliminary working groups



As we learned last week, people in the class have diverse interests.  Reading over my notes
I can identify a few topic area themes that people are interested in.  These included:

- using satellite image data to identify world hot spots
- using medical imaging to diagnose cancer
- using machine learning to identify art forgeries
- teaching computers to win at games
- finding signals in the genome that control transcription of different proteins
- using machine learning to translate EEG data to motion control of devices such as wheelchairs
- integrating information from the news with financial data to make predictions

As the skills and interests whiteboards show, we have a mixture of expertise, with some relative newcomers
to machine learning in the course, and some people with a lot of math background, along with some relative
newcomers.  

The first goal for this week is **to form preliminary working groups.**  We've all had some opportunity
to hear from other class members about their interests.  I suggest that these initial groups be organized
around broad application areas -- so that, for instance, several people interested in working with images
can form a group, even if they have different particular applications in mind.   

These groups are preliminary, you're not committing yourself to a joint project for the semester.  I recommend
shooting for 3-4 people. I'm not much for social engineering so if you'd prefer to work alone, that's ok.  It is a fact of life, however, that industry and academic work in data science/machine learning is a team sport.

Bottom line is that **by Wednesday, January 28** I'd like to know who is working together to start.



### <a name="github"></a>Create GitHub sites 

[GitHub](http://www.github.com) is a website (really a cloud services provider) that was created to support large open-source software development projects.  [Recently acquired by Microsoft](https://news.microsoft.com/2018/06/04/microsoft-to-acquire-github-for-7-5-billion/), it is a key source for making and sharing software and documentation.  

My github profile is [here](https://github.com/jeremy9959).  It consists of some profile information plus
a bunch of *repositories*, each of which contains code or documents related to a  projects I am (or was)  working on 
(in widely varying states of completion). 

One of the repositories is the source code for the
[website for this course](https://github.com/jeremy9959/Math-5800-Spring-2020) and I use GitHub to generate
the [jeremy9959.net page](http://jeremy9959.net) automatically.  Making web pages using GitHub
is pretty easy but we'll save that for later.

The backend of the GitHub site is the software tool called [git](https://git-scm.com).  Git is a beautiful piece
of software that allows you to track versions of your work, undo changes, make experiments without messing up stuff
that works, and collaborate with others.  It is just as useful for working on shared documents (like joint papers)
as it is for software.  

To elaborate a little, you would use [git](https://git-scm.com) to control manage the files in a directory on
your computer, to keep track of changes and make checkpoints so you can get back to a working state if you mess
up your project.  With [GitHub](http://github.com) you can reproduce your directory in the cloud, share it with others,
and also have a backup in case something happens to your local machine.  There are other cloud providers
that do things like [GitHub](http://github.com), such as [GitLab](http://gitlab.com), but [GitHub](http://github.com)
is the biggest and best known.

Knowing the basics of how to use git and GitHub is a baseline skill for any scientist -- or anyone wanting to work in a technical field in industry.  Therefore:

**The second goal for this week** is for everyone in the class to have a GitHub site and a repository associated with
their project for this course.  



To install Git on a Mac or Linux machine, you can use the downloads from the [git](http://www.git-scm.com) site.
**For Windows** I  recommend using the [gitforwindows](https://gitforwindows.org) version, which 
also installs a command line shell (git-bash) that works well with git.  
Alternatively you can install [GitHub Desktop](http://desktop.github.com) which gives you a git-shell 
that also works well on windows.

For some of you this may take 15 minutes, but if you are new to Git and GitHub, here are some references:

- [Git-it](https://github.com/jlord/git-it-electron) is an app that walks you through the basics.  It's fun
and worth a try.  
- [Git Hello World](https://guides.github.com/activities/hello-world/) walks you through making a repository
on the GitHub site without using your local computer.
- [Git Handbook](https://guides.github.com/introduction/git-handbook/) is an overview of of Git with some discussion
of how it relates to GitHub.
- [This udacity walkthrough](https://blog.udacity.com/2015/06/a-beginners-git-github-tutorial.html) looks like a good
introduction, if you can stand the upselling.
- Ask for help from someone who knows what they are doing (a classmate, a friend, or if all else fails me!)

### <a name="references"></a> Collect Examples and References

The final goal for this week is **to begin a library of examples and references** related to the general
area your group is interested in, and to document that library in your github site in the README file.

You can see my example of this for my (hypothetical) twitter project in [my demo github repo](http://github.com/jeremy9959/Math5800-JTT-Demo).

This is essentially a google/library research project. 
A reasonable goal is 6-10 references of at least three different types.  You should provide a brief
indication of what the reference contains.  These links are supposed to be useful to you so don't 
just blindly copy them.

The types I have in mind include:

- Published scholarly articles from journals or conference proceedings. You can identify them because they have references to the journal or conference. They are typically quite condensed and  rather technical, but they sometimes give details not available elsewhere. It's *very important* to consider the place the article was published or the conference where the work was presented in deciding whether the work is likely to be useful - you can get anything published somewhere, especially in this field. 

	A premiere conference in neural networks is [NIPS](https://papers.nips.cc/) (Neural Information Processing Systems) and a 
	lot of breakthroughs appear in its proceedings. One such is the 2012 paper by Krizhevsky, Suskever, and Hinton called [ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf), which demonstrated the feasibility of training huge neural networks to do image classification on massive scale. This paper has 55500 citations on google scholar, or roughly 7000 per year since publication.    The [Journal of Machine Learning Research](http://www.jmlr.org/) is a premier journal in this field, where for example this breakthrough paper [Visualizing Data with t-SNE](http://www.jmlr.org/papers/volume9/vandermaaten08a/vandermaaten08a.pdf) describing the now widely used t-sne algorithm for clustering was described.  It 'only' has 11500 citations since 2008.

- Arxiv preprints.  The Arxiv is a preprint server in the sciences -- it's the same resource used by mathematicians. It's
unrefereed so it has the advantage that you get quick access to results and it has the disadvantage that it has no
barrier to entry.  A search for *neural networks* revealed something like 75 hits published in a two day period 
last week, so it's a flood of stuff.

- Blog posts, tutorials, and self-published articles.  Two big aggregators that come up in these searches are [Medium](http://www.medium.com) and [TowardsDataScience](https://towardsdatascience.com/).  The articles that appear here are sometimes very useful, 
and include very practical, step by step instructions on how to do things. For example, I found this article
on the [visualization tool bokeh](https://towardsdatascience.com/data-visualization-with-bokeh-in-python-part-one-getting-started-a11655a467d4) very helpful and clearly written.  But beware, because anyone can publish in these settings.

- Tutorials from software packages.  These will walk you through how to do basic things in a particular language so you can learn to use that package.  Useful for the intended purpose.

- Coursera, Udemy, Udacity, and other MOOC providers.  Can be very well done and systematic, but
can be VERY expensive and sometimes rather general.

- Course notes from other university courses.  These can be very useful and given you all the detailed stuff you wish I was
giving you.  For example, the famous [Stanford CS229](http://http://cs229.stanford.edu/)  course website has examples
of [projects](http://cs229.stanford.edu/projects.html) done by students in that class going back years.

- Software, usually on GitHub.  For example, I mentioned that I was interested in scraping data from [twitter](http://twitter.com).  I googled "scrape twitter data python" and found this blog post: [How to Scrape Tweets from Twitter](https://towardsdatascience.com/how-to-scrape-tweets-from-twitter-59287e20f0f1). That blog post referred me to the software package
[tweepy](http://www.tweepy.org).  From there I could read the tweepy documentation AND find the [tweepy github site](https://github.com/tweepy/tweepy) where I can look at all the source code.

#### Where should I end up?

Here is my [demo github repository for my hypothetical twitter project](https://github.com/jeremy9959/Math5800-JTT-Demo/blob/master/README.md).
















