from elasticsearch import Elasticsearch 
# CONNECT TO THE ELASTIC CLUSTER
es=Elasticsearch([{'host':'localhost','port':9200}])

e1={
    "first_name":"nitin",
    "last_name":"panwar",
    "age": 27,
    "about": "Love to play cricket",
    "interests": ['sports','music'],
}

e2={
    "first_name" :  "Jane",
    "last_name" :   "Smith",
    "age" :         32,
    "about" :       "I like to collect rock albums",
    "interests":  [ "music" ]
}
e3={
    "first_name" :  "Douglas",
    "last_name" :   "Fir",
    "age" :         35,
    "about":        "I like to build cabinets",
    "interests":  [ "forestry" ]
}

# INSERT DOCUMENTS
res=es.index(index='megacorp',doc_type='employee',id=1,body=e1)

res=es.index(index='megacorp',doc_type='employee',id=2,body=e2)

res=es.index(index='megacorp',doc_type='employee',id=3,body=e3)

# GET DOCUMENT
res=es.get(index='megacorp',doc_type='employee',id=3)
print(res) # INCLUDES METADATA
print(res['_source']) # INCLUDES ONLY ACTUAL DATA


# DELETE A DOCUMENT
# res=es.delete(index='megacorp',doc_type='employee',id=3)
# print(res['result'])

# SEARCH DOCUMENTS
res= es.search(index='megacorp',body={'query':{'match_all':{}}})
print('Got %d hits:' %res['hits']['total'])

# SEARCH DOCUMENTS BY SPECIFYING QUERY
res= es.search(index='megacorp',body={'query':{'match':{'first_name':'nitin'}}})
print(res['hits']['hits'])


