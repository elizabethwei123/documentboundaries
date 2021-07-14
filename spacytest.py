import spacy
def depth65(token65):
    for child in token65.children:
        return max(1 + depth65(child) for child in token65.children);
    return 1
if __name__ == "__main__":
   path = "C:/Users/eliza/Documents/gutenburg.txt"
   file = open(path, 'r')
   text = file.read()
   nlp = spacy.load('en')
   doc = nlp(text)
   pOS = {};
   entities = 0;
   roots = 0
   rootPos = {};
   depths = {};
   print('')
   print('********Sentences that have at least one neg dependency**********')
   for sent in doc.sents:
       for token in sent:
           if str(token.dep_) == 'neg':
               print(sent.text)
               print('')
               print('Starting token: ', end = ' ')
               print(token.text)
               print('')
               print('Ending token: ', end = ' ')
               print(token.head)
               print('')
   print('')
   print('******Dependency subtrees rooted on the verb went***********')
   for token in doc:
       word = str(token.text)
       value = str(token.pos_)
       root = str(token.dep_)
       if value in pOS:
           pOS[value] += 1;
       else:
           pOS[value] = 1;
       if root == 'ROOT':
           currentdepth = depth65(token)
           if currentdepth in depths:
               depths[currentdepth] += 1;
           else:
               depths[currentdepth] = 1;
           if word == 'went':
               for g in token.subtree:
                   print(g.text, end = ' ')
           if value in rootPos:
               rootPos[value] += 1;
           else:
               rootPos[value] = 1;
   print('')
   print ('******Each part of speech tag and their instances*****')
   for x in pOS:
       print(x, pOS[x])
   for ent in doc.ents:
       entities += 1
   print('')
   print('Number of named entities: ', entities)
   print('')
   print('Number of times the root is a VERB: ', rootPos['VERB'])
   sorted_names = sorted(rootPos, key=lambda a: rootPos[a], reverse = True)
   print('')
   print('******POS tags of the root of dependency trees by frequency*****')
   for x in sorted_names:
       print(x, rootPos[x])
   print('')
   print('********Depths of trees by frequency***********')
   sorted_names33 = sorted(depths, key=lambda d: depths[d], reverse=True)
   for x in sorted_names33:
       print("Depth:", end = ' ')
       print(x,'has',  depths[x], 'occurrences')



