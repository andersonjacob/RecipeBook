import sqlite3

conn = sqlite3.connect('RecipeDB')

curs = conn.cursor()

sql = '''
SELECT r.RecipeID, r.Title, c.Category, r.Author, r.Procedure
FROM Recipe r, Category c
WHERE (r.CategoryID = c.CategoryID)
ORDER BY r.CategoryID, r.SubID
'''

isql = '''
select i.Name, ri.amount, ri.unit
from Ingredient i, RecipeIngredient ri
where (ri.RecipeID = :id)
  and (ri.IngredientID = i.IngredientID)
order by ri.IngredientOrder
'''
print sql,'\n'

for row in curs.execute(sql):
    icurs = conn.cursor()
    print row[1],'\n',row[3]
    for ingredient in icurs.execute(isql, {'id': int(row[0])}):
        print '%15s\t%s' % ('%s %s' % (ingredient[1], ingredient[2]),
                            ingredient[0])
		
    print
    print row[4]
    print
