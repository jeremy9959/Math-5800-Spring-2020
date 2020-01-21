# Course Information

## What is this course about

Machine Learning problems fall into two general categories: *supervised* and *unsupervised* learning.  

In supervised learning one starts with a large set of "known data" and
then tries to fit new data into the pattern determined by what's
known.  For example, classifying an image based on a large dataset of
labelled images, or predicting a home price based on a database of
homes and their selling prices, are supervised problems.

In unsupervised learning one seeks to uncover patterns in data *ab
initio.* For one example, given RNA expression data for a large group
of cells, one tries to identify different types of cells that are
similar to each other without knowing in advance how to characterize
cell types.  For another, one might try to extract different
"personality types" from the results of a questionnaire by identifying
groups of people whose answers are similar to each other.  One rather
spectacular type of unsupervised learning is teaching a system to play
a game by having it develop strategies from scratch.

Data Science/Machine Learning is a "hot topic" and the web is filled, not only with a very 
deep scientific literature and powerful 
open source software packages, but also tutorials, blog posts, and entire courses on different
approaches to machine learning.

## Course Overview

The goal of this course is for each student (or, better, each of several small groups of students)
to choose a machine learning problem and dataset and to complete a project that includes the following 
elements:

1. An overview of the problem and how it fits into the general machine learning landscape.
2. Identification of a relevant dataset and a presentation of the notable features of the selected dataset.
3. A choice of approach with justification.
4. An overview of the mathematical foundations of the approach.  This overview should include a more detailed mathematical explanation of at least one aspect of the technique being employed.
5. A fully documented implementation of the approach using available software tools.
6. A report on the conclusions of the project.
	
Depending on your team's strengths and interests, 
you may emphasize different aspects of this project.  For example:

- if you are more interested in the problem of harvesting data from the web (such as images, text, or
social relationships) then you might want to emphasize step 2 and use a simpler algorithm in steps 3-4
to show that the data you've harvested is interesting.

- if you are more interested in the mathematical
foundations of an algorithm, you could *start* with an algorithm and emphasize step 4,
working carefully through the mathematics. Some of the algorithms worth investigating are:

    - Logistic regression. This is an important foundational algorithm for machine learning.
	- Decision Trees. Decision trees, especially "boosted" trees, are widely used in practical applications.
	- Neural Networks.  Neural networks are where many of the most spectacular advances have taken place. The most accessible place to start might be with Convolutional Networks for image classification.
	- Word Vectors.  These are techniques for working with Natural Language; the foundational algorithm is called word2vec.
	- Linear Methods. Support vector machines and other linear classifiers are "classic" machine learning methods that have a lot of interesting associated mathematics.
	- Spectral Methods.  These are techniques for studying graphs
   
	
Fundamentally, machine learning involve minimizing the value of a "loss function" by adjusting parameters.
The most common approach to this is *gradient descent*. 
Another approach to optimization is via *Monte Carlo* methods.  You could focus your project on optimization.

- if you are more interested in implementation, you could focus your efforts on step 5 by developing
a custom implementation of an algorithm.

I expect that the final project will be presented as a git repository with associated gh-pages documentation
for the reports, but we can discuss alternatives to this.

## Course meetings

*I expect regular attendance at class meetings.*

The course meetings will be devoted to progress reports and the sharing of suggestions between groups.
Because we are trying to learn a huge subject in a short time, and because the participants have
varying background, we all have something to contribute.

Each team should be prepared to show some element of their project at each meeting, whether to illustrate progress or to raise a question. 

## Where to look for data

### Kaggle

The [Kaggle](http://kaggle.com) site hosts data science competitions with cash (and other) prizes.  Many of these
competitions are very sophisticated and doing well in them requires expertise and also specialized
technique.  Nevertheless, the kaggle website is a great source of both datasets and ideas for projects,
even if you aren't actually competing.

If you *are* interested in doing one of these competitions, we can talk.

### Other Data Sources

- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php) contains about
500 datasets on all sorts of things for use "by the machine learning
community."

- [CIFAR](https://www.cs.toronto.edu/~kriz/cifar.html) are large sets of labelled images.  CIFAR-10 has 10 classes (like airplane, automobile, bird,...) and 6000 images per class.  CIFAR-100 has 100 classes with 600 images each.

- [80 million tiny images](http://groups.csail.mit.edu/vision/TinyImages/) contains 80 million tiny images that have been used in a variety of interesting projects.

- One can download [Wikipedia](http://wikipedia.org).  Here is a description of
[how to access wikipedia programmatically](https://towardsdatascience.com/wikipedia-data-science-working-with-the-worlds-largest-encyclopedia-c08efbac5f5c).

- [Twitter](https://developer.twitter.com/en/docs)  has an API from which one can extract lots of information. 

- There is a lot of data on sports, for example [NFL Savant](http://nflsavant.com/about.php)
has free tables listing every play in the season.

- The National Institutes of Health has a huge archive of data for those with the expertise to
read it; see [The Cancer Genome Atlas](https://www.cancer.gov/about-nci/organization/ccg/research/structural-genomics/tcga) for example.  

- The [Network Repository](http://networkrepository.com) has a wide range of graphs/networks to study.

### References

The following books are standard references. A project can be built on just one chapter (or section of a chapter!)
of these books.  

- [The Elements of Statistical Learning](https://web.stanford.edu/~hastie/ElemStatLearn/) by Hastie, Tibshirani,
and Friedman.

- [Pattern Recognition and Machine Learning](https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf) by Christopher Bishop.

- [Probabilistic Graphical Models](https://mitpress.mit.edu/books/probabilistic-graphical-models) by Koller and Friedman.

It's also worth knowing that one can access the *entire* O'Reilly Library through the UConn Library.  

 





	
	
