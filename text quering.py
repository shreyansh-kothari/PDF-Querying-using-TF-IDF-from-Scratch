#!/usr/bin/env python
# coding: utf-8

# In[1]:


DM='''CSE3019 Data Mining L T P J C 2 0 2 4 4 
Version : 1.00 Pre-requisite: None 
 
Course Objectives:  To introduce the concept of Data Mining and Data Preprocessing  To provide the skills required to  handle large data sets  To develop the knowledge for application of the mining algorithms for association, clustering.  To introduce the algorithms for mining data streams   To explain the features of recommendation engine 
 
Expected Outcomes: The student will be able to  To design  Data mining algorithms for real world applications  To evaluate the performance of the various Data Mining algorithms  Analyze and leverage data for real-time decision making 
 
Student Learning Outcomes (SLO): 2, 7, 14, 17 
 
Module:1 INTRODUCTION 3 Hours SLO:2, 7 Data Mining – Data ware housing-OLAP-Data Preprocessing 
 
Module:2 CLASSIFICATION TECHNIQUES AND FINDING SIMILAR ITEMS 
5 Hours SLO:7, 17 
Classification Techniques: Decision Tree,ID3,K-Nearest Neighbour Classifier, Naive Bayes- Near Neighbour Search – Shingling of Documents - Similarity Preserving – Locality Sensitive Hashing (LSH)  –Application and Variance  of LSH – Distance Measures – High degrees of similarity 
 
Module:3 MINING DATA STREAMS 4 Hours SLO:7, 17 Stream Data model - Sampling Data in a Stream – Filtering Streams – Counting distinct elements in a stream – Estimating Moments – Counting Ones in a window – Decaying windows  
 
Module:4 LINK ANALYSIS 4 Hours SLO: 7, 17 Page Rank – Link Spam – Hubs and Authorities  
 
Module:5 FREQUENT ITEM SETS 4 Hours SLO: 7, 17 Market-Basket Model – A-priori Algorithm – Handling larger datasets – Counting Frequent items in a stream – Limited Pass Algorithms  
 
Module:6 CLUSTERING 4 Hours SLO: 7, 17 Hierarchical Clustering – K-means Algorithm – Clustering in Non-Euclidean spaces, Clustering for Streams and Parallelism -  
 
Module:7 RECOMMENDATION SYSTEMS 4 Hours SLO: 7, 17 Content based – Collaborative Filtering – Dimensionality reduction-Case study 
 
Module:8 CONTEMPORARY ISSUES (To be handled by experts from industry) 
2 Hours SLO: 2 
 
 Total Lecture: 30 Hours  
 
 
Text Book: 1. Ian H. Witten, Eibe Frank, Mark A. Hall, Data Mining: Practical Machine Learning Tools and Techniques, Morgan Kaufmann , 2011 Reference Books: 1. Jiawei Han, Micheline Kamber and Jian Pei, Data Mining: Concepts and Techniques,  Morgan Kaufmann  2011 2. J. Leskovec, A. Rajaraman, and Jeffrey D. Ullman. Mining of Massive Datasets. Cambridge University Press, 2014. 
 
   SLO: 17 Project  # Generally a team project [3 to 4 members] # Concepts studied in XXXX should have been used # Down to earth application and innovative idea should have been attempted # Report in Digital format with all drawings using software package to be submitted. [Ex. 1. Design of a traffic light system using sequential circuits OR 2. Design of digital clock]  # Assessment on a continuous basis with a min of 3 reviews. 
 
//Available online data sources may be used for exploring the following projects:  For example: Kaggle, UCI repository, kdnuggets, UCR Time Series Archive etc. Projects may be given as group projects  
Sample Projects: 1. Using a programming language that you are familiar with, such as C++ or Java, implement recent frequent/closed/maximal itemset mining algorithms: Compare the performance of each algorithm with various kinds of large data sets. Write a report to analyze the situations (e.g., data size, data distribution, minimal support threshold setting, and pattern density) where one algorithm may perform better than the others, and state why. 2. The DBLP data set (www.informatik.uni-trier.de/_ley/db/) consists of over one million entries of research papers published in computer science conferences and journals. Among these entries, there are a good number of authors that have coauthor relationships.  (a) Propose a method to efficiently mine a set of coauthor relationships that are closely correlated (e.g., often coauthoring papers together). (b) Based on the mining results and the pattern evaluation measures, discuss which measure may convincingly uncover close collaboration patterns better than others. (c) Based on the study in (a), develop a method that can roughly predict advisor and advisee relationships and the approximate period for such advisory supervision. 3. Implement the associative classification algorithms and compare the performance of each algorithm with various kinds of large data sets. Write a report to analyze the situations (e.g., data size, data distribution, minimal support threshold setting, and pattern density) where one algorithm may perform better than the others, and state why. 4. Implement fuzzy clustering and probabilistic clustering methods and compare the performance of each algorithm with various kinds of large data sets. Write a report to analyze the situations (e.g., data size, data distribution, pattern density and cluster validity) where one algorithm may perform better than the others, and state why.  5. Implement and compare different outlier detection methods/outlier factors on various kinds of large data sets. Write a report to analyze the situations (e.g., data size, data distribution, pattern density) where one algorithm may perform better than the others, and state why. 6. Using a programming language that you are familiar with, such as C++ or Java, implement recent algorithms for intent mining: Compare the performance of each algorithm with various kinds of large data sets. Write a report to analyze the results where one algorithm may perform better than the others, and state why. 7. Design and implement sentiment analysis algorithm for twitter dataset. Experiment the proposed idea using different classifiers and identify the best classifier for the chosen data set based on different performance measures. 
Design and implement content based, user based and collaborative filtering technique on any benchmark dataset to build a recommender system. Prepare a report based on the performance of different methods to justify the choice of the best recommender system. 
 
Lab    SLO: 14  Indicative List of Experiments: 
 
1. Implementing the classification techniques for real world data sets 2. Implement algorithms for similarity matching  3. Implement algorithms for mining data streams  4. Simulate Page ranking algorithm 5. Design and implement link spam detection  6. Implement A-priori algorithm using MapReduce 7. Clustering in Non-Euclidean spaces 8. Clustering for Streams and Parallelism  9. Design and develop a recommendation engine for the given application 
 
 
 
Date of Approval by the Academic Council 16.03.1'''
WM='''Web Mining    L,T,P,J,C                                                                                        3,0,2,0,4   v.1.1 Objectives  To focus on a detailed overview of the web mining process and its techniques  To Understand the basics of Web search with special emphasis on web Crawling  To understand the basic of indexing and the various type of query processing approaches.  To appreciate the use of machine learning approaches for Web Content Mining  To understand the role of hyper links in web structure mining  To appreciate the various aspects of web usage mining Expected Outcome Upon Completion of the course, the students will be able to  Build a sample search engine using available open source tools  Describe the browser security model in web security  Identify the different components of a web page that can be used for mining  Apply machine learning concepts to web content mining  Implement Page Ranking algorithm and modify the algorithm for mining information  Design a system to harvest information available on the web to build recommender systems  Analyse social media data using appropriate data/web mining techniques  Modify an existing search engine to make it personalized 
 
 
Module  Topics L Hrs SLO 1 INTRODUCTION Introduction of WWW – Architecture of the WWW – Web Document Representation- Web Search Engine – Challenges - Web security overview and concepts, Web application security, Basic web security model -Web Hacking Basics HTTP & HTTPS URL, Web Under the Cover Overview of Java security Reading the HTML source. 
 5 2 2 WEB CRAWLING   Basic Crawler Algorithm: Breadth-First/ depth-First Crawlers, Universal Crawlers- Preferential Crawlers :  Focused Crawlers - Topical Crawlers. 
 5 7, 1 3 INDEXING 5 2 

 
 
 
 
 
 
 
 
 
Static and Dynamic Inverted Index– Index Construction and Index Compression- Latent Semantic Indexing.  Searching using an Inverted Index: Sequential Search - Pattern Matching - Similarity search. 
 
 
 
4 WEB STRUCTURE MINING Link Analysis - Social Network Analysis - Co-Citation and Bibliographic Coupling - Page Rank- Weighted Page Rank- HITS - Community Discovery - Web Graph Measurement and Modelling- Using Link Information for Web Page Classification. 
 
8 7, 1 
5 WEB CONTENT MINING Classification: Decision tree for Text Document- Naive Bayesian Text Classification - Ensemble of Classifiers.  Clustering:  K-means Clustering - Hierarchical Clustering – Markov Models - ProbabilityBased Clustering. Vector Space Model – Latent semantic Indexing – Automatic Topic Extraction from Web Documents. 
 
8 7, 1 
6 WEB USAGE MINING Web Usage Mining - Click stream Analysis - Log Files - Data Collection and Pre-Processing - Data Modelling for Web Usage Mining - The BIRCH Clustering Algorithm - Modelling web user interests using clustering- Affinity Analysis and the A Priori Algorithm – Binning –Web usage mining using Probabilistic Latent Semantic Analysis – Finding User Access Pattern via Latent Dirichlet Allocation Model. 
 
9 7, 1 
7 QUERY PROCESSING Relevance Feedback and Query Expansion - Automatic Local and Global Analysis – Measuring Effectiveness and Efficiency 
 
3 11 
8 Recent Trends  2  Lab (Indicative List of Experiments in the areas of )  
 
1. To develop the Search Engine for retrieval process Develop the search engine  that  crawls, transforms and index information for retrieval and presentation in response to user queries 2. To develop the Crawler based on domains Develop the Web crawlers that can copy all the pages they visit for later processing by a search engine which indexes the downloaded pages so the users can 
60    

 
 
 
 
 
 
 
 
 
search much more efficiently. 3. Extract textual information and Multimedia contents from documents Efficiently extract the related textual information and Multimedia contents from documents using web content, web structure and web usage mining 
 
4. Develop Search engine indexing 
  The indexing helps to optimize speed and performance in finding relevant documents for a search query. Without an index, the search engine would scan every document in the corpus, which would require considerable time and computing power.  5. Increase the efficiency of Sentiment Analysis  and Opinion Mining  
Sentiment Analysis is the process of determining whether a piece of writing is positive, negative or neutral. It’s also known as opinion mining, deriving the opinion or attitude of a speaker. Sentiment analysis aims to determine the attitude of a speaker, writer, or other subject with respect to some topic or the overall contextual polarity or emotional reaction to a document, interaction, or event.  6. Implement the Recommendation System.  A recommender system or a recommendation system  seeks to predict the "rating" or "preference" that a user would give to an item . It includes variety of area like movies, music, news, books, research articles, search queries, social tags, and products in general 
 
7. To implement the effective compression schemes for storing the data using less storage space.  Search engine would scan every document in the corpus through indexing. The indexed documents should be compressed in effective manner. 8. To develop the effective query refinement mechanism based on query algebra.  Query expansion (QE) or refinement is the process of reformulating a seed query to improve retrieval performance. In the context of search engines, query 

 
 
 
 
 
 
 
 
 
expansion involves evaluating a user's input (what words were typed into the search query area) and expanding the search query to match additional documents. 9. Personalize the search engine. A web search engine is a software system that is designed to search for information on the World Wide Web. Personalize the search engine for kids, to list only research articles, image, and so on. 
10.  Personalized Web Search  
        Personalize web search using user-logged search behavior context using  user ids, queries, query terms, urls, url domains and clicks. 
 
11. Consumer Products 
Identify product mentions within a largely user-generated web-based corpus and disambiguate the mentions against a large product catalog using blogs, forums, product review sites, and e-commerce merchants. 
 
12. Large Scale Hierarchical Text Classification Hierarchies are becoming ever more popular for the organization of text documents, particularly on the Web. Web directories and Wikipedia are two examples of such hierarchies. Along with their widespread use comes the need for automated classification of new documents to the categories in the hierarchy. As the size of the hierarchy grows and the number of documents to be classified increases, a number of interesting machine learning problems arise. In particular, it is one of the rare situations where data sparsity remains an issue, despite the vastness of available data: as more documents become available, more classes are also added to the hierarchy, and there is a very high imbalance between the classes at different levels of the hierarchy 13. Company  Web 
Given the data related to current employees and their provisioned access, models can be built that automatically determine access privileges as employees enter and leave roles within a company. These auto-access models seek to minimize the human involvement required to grant or revoke employee access. The model will take an employee's role information and a resource code and will return whether or not 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
access should be granted. 
List of Case Studies: 1. Market -Customer analysis 2. Biological/ DNA sequence analysis 3.  Detecting software bugs 4.  Improving storage performance 5.  Design of structured pattern mining methods 6.  Network alarm pattern mining 7. XML query access pattern analysis 8. System performance 9.  Telecommunication network 10. Financial and Scientific data 11.  Creating adaptive web sites 12.  System improvement 13.   Navigation patterns WEBLOG. 
 
 
Text Books 1. Bing Liu, “ Web Data Mining: Exploring Hyperlinks, Contents, and Usage Data (Data-Centric Systems and Applications)”, Springer; 2nd Edition 2010 2. Zdravko Markov, Daniel T. Larose, “Data Mining the Web: Uncovering Patterns in Web Content, Structure, and Usage”, John Wiley & Sons, Inc., 2012 
 
 
Reference Books 1. Guandong Xu ,Yanchun Zhang, Lin Li, “Web Mining and Social Networking: Techniques and Applications”, Springer; 1st Edition.2010 2. Soumen Chakrabarti, “Mining the Web: Discovering Knowledge from Hypertext Data”, Morgan Kaufmann; edition 2012 3. Adam Schenker, “Graph-Theoretic Techniques for Web Content Mining”, World Scientific Pub Co Inc , 2015 4. Min Song, Yi Fang and Brook Wu, Handbook of research on Text and Web mining technologies, IGI global, information Science Reference – imprint of :IGI publishing, 2011.  

 
 
 
 
 
 
 
 
 
Web  Mining 
 Knowledge Areas that contain topics and learning outcomes covered in the course  
 
Knowledge Area Total Hours of Coverage 
CS: IAS(Information Assurance and Security) 5 CS: IM(Information Management) 13 CS: Intelligent Systems (IS) 27 
 
Body of Knowledge coverage [List the Knowledge Units covered in whole or in part in the course.  If in part, please indicate which topics and/or learning outcomes are covered.  For those not covered, you might want to indicate whether they are covered in another course or not covered in your curriculum at all. This section will likely be the most time-consuming to complete, but is the most valuable for educators planning to adopt the CS2013 guidelines.]  
 
 
KA Knowledge Unit Topics Covered Hours CS: IAS 
 IAS/Web Security  Web security model and its applications  Browser security model  HTTP security extensions 
 5 
CS: IM 
IM/Information Management Concepts 
 Basic information storage and retrieval (IS&R) concepts  Information capture and representation  Supporting human needs: searching, retrieving, linking, browsing, navigating  Analysis and indexing 
 
4 
CS: IM 
IM/Indexing  The impact of indices on query performance  The basic structure of an index  Indexing text  Indexing the web (e.g., web crawling) 
6 

 
 
 
 
 
 
 
 
 
 
CS: IS IS/Basic Search Strategies 
 Uninformed search (breadth-first, depth-first, depth-first with iterative deepening)  Heuristics and informed search 
3 
CS: IS IS/Basic Machine Learning 
• Definition and examples of broad variety of machine learning tasks, including classification • Inductive learning • Simple statistical-based learning, such as Naive Bayesian Classifier, decision trees • The over-fitting problem • Measuring classifier accuracy 
23 
 IS/Advanced Machine Learning 
Learning graphical models (Cross-reference IS/Reasoning under Uncertainty) 
4 
---- ----- ----- ---   Include all the topic here    Total hours   45 Where does the course fit in the curriculum? [In what year do students commonly take the course? Is it compulsory? Does it have prerequisites, required following courses? How many students take it?] 
 
This course is a   Elective Course.   Suitable from 4th semester onwards.  Knowledge of basic mathematics is essential. What is covered in the course? [A short description, and/or a concise list of topics - possibly from your course syllabus.(This is likely to be your longest answer)] 
 
Part 1: Introduction to Web Mining It introduces what is web mining and its architecture, challenges and security over the web.  
 
Part II: Web Crawling and Indexing This section covers the way to fetch and store the data from the web using recent algorithms.  

 
 
 
 
 
 
 
 
 
Part III: Three categories of web mining This section explains web mining in three different categories, its explained using the recent algorithms.  
 
What is the format of the course? [Is it face to face, online or blended? How many contact hours? Does it have lectures, lab sessions, discussion classes?] 
 
This Course is designed with 100 minutes of  in-classroom sessions per week, 60 minutes of  video/reading  instructional material per week, 100 minutes of lab hours per week,   as well as 200 minutes of  non-contact time spent on implementing course related project. Generally this course should have the combination of lectures, in-class discussion, case studies, guest-lectures, mandatory off-class reading material, quizzes. 
 
 
 
 
How are students assessed? [What type, and number, of assignments are students are expected to do? (papers, problem sets, programming projects, etc.). How long do you expect students to spend on completing assessed work?] 
 
 Students are assessed on a combination group activities, classroom discussion, projects,    and continuous, final assessment tests. 
 
 Additional weightage will be given based on their rank in crowd sourced projects/ Kaggle like competitions. 
 
 Students can earn additional weightage based on certificate of completion of a related MOOC course. 
  Additional topics [List notable topics covered in the course that you do not find in the CS2013 Body of Knowledge] 
 
Other comments  [optional] 
 
 
 
 

 
 
 
 
 
 
 
 
 
Session wise plan Student Outcomes Covered: 2, 11, 14, 17 
 
Class Hour  Lab Hour 
 
Topic Covered  levels of mastery 
Reference Book 
Remarks  
2  Introduction and Architecture of the WWW  
Familiarity 1  
1  Web Document Representation- Web Search Engine – Challenges 
Usage 1  
1  Web security overview and concepts, Web application security, Basic web security model   
Familiarity 1  
1  Web Hacking Basics HTTP & HTTPS URL, Web Under the Cover Overview of Java security Reading the HTML source 
Familiarity 1  
2  Basic Crawler Algorithm: Breadth-First/ depth-First Crawlers 
Usage 1,2  
1  Universal Crawlers Usage  1,2  2  Preferential Crawlers :  Focused Crawlers - Topical Crawlers. 
 Usage 1,2   
3  Static and Dynamic Inverted Index– Index Construction and Index Compression- Latent Semantic 
Familiarity 1  

 
 
 
 
 
 
 
 
 
Indexing 2  Searching using an Inverted Index: Sequential Search - Pattern Matching - Similarity search 
Usage  1,2  
3  Link Analysis - Social Network Analysis - CoCitation and Bibliographic Coupling 
Familiarity 1,2  
3  Page Rank- Weighted Page Rank 
Usage  1,2  
2  Community Discovery - Web Graph Measurement and Modelling- Using Link Information for Web Page Classification. 
 
Familiarity 1,2  
3  Classification: Decision tree for Text Document- Naive Bayesian Text Classification - Ensemble of Classifiers.   
Assessment  1,2,3  
3  Clustering:  Kmeans Clustering - Hierarchical Clustering – Markov Models - Probability-Based Clustering. 
Assessment 1,2  
2  Vector Space Model – Latent semantic Indexing – Automatic Topic 
Usage  1  

 
 
 
 
 
 
 
 
 
Extraction from Web Documents. 
 
2  Web Usage Mining - Click stream Analysis -Web Server Log Files - Data Collection and Pre-Processing - Data Modelling for Web Usage Mining 
Usage  1,2  
4  The BIRCH Clustering Algorithm - Modelling web user interests using clustering- Affinity Analysis and the A Priori Algorithm – Binning 
Usage 1,2  
 
2  Web usage mining using Probabilistic Latent Semantic Analysis – Finding User Access Pattern via Latent Dirichlet Allocation Model. 
 
Usage 1,2  
2  Relevance Feedback and Query Expansion - Automatic Local and Global Analysis 
Usage 1,2  
2  Application Assessement         45 Hours (3 Credit hours      

 
 
 
 
 
 
 
 
 
/week  15 Weeks schedule) 
 
Approved by Academic Council No.:47 Date: 05.10.2017 
 '''
 
 
 
 
 
AI='''Subject Code :  Artificial Intelligence                                    L,  T, P,  J, C                                                                                                                       3,  0, 0,  4, 4 
 
Preamble The course deals with the specification and design of intelligent (autonomous) systems and prepares the student to identify the appropriate representation and reasoning mechanism to implement it. 
 
 
Objectives The objective of this course is to  
 
 Familiarize students with Artificial Intelligence principles and techniques   Introduce the facts and concepts of cognitive science by computational model and their applications  Explore problem-solving paradigms, search methodologies and learning algorithms 
 
Expected Outcome 
 
After successfully completing the course the student should be able to  
1. apply knowledge of computing and mathematics appropriate to the discipline 2. analyze a problem, identify and define the computing requirements appropriate to its solution 3. to design, implement, and evaluate a computer-based system, process, component, or program to meet desired needs 4. design efficient algorithm to achieve optimized solution in complex situation 5. apply heuristic methodologies in state-space problems 6. characterize various ways to represent the environmental knowledge and to infer from it 7. design the adaptive mechanism in case of uncertainty 8. implement learning algorithms to apply and resolve in real world problems 
 
SLOs 1,2,5,7,17  Module Topics  L hours SLO 1 Artificial Intelligence and its Issues Definitions - Importance of AI, Evolution of AI - Applications of AI, Classification of AI systems with respect to environment, Knowledge Inferring systems and Planning, Uncertainty and towards Learning Systems 
 9 2 
2 Overview to Problem Solving Problem solving by Search, Problem space - State space, Blind Search - Types, Performance measurement 
 
5 1,17 
3 Heuristic Search   Types, Game playing – mini-max algorithm, Alpha-Beta Pruning  
 
4 1, 17 
4 Knowledge Representation and Reasoning 
 
Logical systems – Knowledge Based systems, Propositional Logic – Constraints, Predicate Logic – First Order Logic, Inference in First Order Logic, Ontological Representations and applications 
 
7 7 
5 Uncertainty and knowledge Reasoning 
 
Overview – Definition of uncertainty, Bayes Rule – Inference, Belief Network, Utility Based System, Decision Network 
 
7 1,5,7 
6 Learning Systems 
 
Forms of Learning – Types - Supervised, unsupervised, reinforcement learning, Learning Decision Trees 
4 7 
7 Expert Systems  
 
Expert Systems‐ Stages in the development of an Expert Systems‐  Probability based Expert Systems‐Expert System Tools‐Difficulties in Developing Expert SystemsApplications of Expert Systems 
 
7 1, 5, 17 
 
 
 
8 Recent Trends 
 
2  
Project (clear explanation in an elaborated manner) Generally a team project [3 to 4 members]. The project should cover some of the following (tentative domains). i.e., 
 A machine learning approach in financial markets  Background Analysis and Design of  an Agent-Based Operating System  Intelligent Tourist Information System  Classification of objects in images based on various object representations  Visual Semantic Web Ontology based E-learning management system  Controlling a Robot Hand in Simulation and Reality  Face Detection by Image Discriminating  An intelligent mobile robot navigation technique using RFID Technology  Library Robot – Path Guiding Robotic System with AI using Microcontroller  Wireless AI Based Fire Fighting Robot for Relief Operations 
Assessment is based on 3 reviews. 
 
60 (Non Contact hours) 
5,6,14,17,18 
 
 

 
 
Text Books (overall syllabus covered) 
 
1. Stuart Russell and Peter Norvig Artificial Intelligence - A Modern Approach, Prentice Hall, 3rd edition, 2011. 2. D. Poole and A. Mackworth. Artificial Intelligence: Foundations of Computational Agents, Cambridge University Press, 2010 
 
 
Reference 
 
3. Elaine Ric, Kevin Knight and Shiv Shankar B. Nair, Artificial Intelligence, 3rd edition, Tata McGraw Hill, 2009. 4. George F. Luger, “Artificial Intelligence-Structures and Strategies for Complex Problem Solving”, 6th edition, Pearson, 2008. 5. R. Brachman, H. Levesque. Knowledge Representation and Reasoning, Morgan Kaufmann, 2004. 6. E. Alpaydin. Introduction to Machine Learning. MIT Press, 2nd edition, 2010 7. R. S. Sutton and A. G. Barto. Reinforcement Learning: An Introduction. MIT Press, 1998 8. N.P.Padhy: Artificial Intelligence and Intelligent Systems, Oxford University Press, 2009. 
 
Mode of Evaluation: 
 
 Project review/evaluation, Tests, Assignments, Seminars 
 
 
 
Artificial Intelligence 
Knowledge Areas that contain topics and learning outcomes covered in the course  
Knowledge Area Total Hours of Coverage 
CS: IS (Intelligent Systems) 
CE: HCI4 (if Computer Engineering Covered) 
45 (split up) 
 
Body of Knowledge coverage 
[List the Knowledge Units covered in whole or in part in the course.  If in part, please indicate which topics and/or learning outcomes are covered.  For those not covered, you might want to indicate whether they are covered in another course or not covered in your curriculum at all. This section will likely be the most time-consuming to complete, but is the most valuable for educators planning to adopt the CS2013 guidelines.]  
 

 KA Knowledge Unit Topics Covered Hours 
IS IS/Fundamental Issues 
Overview of AI  and its challenges  Examples of recent AI applications, Intelligent behaviour - The Turing test Rational versus non-rational reasoning Nature of environments  Fully versus partially observable  Single versus multi-agent  Deterministic versus stochastic  Static versus dynamic  Discrete versus continuous Nature of agents  Autonomous versus semi-autonomous  Reflexive,   goal-based,   utility-based The importance of perception and environmental interactions Major issues  Knowledge Inferring systems   Planning,   Uncertainty   Towards Learning Systems 
9 
IS IS/Basic Search Strategies 
Problem spaces (states, goals and operators),  problem solving by search Uninformed search (breadth-first, depth-first, depth-first with iterative deepening) Heuristics and informed search (hill-climbing, generic best-first, A*) Space and time efficiency of search Two-player games (Introduction to minimax search) 
5 
IS  IS/Basic Knowledge Representation and Reasoning 
Review of propositional and predicate logic propositional logic First Order Logic resolution Review of probabilistic reasoning,  Bayes theorem,  inference by enumeration Review of basic probability (cross-reference DS/Discrete Probability) Random variables and probability distributions Axioms of probability Probabilistic inference Bayes’ Rule 
4 
IS IS/Advanced Representation and Reasoning 
Ontological Engineering, Representations, Semantic networks 
3 
IS IS/Advanced search Constructing search trees 4 
Stochastic search Simulated annealing Minimax Search, Alpha-beta pruning 
 
 
IS IS/Reasoning Under Uncertainty 
Conditional Independence Bayesian networks Exact inference (Variable elimination) Approximate Inference (basic Monte Carlo) 
7 
IS IS/Basic Machine Learning 
Forms of Learning, Decision Trees,  Statistical-Based Learning such as Naïve Bayesian Classifier. 
4 
IS IS/Expert Systems Stages in development of Expert Systems, Probability Based, Tools, Difficulties and Challenges in building expert systems, Applications of Expert Systems: Artificial Neural network, clustering analysis 
7 
 
 
Where does the course fit in the curriculum? 
This course is an elective course and suitable from sixth semester onwards. Data Structures and Algorithms, Predicate Calculus and Probability theory are the pre-requisites for this course.  
What is covered in the course? 
 INTRODUCTION TO AI.  Fundamental concepts. Main research areas and application fields. 
 
 PROBLEM SOLVING AND SEARCH. State spaces and search methods. Non-informed and informed search strategies. Constraint satisfaction problems. Games and adversarial search. uninformed, informed search, search for optimization (hill climbing, simulated annealing, genetic algorithms), adversarial search (minimax, game trees) 
 
 LOGICAL REPRESENTATION AND REASONING. The use of propositional and first order logic for the representation of knowledge. inference complexity, unification and resolution, Knowledge-based reasoning as logical deduction. Inference procedures (forward chaining, backward chaining, resolution). 
 
 PROBABILISTIC REASONING. Axioms of probability, basic statistics (expectation and variance), inference by enumeration, Baye’s rule. 
 
 ADVANCED REPRESENTATION AND REASONING. Ontological Engineering, Representations ,Semantic networks 
 
 ADVANCED SEARCH METHODOLGIES. Constructing search trees, Stochastic search Simulated annealing, Minimax Search, Alpha-beta pruning 
 
 DECISION UNDER UNCERTAINITY. Conditional Independence, Bayesian networks Exact inference (Variable elimination), Approximate Inference (basic Monte Carlo) 
 
 EXPERT SYSTEMS.  Stages in development of Expert Systems, Probability Based, Tools, Difficulties and Challenges in building expert systems, Applications of Expert Systems: Artificial Neural network, clustering analysis 
 
 
What is the format of the course? 
[Is it face to face, online or blended? How many contact hours? Does it have lectures, lab sessions, discussion classes?] 
This course is designed for face to face interaction with 150 minutes of in-classroom sessions per week as well as 200 minutes of non-contact time spent on implementing course related project. Generally this course should have the combination of lectures, in-class discussion, case studies, guest-lectures, mandatory off-class reading material, quizzes. 
How are students assessed? 
[What type, and number, of assignments are students are expected to do? (papers, problem sets, programming projects, etc.). How long do you expect students to spend on completing assessed work?]  Students are assessed on a combination group activities, classroom discussion, projects,    and continuous, final assessment tests.  Additional weightage will be given based on their rank in crowd sourced projects/ Kaggle like competitions.  Students can earn additional weightage based on certificate of completion of a related MOOC course. 
 
 
 
Session wise plan 
 
Sl. No  
Topic Covered  Class Hour  
levels of mastery 
Reference Book 
Remarks  
1 Formal quadratic definitions of AI - Importance of AI, Evolution of AI - Applications of AI 
3 Familiarity 1 (Chap 1)  
2 Classification of AI systems with respect to environment 
2 Familiarity 1 (Chap 2), 2 (Chap 2) 
 
3 Brief overview of Knowledge Inferring systems and Planning 
2 Familiarity 1(Chap10), 2(Chap 8), 3(Chap13) 
 4 Brief overview of dealing with 2 Familiarity  1(Chap13),  
Uncertainty and towards Learning Systems 
2(Chap 6), 3(Chap 7), 4(Chap 9) 
5 Problem solving by Search, Problem space - State space, 
1 Familiarity  1(Chap 3)  
6 Types of Blind Search – DFS, BFS, IDS,  Performance measurement 
4 Usage  1(Chap 3), 2(Chap 3), 3(Chap 2), 4(Chap  3) 
 
7  Heuristics Search and it’s types 
2 Assessment  1 (Chap 3)  
8 Game playing – mini-max algorithm, Alpha-Beta Pruning 
2 Usage  1 (Chap 5)  
9 To design a heuristic algorithm for real time problems 
 Assessment  Project Component (15 hours) 
10 Logical systems – Knowledge Based systems, Propositional Logic 
2 Familiarity  1(Chap 5), 5(Chap 1) 
 
11 Constraints of Propositional Logic, Predicate Logic – First Order Logic 
3 Usage  1(Chap 8), 5 (Chap 2) 
 
12 Inference in First Order Logic by Modus Ponens and Resolution Refutation 
3 Usage  1(Chap 9)  
13 Ontological Representations and applications 
1 Assessment 1(Chap 12), 2(Chap13), 3(Chap 11)  
 
14 To implement a data model using ontology  
 Assessment  Project Component (15 hours) 
15 Overview, definition of Uncertainty and Bayes’ Rule 
2 Familiarity  1(Chap13), 2(Chap 9), 3(Chap 8) 
 16 Inference using Bayes Rule 2 Usage  1(Chap 14), 5(Chap12) 
 17 Reasoning under Uncertainty - Belief Network 2 Usage  1(Chap 14)  
18 Utility Based System, Decision Network 
3 Assessment  1(Chap 16)  
19 To develop an Expert System using Bayes model  
 
 Assessment  Project Component (15 hours) 
20 Overview of types of learning- Supervised, Reinforcement, Unsupervised 
2 Familiarity 1(Chap 18)  
21 Learning using Decision Support Trees 
2 Usage 6(Chap 9)  
22 Expert Systems, stages and development, Probability Based Expert Systems, Tools, Difficulties and Challenges in building expert systems  
 
4 Familiarity 8(Chap 6)  
23 Applications of Expert Systems: Artificial Neural network, clustering analysis 
3 Familiarity 8(Chap 6, 8)  
24 To design a NLP/Fuzzy logic system for contemporary problems 
 Assessment  Project Component (15 hours) Total hours covered  45 (Theory)    60 (Project) '''


# In[2]:


import re
import math


# In[3]:


docs=[]
docs.append(AI)
docs.append(DM)
docs.append(WM)
sw=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
tdoc=[]
termsDoc=[]
completeList=[]
names=['Artificial Intelligence','Data Mining','Web Mining']


# In[4]:



def Filter(docs):
    tdoc=[]
    global termsDoc
    for i in docs:
        tdoc.append(re.sub('[^a-zA-Z]',' ',i))
    for i in tdoc:
        termsDoc.append(list(set(i.split())))
    for i in range(len(termsDoc)):
        for j in range(len(termsDoc[i])):
            termsDoc[i][j]=termsDoc[i][j].lower()
    return termsDoc


# In[5]:


termsDoc=Filter(docs)
termsDoc


# In[6]:


def RemStopWords(termsDoc):
    global sw
    termsDoc1=termsDoc
    for i in range(len(names)):
        termsDoc[i]=[a for a in termsDoc[i] if a not in sw]
    return termsDoc,termsDoc1


# In[7]:


termsDoc,termsDoc1=RemStopWords(termsDoc)
def CreatingList(termsDoc):
    global sw
    global completeList
    trial=[]
    #trial=ai+wm+dm
    #print(len(trial),len(ai))
    trial = [a for a in termsDoc]
    for i in trial:
        for j in i:
            if j not in sw:
                completeList.append(j)
    completeList=list(set(completeList))
CreatingList(termsDoc)


# In[8]:


#completeList


# In[9]:


def BooleanMatrix(termsDoc1):
    global completeList
    lenOfDocs=[]
    for i in termsDoc1:
        lenOfDocs.append(len(i))
    l=-1
    bools=[]
    for k in termsDoc:
        temp=[]
        l=l+1
        for i in completeList:
            if(i in k):
                x=k.count(i)
                temp.append(x/lenOfDocs[l])
            else:
                temp.append(0)
        bools.append(temp)
    mat=[completeList]
    for i in bools:
        mat.append(i)
    return mat


# In[10]:


#print(completeList,bools)


# In[11]:


mat=BooleanMatrix(termsDoc1)
def idfVector(mat):
    global completeList
    idf=[]
    for i in range(len(completeList)):
        c=0
        for j in range(3):
#            print(mat[j+1][i])
            if(mat[j+1][i]>0):
                c=c+1
        idfx=math.log((1+3)/c)
        idf.append(idfx)
    return idf


# In[12]:


#matnew=mat.copy()


# In[ ]:





# In[13]:


def GetQuery():
    query=input("Enter The Query:").lower().split()
    return query


# In[14]:



def QueryDoc(query):
    qmat=[]
    qmat.append(query)
    qmat.append([])
    for i in range(len(qmat[0])):
        qmat[1].append(1)
    s=sum(qmat[1])
    for i in range(len(qmat[0])):
        qmat[1][i]=qmat[1][i]/s
    return qmat


# In[15]:


query=GetQuery()
qmat=QueryDoc(query)
idf=idfVector(mat)
def idfQueryDoc(qmat):
    idfq=[]
    index=[]
    for j in range(len(qmat[0])):
        for i in range(len(mat[0])):
            if(mat[0][i]==qmat[0][j]):
                index.append(i)
                idfq.append(idf[i])
                break
    return idfq, index


# In[30]:


idfq,index=idfQueryDoc(qmat)

def tfidfQuery(qmat,idfq,idf):
    for i in range(len(qmat[1])):
        qmat[1][i]=qmat[1][i]*idfq[i]
    return qmat


# In[31]:


qmat=tfidfQuery(qmat,idfq,idf)
def filteredMatrix(mat,qmat,index):
    mfq=[]
    for i in range(len(mat)):
        mfq.append([])
        for j in range(len(qmat[0])):
            mfq[i].append(mat[i][index[j]])
    return mfq


# In[32]:



# In[71]:


mfq=filteredMatrix(mat,qmat,index)
def FinalDict(mfq):
    final={}
    for j in range(1,len(mfq)):
        value=0
        for i in range(len(qmat[0])):
            value=value+mfq[j][i]*qmat[1][i]
        if(value!=0):
            final[value]=j
    return final

# In[72]:


final=FinalDict(mfq)
def FinalOutput(final):
    x=sorted(final)
    for i in range(len(x)):
        print(i+1,") ",names[final[x[i]]-1])


# In[73]:


FinalOutput(final)
# In[ ]:





# In[ ]:




