## Models:
1. Catboost
2. MLP
3. CNN1D
4. Simple Attention
5. Transfomer (ruBert)
6. Fasttext
7. Word2Vec (not finished)


## ANN (ANNOY):
#### n_trees = 100
Query per second: 0.37872721656920416, recall: 0.8781388223082364, num searches: 100 // 2.6404228591194257463401545675346
Query per second: 0.3730229526371151, recall: 0.9000403594174406, num searches: 200
Query per second: 0.38556676337557266, recall: 0.9068584250355932, num searches: 400
Query per second: 0.3868787612061824, recall: 0.9337387661747365, num searches: 1000
Query per second: 0.4020893026740004, recall: 0.959333797907211, num searches: 2000 // 2.4870097099070655222723480346717
Query per second: 0.4309715295766855, recall: 0.9802588727166692, num searches: 4000
Query per second: 0.4732524622742404, recall: 0.9991773715979403, num searches: 10000


#### n_trees = 200
Query per second: 0.36983839774028565, recall: 0.8781388223082364, num searches: 100
Query per second: 0.37010889342336944, recall: 0.9000403594174406, num searches: 200
Query per second: 0.37309495676819554, recall: 0.9068584250355932, num searches: 400
Query per second: 0.38875049498862174, recall: 0.9337387661747365, num searches: 1000
Query per second: 0.4007463933413507, recall: 0.959333797907211, num searches: 2000
