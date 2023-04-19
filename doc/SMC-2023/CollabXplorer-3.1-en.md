<!-- # CollabXplorer: Interdisciplinary Collaboration Discovery and Recommendation -->

# Abstract

This paper presents a system called CollabXplorer for the discovery and recommendation of potential interdisciplinary partners, as well as the presentation of cross-domain collaboration networks. The system uses global semantic information and social influence to build scholar embedding models and converts academic information of scholars into vector representations to identify potential cross-domain partners. The system also uses a background recommendation engine algorithm based on user tips and personal influence to recommend suitable partners for users. Its results can be presented to the user through the visual interface of the system. In addition, we have evaluated and tested the system, which shows that the system has high accuracy and good vector representation effect, and is suitable for large-scale applications.

# Keywords

Interdisciplinary collaboration, scholar embedding, a global information and social influence, recommendation engine algorithm, visual interface.

# Introduction

Interdisciplinary collaboration has become an essential part of today's academic research. Driven by globalization and the development of information technology, more and more scholars need to collaborate with researchers in other fields to produce more innovative and comprehensive research results.

The convergence of different fields represents a promising area of scientific progress and innovation, where breakthroughs and transformations are most likely to occur. Collaborative efforts between scholars from different disciplines are essential to promote scientific development. Therefore, a systematic approach is needed to identify and recommend potential interdisciplinary collaborators. This includes discovering and evaluating existing interdisciplinary networks and recommending suitable partners based on the specific descriptions of scholars to facilitate and drive effective interdisciplinary collaboration.

However, the interdisciplinary collaboration also faces some challenges, such as subject specialization, knowledge boundaries, communication barriers, and data exchange limitations. Traditional collaborative methods are usually based on knowledge, experience, and social networks in a specific field, and are unable to discover and utilize those scholars from different subject areas but with potential collaborative relationships. Therefore, it is crucial to develop interdisciplinary collaborative discovery and recommendation systems with high accuracy and real-time performance.

Traditional methods of discovering and recommending collaborations between scholars are mainly based on the direction and content of their research within a particular field. This method usually relies on the research field, academic title, academic achievement, work experience and other data scattered in the institution of the scholar, the scholar's home page and various scholar databases. These data require a lot of manual annotation and maintenance, and it is difficult to ensure the integrity and real-time performance of the data. And because the data formats of different institutions and scholar databases are different and not completely open to the public, integrating these data is also a big challenge.
In addition, some methods rely on multimodal data, such as courseware and classroom recording data, which are too costly and not universal. Therefore, traditional scholar collaboration discovery and recommendation cannot promote in-depth exploration of collaborative relationships among scholars, nor can they address the challenges posed by the rapid development of interdisciplinary collaboration.

To tackle the above-mentioned challenges, this paper introduces a system called CollabXplorer for collaborative discovery and recommendation across disciplines. We know that to recommend suitable cross-field collaboration partners for scholars, we must first evaluate the research direction of scholars suitably. Therefore, this paper first focuses on the quantification and representation of scholars, that is, embedding scholars into a lower dimensional continuous vector space.
Specifically, we propose an innovative scholar-embedding model based on global semantic information and social influence to obtain vectors for author representation. The input of our scholar embedding model consists of two parts: global semantic information and social influence. Among them, semantic input refers to the summary of all papers of scholars, which represents all academic achievements of scholars in various disciplines. The introduction of semantic input allows us to cross the barriers between disciplines and evaluate scholars from multiple disciplines from a finer semantic dimension. Social influence input is a comprehensive measure of scholars' influence and contribution in each discipline, which reflects scholars' expertise and cooperation in interdisciplinary. At the same time, the above two inputs are calculated in real-time based on the paper abstract, the number of papers published, and the number of citations, which allows us to track the research trends of scholars in real-time.

After successfully obtaining the scholar vector, we use the existing data to find potential cross-domain collaborations among scholars and recommend collaborators that meet the needs and preferences of scholars (users). To achieve this goal, we propose an algorithm to recommend matching collaborators to users by considering the suitability between scholars, the social influence of collaborators, and the cue words entered by the user. In addition, CollabXplorer provides a user interface to help users better interact with the system and discover collaborators in the target research area. The system uses multi-level architecture and modern software technology to ensure its performance and stability of the system. In this paper, the design and implementation of the system are introduced in detail, and experts and scholars from the Beijing University of Posts and Telecommunications (BUPT) are invited to evaluate and experience the system. The experimental data strongly verify the accuracy and effectiveness of CollabXplorer.

Overall, this paper provides an effective way for scholars and researchers to discover and exploit opportunities for interdisciplinary collaboration. CollabXplorer's methods and algorithms can provide more practical and efficient tools for academia to promote more interdisciplinary cooperation and creative research results.

# Related Work

Recommender systems have been a hot concern for many researchers, and their usability is reflected in various fields. Similarly, recommender systems also play an important role in the field of education.

We have seen different solutions to the problem of collaboration across disciplines. Among them, XXX's system focuses on recommending the most suitable cross-speciality '\cite{}', simplifying and correcting the work of decision-makers, and promoting cross-speciality reform. However, the practical problem, in this case, is that there is no more consideration of the specific cooperation needs of scholars in these fields, and blind field crossover may lead to an insufficient collaboration of scholars in scientific research and waste of scientific research resources. On the other hand, the system requires multi-modal data input of papers, class intervals and classroom recordings, and requires a large amount of manually labelled data, which is not suitable for large-scale application in global institutions and subject fields.

In addition, XXX's recommendation system focuses on the recommendation of scholars of the same type '\cite{}'. After inputting author information and relevant scholar information, they rank scholars according to various factors, such as paper content, journal quality, etc., and generate evaluation scores on this basis, assign weights, and calculate scholar similarity to match scholars. However, for the requirements of cross-field cooperation, its deficiency is that we only obtain the recommendations of scholars in similar fields, but it is still very insufficient for the potential collaboration discovery across fields.

The core advantage of CollabXplorer is that we comprehensively analyze the entire public literature of scholars at the granularity of words, and we consider the needs and preferences of users when recommending collaborators. The above two innovations make CollabXplorer more universal and extensible, so that it can be applied to a wide range of disciplines, and effectively serve the needs of interdisciplinary cooperation between scholars. Compared with the current scholar recommendation system:

- We focus on the summarization of all literature of scholars, and consider the social influence and collaboration network of scholars to construct a more comprehensive vector representation method of scholars.
- We don't need scattered structured data about academic fields, job titles, academic achievements, work histories, etc. These data require a lot of manual maintenance, are difficult to integrate, and the integrity and real-time performance of the data cannot be guaranteed. Therefore, we skip the traditional feature extraction work, and directly embed scholars into the low-latitude vector space according to the content of the paper for subsequent analysis. We selected some open paper databases as data sources to ensure the integrity and real-time performance of the data.
- We do not need to construct scholarly evaluation and recommendation methods for specific subject areas. With our scholar embedding model, the resulting scholar vectors can be directly used for collaborator recommendation, which applies to a wide range of subject areas.
- We do not need a lot of manually labelled data to train the recommendation mode, but only need the user to input the prompt word, and then we can recommend the "interdisciplinary" cooperators that match the description and have a high fit for the user.

# CollabXplorer

This section describes the system design, implementation, and interaction design of CollabXplorer.
The part of system design and implementation focuses on the system architecture, data sources, scholar embedding model, scholar recommendation algorithm and the implementation of key components of CollabXplorer. The user interaction experience part mainly covers the interface design, function and user experience of the system.
The main goal of the system is to find meaningful interdisciplinary cooperation potential from a large number of unstructured academic data, and present it to users in a visual way through the recommendation algorithm.

## System Design and Implementation

The architecture \ref{fig:framework} of this system mainly includes the following layers: infrastructure layer, data layer, algorithm layer and application layer. The data layer mainly includes data storage, data acquisition and data preprocessing. The algorithm layer covers feature engineering, recommendation engine and visualization of the collaboration network for this task. The application layer contains system functions and user interfaces such as account system, user preference, academic/recommendation information statistics, prompt word input, collaborator recommendation, cooperation network interaction and site interaction.

Regarding the infrastructure, we use Docker container technology on the Alibaba Cloud Elastic Computing Service platform to package each system component into images for easy deployment and management. And the Kubernetes cluster management tool is used to realize the system's automatic deployment, maintenance and expansion.

The system adopts the development mode of front-end and back-end separation, in which the front-end is developed by the Vue.js framework, and the back-end is implemented by Python's Flask framework. A typical system workflow for a recommendation task based on user prompts can be summarized as follows.

- Front-end:
  - Implement user login, registration, authentication, etc. by calling the backend API.
  - Pass the user input to the backend via the backend API.
  - Call the backend API, pass the user input prompt as a parameter to the backend, and block the process until the backend returns the result.
- Backend:
  - Compute vectors for all scholars within all databases based on the user's prompt words and recommendation preferences.
  - Compute the suitability of all scholars concerning the current user and sort the recommended top-ranked scholars in descending order.
  - Wrap the recommendation in JSON format and return it to the front end, persisting the record.
- Front-end:
  - Receive and parse JSON data, refresh page recommendation statistics and list of recommendations.
  - Render interdisciplinary collaboration networks locally.
  - Listen for user interactions, such as clicking on scholars in the recommendation list, clicking on nodes in the interdisciplinary collaboration network, etc., and call back-end APIs to persist user behavior records.

![framework](https://my-typora-p1.oss-cn-beijing.aliyuncs.com/typoraImgs/202304142351559.png)

### Data Layer

The academic data of scholars is an important consideration when designing this system because the quality of data is the key to the recommendation algorithm. \ref{fig:data_layer} describes the design and implementation of the data layer.

![data_layer](https://web.metattri.com/i/2023/04/15/643ac1ba5199a.png)

#### Data Acquisition

We use ORCID as the unique identification of the scholar. ORCID is an open, free, and growing scholar identification system that provides each scholar with a unique, persistent, and verifiable scholar identifier.
However, ORCID does not directly provide metadata of papers, such as abstracts, keywords, etc., so we need to obtain academic information of scholars through other channels. Crossref provides metadata for most of the world's scholarly publications. According to the API provided by Crossref, using the scholar's ORCID as the parameter query, we can obtain the metadata of all the papers of the scholar, including all the authors, titles, abstracts, keywords and other information.
For scholars who are not queried on ORCID, our fallback databases are dblp and Google Scholar. By querying the name of the scholar, we can obtain the URL of each paper of that scholar. We wrote the corresponding web crawler or used the API provided by the publisher to obtain the metadata of the paper based on the URL.

We choose a more flexible non-relational database MongoDB as data storage. MongoDB is a database based on distributed file storage. Its data model is document-oriented, and its data is stored in JSON form, so it is very suitable for storing the academic information of scholars.
We define each scholar's document:

```JSON
{
  "orcid": "xxxx-xxxx-xxxx-xxxx",
  "dblp_id": "xxx/xxxx",
  "name": ["name1", "name2", "..."],
  "affiliation": [["dept.1", "Aff.1"], ["dept.2", "Aff.2"], "..."],
  "articles": {
    // 1st article's metadata
    "xxxxxx1": {  // DOI or dblp_id
      "title": "article's title",
      "url": "article's url",
      "year": "year of publication",
      "journal": "journal's name",
      "authors": [["name1", "orcid/dblp_id"], ["name2", "id"], "..."],
      "abstract": "xxxxxx",
      "keywords": ["keyword1", "keyword2", "..."],
      "citations": "n"
    },
    // 2nd article
    "xxxxxx2": {"...": "..."},
    "...": {"...": "..."}
  }
}
```

#### Data Preprocessing

In the next step, we need to preprocess the academic information of the scholars to ensure the quality of the data. Our preprocessing mainly consists of the following steps:

1. Data cleaning: Remove outliers such as missing abstracts, keywords, co-authors, etc.
2. Data Normalization: Remove stop words. Stop words are words that have no real meaning in natural language processing due to their frequent occurrence. For example:'the', 'a', 'an', 'of', 'in', 'on', etc. These words occur frequently in the text but do not contribute much to the meaning of the text, so we need to remove these stop words. We used a list of stop words from the NLTK library to normalize the data.
3. Data integration: The academic information of scholars from different data sources will be integrated, including conflict merging and deduplication. We set a timed task to automatically update academic information of scholars from data sources such as Crossref, dblp and Google Scholar every day to ensure the real-time nature of the data.

### Embedding

To extract all the features of a scholar and then perform scholar recommendation, it is necessary to convert the scholar's academic information into a vector, and we call this process scholar embedding. \ref{fig:scholar_embedding} describes the workflow of scholar embedding.

![scholar_embedding](https://my-typora-p1.oss-cn-beijing.aliyuncs.com/typoraImgs/202304101805671.png)

Word embedding, also known as distributed representation, is a widely used technique in natural language processing (NLP) that enables machines to capture the meaning and context of words. global Vectors for Word Representation (GloVe) is one such approach that is popular for its ability to produce high-quality word embeddings.

Pennington et al. `\cite` proposed the GloVe, a method for training word embeddings based on the global co-occurrence statistics of words in a corpus. The method consists of decomposing the word co-occurrence count matrix using singular value decomposition (SVD) and learning word vectors that capture statistical relationships between words.

The key formulation used in GloVe is the objective function:

$$
J = \sum_{i,j=1}^{V}f(X_{ij})(w_i^T \tilde{w_j} + b_i + \tilde{b_j} - log(X_{ij}))^2
$$

where $V$ is the vocabulary of words, $X_{ij}$ is the number of co-occurrence of words $i$ and $j$, $w_i$ and $w_j$ are word vectors, $b_i$ and $b_j$ are biased words, and $f(X_{ij})$ is a weighting function that assigns smaller weights to rare word pairs. The goal is to minimize $J$ by adjusting the word vectors and biases. Another important formula in word embedding is cosine similarity：
$$
similarity(w_i, w_j) = cos(θ) = (w_i^T *w_j) / (||w_i||* ||w_j||)
$$

It measures the similarity between two word vectors $w_i$ and $w_j$ by calculating the cosine of the angle between them. High cosine similarity values indicate that words are semantically similar and that cosine similarity is superior when performing similarity calculations for searches.

When applying GloVe to the problem of this article, i.e., constructing a semantic and combined influence-based cooperative network, the corresponding principle is to transform the abstracts of scholars' papers into vectors using GloVe's pre-trained model, a process called paper embedding. Then, based on the combined influence of each paper, a weighted average operation is performed on these paper vectors to obtain the scholar vectors, a process called scholar embedding.

#### Paper Embedding

We define the vector $\vec P$ of the paper：

$$
\vec P = \frac{1}{n}\sum_{i=1}^{n} \vec W_i
$$

where $\vec W_i$ is the word vector of the $ith$ word in the abstract of the paper and $n$ is the total number of words in the abstract of the paper. Here we use the mean value to represent the thesis vector, which is because we believe that the topic of the paper should be determined by all the words in the abstract together.

For the word vector $\vec W$, we use the NLTK library to perform text segmentation on the abstracts of papers in the database and then map the resulting words, i.e., tokens, into GloVe's pre-trained model to obtain a 100-dimensional word vector for each word. In this paper, we choose GloVe's pre-trained model (6B tokens, 400K vocab, uncased, 100d vectors), which is trained on the Wikipedia corpus.

#### Scholar Embedding

First we define some notation. $x_{ij}$ represents the total number of co-authors in paper $j$ of scholar $i$. In general, for a paper, the higher the author's ranking, the greater his contribution to that paper. Therefore, we can assume that the scholar's contribution is non-uniformly proportional to his ranking in that paper, using an exponential function to represent.`\ref{}`

![指数函数](https://my-typora-p1.oss-cn-beijing.aliyuncs.com/typoraImgs/202303082319201.png)

Based on the above assumptions, then the contribution degree $E_{Rij}$ of scholar $i$ to paper $j$ is expressed as follows:

$$
E_{Rij}= \begin{cases} e,& \text{k = 1} \\ e^{\frac{x_{ij}-k}{x_{ij}}}, & \text{others} \end{cases}
$$

where $k$ denotes the rank of the scholar among all co-authors in the paper.

In addition, the number of citations in the paper reflects the influence of the paper, and usually, the more citations, the higher the influence of the paper. Therefore, we define the impact factor $C_{ij}$ of scholar $i$'s paper $j$ as follows:
$$
C_{ij} = \begin{cases} 0,& {{n_{ij}} = 0} \\ 1, & {{n_{ij}} > 0} \end{cases}
$$

where $n_{ij}$ is the number of times the paper is cited. And combined with the impact factor $C_{ij}$ of the paper, we can get the impact $E_{Cij}$ of paper $j$, which is defined as follows:

$$
E_{Cij} = C_{ij} e^{\frac{n_{ij}}{n_{i_{max}}}}
$$

where $n_{ij}$ is the number of citations of paper $j$, $n_{i_{max}}$ is the highest single citation number of scholar $i$.

The above two steps present the contribution of scholars to the paper and the influence of the paper, respectively. Next, we improve the above equation based on the idea of PageRank, an algorithm proposed by Sergey Brin and Lawrence Page et al. `[cite?]` that takes into account the influence of other factors based on the influence of a single point of the network, and we adapt the model:
$$
E_{ij} = \lambda E_{Rij} + (1-\lambda)E_{Cij}
$$

$E_{ij}$ represents the combined influence of paper $j$, here we consider two factors: the contribution of scholar $i$ to paper $j$ $E_{Rij}$ and the influence of paper $j$ $E_{Cij}$, where the weight parameter $\lambda$ determines the influence of both $E_{Rij}$ and $E_{Cij}$ on $E_{ij}$. with values in the range $[0, 1]$.

With the above steps we obtain the influence $E_{ij}$ of scholar $i$ in paper $j$, and next multiply it with the vector $\vec{P_{ij}}$ of paper $j$ of scholar $i$ extracted by GloVe and perform the weighted average operation to obtain the vector $\vec{A_i}$ of scholar $i$, which is defined as follows:
$$
\vec{A_i} = \frac{\sum_{j=1}^{m} E_{ij} \vec{P_{ij}}}{m}
$$

where $m$ denotes the total number of papers written by scholar $i$. By this method we can obtain a vector representation of each scholar, and we call the above process author embedding.

### Collaborator Recommendation

For a recommendation system, we must consider the scholars' needs. In this paper, we allow the central scholar (for whom the system will recommend collaborators) to enter a prompt to describe the collaborator he expects to seek. Thus, our goal is to find collaborators that match the prompt and have high suitability with the central scholar. In short, we use prompts to modulate the vectors of all scholars in the database, compute the suitability of the new vectors of the central scholar and other scholars, and recommend the top-ranked scholars as collaborators. The workflow of our recommendation engine is shown in Figure \ref{fig:flow_chart}:

![flow_chart](https://web.metattri.com/i/2023/04/16/643b804f1b156.png)

Similarly to the formula `\ref{formula}`, we define the vector form $\vec{p}$ of the user input prompt.

$$
\vec{p} = \sum_{k=1}^{n} \vec{W_k}
$$

where $\vec{W_k}$ refers to the GloVe vector representation of the $kth$ word in prompt.

Next, we compute the similarity $s_{ij}$ between the vector $\vec{P_{ij}}$ of scholar $i$'s paper $j$ and the vector representation $\vec{p}$ of prompt to obtain the similarity $s_{ij}$ between paper $j$ and prompt, which is calculated as follows:
$$
s_{ij} = \cos(\vec{p}, \vec{P_{ij}})
$$

Due to $s_{ij} \in [-1, 1], E_{ij} \in [1, e]$, to change the range of $s_{ij}$ from $[-1, 1]$ to $[1, e]$, we modify the formula in the following way:

$$
s'_{ij} = \frac{e-1}{2}(s_{ij}+1) + 1
$$

where $s'_{ij}$ is the transformed value of $s_{ij}$.

In turn, we obtain the weights $W_{ij}$ of scholar $i$'s paper $j$, consisting of the similarity and the combined influence $E_{ij}$ `\cite formula` components.

$$
W_{ij} = \beta s'_{ij} + (1-\beta)E_{ij}
$$

here we introduce variable coefficients $\beta$ to weigh the importance of $s_{ij}$ and $E_{ij}$. The $\beta$ can vary according to the needs of the central scholar. Specifically, a larger $\beta$ is taken if the central scholar values the suitability with the collaborator more, and a smaller $\beta$ is taken if the social influence of the collaborator is more important.

At this point, we have the vector representation of scholar $A_i$ modulated by prompt:

$$
\vec{A_i} = \frac{\sum_{j=1}^{m} W_{ij} \vec{P_{ij}}}{m}
$$

where $m$ denotes the total number of papers written by scholars $i$.

On this basis, we calculate the suitability $S_{i}$ of central scholars and scholars $A_i$.
$$
S_{i} = \cos(\vec{U}, \vec{A_i})
$$

where $\vec{U}$ refers to the vector representation of the central scholars.

We sort $S_1 \backsim S_{126}$ in descending order and recommend the top-ranked scholars as potential collaborators of the central scholars.

## Interaction Design

![dashboard](https://web.metattri.com/i/2023/04/18/643eb58608c41.png)

Users can use this system after authenticating their academic identity and choosing to allow this system to include their academic data. After successful login, the user will enter dashboard \ref{fig:dashboard}, which is divided into three parts: sidebar console, a display interface and message notification interface. Here we will mainly introduce the display interface.

The following are described in order from left to right, top to bottom. The first is the personal information section, where the user's personal information will be displayed, such as name, organization, email, etc., and the subject and specific subdivision tags can be added by the user. The above information can be modified, saved and revoked.

The top four rectangular boxes are the number of papers published by an individual, the number of citations of his papers, the number of scholars he has collaborated with, and the number of times he has been recommended to other scholars by the system. These indicators will help users evaluate their own academic research level and cooperation level in a quantitative form.

Of the four partitions below, the first is the top-left line chart area, which in the current plot refers to the number of times per month you are referred to other scholars when they make a query. The bottom-left bar area refers to the scholars recommended to you based on your prompt, ranked from top to bottom in terms of potential collaboration possibilities.

Through the search box on the top right, users can enter unstructured prompt words that describe the research content of the collaborators they expect to seek. Based on the prompt words, the system will recommend collaborators with high suitability to the user. It is worth noting that the social influence of collaborators is also one of the recommendation metrics. Users can go to the "Setting" option to adjust their personal preference, that is, suitability first or influence first, corresponding to the size of the parameter $\beta$ `\cite{fig}`; On the other hand, the system will analyze all the recommended collaborators, classify and colour them according to the research field. Relevant statistics are presented in the "Areas of Recommend Cooperators" section.

The relationship network diagram at the bottom right is the key to our recommendation system. In this diagram, you can visually observe the potential cooperation potential between you and the recommended person. The dots in the graph represent scholars, and their sizes change accordingly with the change in cooperation potential. Wired means that two scholars have previously appeared as co-authors on the same paper; The colour of the points indicates the different fine molecular fields under the current search domain, thus helping the user to make a better choice.

In summary, this system shows the user's personal information, the level of academic research, and the functionality of the recommender system. Through various graphs and visualizations, users can gain insight into their research area, co-authors, and potential collaboration possibilities to better select partners and directions. This system provides a platform for academic researchers to communicate and cooperate, which helps to promote the progress and development of academic research.

# Evaluation

To evaluate our system, we generated scholar documents `\cite codes` for 126 scholars from BUPT and wrote them to the database. This work was supported by the BUPT Personnel Office and the library, and all data were manually proofread to ensure accuracy of the data. For this system, we designed two experiments, which are used to evaluate the effect of author embedding and recommendation respectively.

## Embedding Evaluation

To evaluate the effect of author embedding, we conduct experiments on the author similarity task. Pennington `\cite?` et al. evaluated GloVe for word similarity, and accordingly, we design the author similarity task referring to their work, this is because our embedding is based on GloVe pre-trained model. Specifically, we invited experts from the Beijing University of Posts and Telecommunications to evaluate the collaborative relationships of 126 scholars in our database. The cooperative relationship is divided into 5 levels, which are 1, 2, 3, 4 and 5 respectively, and the corresponding author similarity value is 0.2, 0.4, 0.6, 0.8 and 1. Where level 1 indicates no cooperation at all and level 5 indicates close cooperation. We denote these evaluation results as $t_{ij}$, where $i$ and $j$ denote the two scholars, respectively.

Through author embedding, we can obtain the vector representation of the scholar. We define the similarity between scholars $s_{ij}$:
$$
s_{ij} = \frac{\vec{A_i} \cdot \vec{A_j}}{{\mid \vec{A_i} \mid} \cdot {\mid \vec{A_j} \mid}}
$$

Here, $\vec{A_i}$ denotes the vector of scholar $i$, and $\vec{A_j}$ denotes the vector of scholar $j$.

According to the above method, the similarity between scholar $i$ and all other scholars $\vec{s_i}$ that the expert evaluation result $\vec{t_{i}}$ can be obtained in the same way. We choose the cosine similarity between $\vec{s_i}$ and $\vec{t_i}$ as the evaluation metric for the author similarity task, where closer to 1 indicates that our author embedding is more accurate. Let's call this metric accuracy:
$$
accuracy = \frac{\vec{s_i} \cdot \vec{t_{i}}}{{\mid \vec{s_i} \mid} \cdot {\mid \vec{t_{i}} \mid}}
$$

### 实验结果

We show the similarity between the two sets of data in `Fig.`. We chose to calculate the average accuracy for each of the 10 data points in the steps of 10 scholars. You can see that the average accuracy is roughly $(0.75, 0.95)$. The average accuracy of 126 data points is **0.91**, which indicates that our scholar embedding model can accurately reflect the collaboration between scholars.![acc](https://my-typora-p1.oss-cn-beijing.aliyuncs.com/typoraImgs/202303120043420.png)

### Model Analysis:$\lambda$的选择

In `Fig ?`, we show that `Eqn. (?)`, the impact of different choices of $\lambda$ on overall model accuracy. You can see that the accuracy increases at the beginning as $\lambda$ increases. Because when the value of $\lambda$ is larger, the author's vector is affected by its contribution, which can better reflect the importance of the author in the paper, making the evaluation more accurate. But after a certain amount of $\lambda$, the accuracy starts to drop. This is because when the value of $\lambda$ is large, the vector of authors is affected by the influence of the paper, but this influence is determined by the number of citations of the paper, and the number of citations of the paper is affected by many factors, such as the publication time of the paper, the topic of the paper, etc. Therefore, after the value of $\lambda$ reaches a certain level, the author's vector will be affected by many irrelevant factors, making the evaluation inaccurate. For this reason, we chose a value of 0.56 for $\lambda$, which gives us the maximum accuracy.

![lambda](https://my-typora-p1.oss-cn-beijing.aliyuncs.com/typoraImgs/202303102323182.png)

## Recommendation Evaluation

To evaluate the effectiveness of this recommender system, we take a manual scoring approach and invite 20 researchers from BUPT to rate the recommendation results.

### 实验设计

We allowed the 20 raters to freely choose the prompt and designated the central scholar. This allows evaluators to evaluate the accuracy of the recommender system in their familiar domain, based on their expertise and experience.
According to the prompt of the evaluator's input and the central scholar, the system recommends the top 5 collaborators, that is, generates a recommendation record. The evaluator assigns satisfaction scores to each of the five collaborators, where the score $s_j \in \left [0.00,1.00 \right]$.
To keep our sample diverse, we asked each evaluator to generate and rate five different recommendations, which meant that each evaluator had to rate 25 collaborators. Therefore, we received the scoring results of 100 recommendation records in total, containing satisfaction ratings for 500 collaborators recommended by the system.
In this evaluation, the recommendation preference of the system is suitability first. The `\cite` table shows the ratings for the top 5 recommendations.

|           | Recommendation Information |                      |      |      | Score |      |      |
| --------- | -------------------------- | -------------------- | ---- | ---- | ----- | ---- | ---- |
| Record ID | Center Scholar             | Prompt               | 1st  | 2nd  | 3rd   | 4th  | 5th  |
| 01        | \*\*                       | bioscience           | 0.54 | 0.91 | 0.39  | 0.89 | 0.36 |
| 02        | \*\*                       | graph neural network | 0.70 | 0.62 | 0.49  | 0.37 | 0.52 |
| 03        | \*\*                       | beamforming          | 0.85 | 0.84 | 0.51  | 0.69 | 0.26 |
| 04        | \*\*                       | multi-agent          | 0.82 | 0.76 | 0.74  | 0.71 | 0.40 |
| 05        | \*\*                       | econometrics         | 0.95 | 0.71 | 0.92  | 0.96 | 0.30 |

After obtaining the ratings of each rater for each recommendation, we define three evaluation metrics as follows:

$$
\begin{aligned}
T_1 &= s_{1} \\
T_3 &= 0.7s_{1}+0.2s_{2}+0.1s_{3} \\
T_5 &= 0.5s_{1}+0.3s_{2}+0.1s_{3}+0.05s_{4}+0.05s_{5}
\end{aligned}
$$

Where $T_i$ represents the rating of the first $i$ recommendations, and $s_{j}$ represents the satisfaction rating of the evaluator for the $j$ recommended collaborator.

We use box plots to describe 100 data points (recommendation records) statistically, to show the performance of the recommender system more intuitively. The horizontal axis of the box plot is the three evaluation metrics, the vertical axis is the rating, the upper and lower boundaries of the box plot are the 75% and 25% quantiles, the middle line is the median, and the upper and lower edges of the box plot are the maximum and minimum values, respectively. See the following figure \ref{fig:boxplot} :

![boxplot](https://web.metattri.com/i/2023/04/19/643ee417c861d.png)

The median and mean values of $T_1$ are 0.85 and 0.84, respectively, which are higher than those of $T_3$ and $T_5$, indicating that the evaluation is generally more satisfied with the first collaborator recommended by the system. This indicates that under the recommendation preference of suitability priority, the fit between the first collaborator recommended by the system and the scholars of the centre can meet the needs of carrying out cooperation.
The gap between the median and mean values of $T_3$ and $T_1$ is around $1\%$, which can be considered as the recommendation quality is similar. On the other hand, $T_3$ has the smallest variance, indicating that the top 3 recommended by the system are the relatively stable fit between the collaborators and the centre scholars.
$T_5$ has the lowest median and mean, as well as the largest variance, indicating a decline in recommendation quality and stability. This is also in line with expectations, because among the top 5 recommended collaborators, the fit between the collaborators and the centre scholars is gradually decreasing, and some collaborators may affect the overall recommendation quality of $T_5$. However, to ensure the diversity of recommendations, we will try to minimize such quality and stability degradation problems in our future work.
In general, the median and the mean value of $T_1-T_5 $ are all above 0.8, which indicates that the recommendation system designed in this study has good accuracy in recommending coauthors with a high degree of relevant fit, and can recommend valuable coauthors for scholars.

# Conclusion

In summary, this paper presents CollabXplorer, an innovative system for interdisciplinary collaboration discovery and recommendation in the academic community. With the drastic development of globalization and information technology, interdisciplinary collaboration has become essential for producing innovative and comprehensive research outcomes. However, disciplinary specialization, knowledge boundaries, and communication barriers remain challenges in interdisciplinary collaboration. To address these challenges, this paper proposes a systematic approach that includes discovering and evaluating existing interdisciplinary networks, constructing an author embedding model based on global semantic information and social influence, and recommending suitable partners based on scholars' specific descriptions.

The proposed system's architecture comprises infrastructure, data, algorithm, and application layers, using data acquisition sources such as the ORCID system, Crossref, dblp, and Google Scholar databases. To ensure the quality of the data, the system preprocesses academic information by cleaning, normalizing, and integrating data from different sources. Scholar vectors are constructed by analyzing the abstracts of scholars' publications using a scholar embedding method, allowing for a more comprehensive evaluation of scholars from multiple disciplines. The user interface of the system is user-friendly, allowing for easy deployment and management worldwide.

Experiments on author embedding and recommendations demonstrate that the system can accurately reflect the cooperation relationship between scholars and accurately recommend valuable collaborators with a high degree of similarity in research interest. This paper provides a practical and efficient tool for the academic community to promote interdisciplinary collaboration and creative research outcomes. Future work aims to minimize the decline in recommendation quality beyond the top 3 recommended collaborators while maintaining diversity. Overall, the proposed system provides a platform for academic communication and collaboration, helping researchers to find suitable collaboration partners and move forward in their research effectively.

# Reference
