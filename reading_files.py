#ef load_recipeds(file_path):
   #try :
with open("myfile.txt","r") as file:
    content=file.read()
    recipes=content.split("\n\n")
    recipe_dict={}
    for recipe in recipes:
        lines=recipe.strip().split("\n")
        if len(lines)>=3:
            name=lines[0].strip()
            ingredients=lines[1].replace('ingridients :','').strip()
            instructions=lines[2].replace("instructuins","").strip()
            recipe_dict[name]={"ingridients":ingredients , "instructions":instructions}
    print(recipe_dict) 

