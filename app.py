from flask import Flask, render_template

app = Flask(__name__)

recipes = [
    {
        'id': 1,
        'name': 'Amok Trey',
        'image': 'amok-trey.png',
        'description': 'A traditional Cambodian curry dish made with fish, coconut milk, and kroeung paste. Amok Trey is typically wrapped in banana leaves and steamed.',
        'cooking_time': '45 minutes',
        'difficulty': 'Medium',
        'servings': 4,
        'ingredients': [
            '500g white fish fillets',
            '3 tbsp kroeung paste',
            '400ml coconut milk',
            '1 egg, beaten',
            '1 tbsp fish sauce',
            '1 tsp sugar',
            '2 kaffir lime leaves, finely sliced',
            'Red chili slices for garnish',
            'Banana leaves for wrapping'
        ],
        'instructions': [
            'Clean and slice the fish into bite-sized pieces.',
            'Mix the kroeung paste with coconut milk in a bowl.',
            'Add fish sauce, sugar, and beaten egg to the mixture.',
            'Add the fish pieces to the mixture and stir gently.',
            'Line a steaming dish with banana leaves.',
            'Pour in the fish mixture.',
            'Steam for about 20-30 minutes until set.',
            'Garnish with kaffir lime leaves and red chili.'
        ],
        'tips': 'If banana leaves are not available, you can use aluminum foil or simply steam in a heat-proof dish.'
    },
    {
        'id': 2,
        'name': 'Lok Lak',
        'image': 'lok-lak.jpg',
        'description': 'Cambodian Lok Lak is a popular beef stir-fry dish served with a lime and pepper dipping sauce. It\'s traditionally served on a bed of lettuce and tomatoes.',
        'cooking_time': '30 minutes',
        'difficulty': 'Easy',
        'servings': 4,
        'ingredients': [
            '500g beef tenderloin, cut into cubes',
            '2 tbsp oyster sauce',
            '1 tbsp soy sauce',
            '1 tbsp sugar',
            '2 cloves garlic, minced',
            '1 tbsp vegetable oil',
            'Lettuce leaves',
            'Sliced tomatoes',
            'Sliced cucumbers',
            '1 lime, cut into wedges',
            '1 tbsp black pepper'
        ],
        'instructions': [
            'Marinate beef in oyster sauce, soy sauce, sugar, and minced garlic for at least 20 minutes.',
            'Heat oil in a wok or large frying pan over high heat.',
            'Cook beef quickly, about 2-3 minutes for medium-rare.',
            'Prepare plates with a bed of lettuce, sliced tomatoes, and cucumbers.',
            'Place the cooked beef on top of the vegetables.',
            'Mix lime juice with black pepper for dipping sauce.',
            'Serve immediately with steamed rice.'
        ],
        'tips': 'For the best texture, don\'t overcook the beef. It should be seared outside but still tender inside.'
    },
    {
        'id': 3,
        'name': 'Nom Banh Chok',
        'image': 'nom-banh-chok.jpg',
        'description': 'Nom Banh Chok, or Cambodian noodles, is a popular breakfast dish consisting of rice noodles topped with a fish-based green curry and fresh vegetables.',
        'cooking_time': '40 minutes',
        'difficulty': 'Medium',
        'servings': 4,
        'ingredients': [
            '500g rice noodles',
            '400g fish (snakehead or catfish)',
            '2 tbsp kroeung paste',
            '2 cups coconut milk',
            '1 tbsp fish sauce',
            '1 tbsp sugar',
            'Bean sprouts',
            'Banana flowers, thinly sliced',
            'Cucumber, julienned',
            'Fresh herbs (mint, basil)',
            'Lime wedges',
            'Chili (optional)'
        ],
        'instructions': [
            'Cook the fish in water until tender, then remove bones and flake the meat.',
            'In a pot, combine the fish, kroeung paste, and coconut milk.',
            'Simmer for 15-20 minutes, then season with fish sauce and sugar.',
            'Prepare rice noodles according to package instructions.',
            'Place noodles in bowls and ladle the fish curry over them.',
            'Top with fresh vegetables and herbs.',
            'Serve with lime wedges and chili on the side.'
        ],
        'tips': 'This dish is best enjoyed fresh. The curry sauce can be made ahead of time but add the vegetables just before serving.'
    },
    {
        'id': 4,
        'name': 'Bai Sach Chrouk',
        'image': 'bai-sach-chrouk.webp',
        'description': 'Bai Sach Chrouk is a simple but delicious Cambodian breakfast dish consisting of grilled pork served with broken rice and a side of pickled vegetables.',
        'cooking_time': '35 minutes',
        'difficulty': 'Easy',
        'servings': 4,
        'ingredients': [
            '500g pork shoulder or belly',
            '2 tbsp sugar',
            '2 tbsp soy sauce',
            '1 tbsp fish sauce',
            '2 cloves garlic, minced',
            '1 tbsp coconut milk',
            '2 cups broken rice',
            'Cucumber slices',
            'Pickled carrot and daikon',
            'Fresh herbs',
            'Scallion oil'
        ],
        'instructions': [
            'Slice the pork thinly and marinate in sugar, soy sauce, fish sauce, garlic, and coconut milk for at least 1 hour.',
            'Grill or pan-fry the pork until caramelized and cooked through.',
            'Cook broken rice according to instructions.',
            'Serve the pork over rice with cucumber slices and pickled vegetables.',
            'Drizzle with scallion oil and garnish with fresh herbs.'
        ],
        'tips': 'For authentic flavor, grill the pork over charcoal if possible. The coconut milk helps tenderize the meat and adds subtle sweetness.'
    },
    {
        'id': 5,
        'name': 'Samlor Korko',
        'image': 'samlor-korko.jpg',
        'description': 'Samlor Korko is considered Cambodia\'s national soup, featuring a mix of vegetables, kroeung paste, and pork or fish. It\'s a hearty and flavorful dish.',
        'cooking_time': '50 minutes',
        'difficulty': 'Medium',
        'servings': 6,
        'ingredients': [
            '300g pork ribs or fish',
            '2 tbsp kroeung paste',
            '2 cups pumpkin, cubed',
            '1 cup eggplant, cubed',
            '1 cup green papaya, sliced',
            '2 cups morning glory or water spinach',
            '200g rice paddy herb',
            '3 tbsp prahok (fermented fish paste)',
            '2 tbsp fish sauce',
            '1 tbsp sugar',
            '6 cups water',
            'Kaffir lime leaves'
        ],
        'instructions': [
            'Bring water to a boil and add pork ribs or fish.',
            'Add kroeung paste and simmer for 10 minutes.',
            'Add pumpkin, eggplant, and green papaya.',
            'Dissolve prahok in a small amount of the broth, then add back to the pot.',
            'Add fish sauce and sugar to taste.',
            'Add morning glory and rice paddy herb just before serving.',
            'Garnish with torn kaffir lime leaves.',
            'Serve hot with rice.'
        ],
        'tips': 'Authentic Samlor Korko uses a variety of vegetables. Feel free to substitute with seasonal vegetables that are available to you.'
    },
    {
        'id': 6,
        'name': 'Kuy Teav',
        'image': 'kuy-teav.jpg',
        'description': 'Kuy Teav is a popular Cambodian noodle soup typically eaten for breakfast. It features rice noodles in a flavorful pork or beef broth.',
        'cooking_time': '45 minutes',
        'difficulty': 'Medium',
        'servings': 4,
        'ingredients': [
            '500g pork bones',
            '200g ground pork',
            '200g rice noodles',
            '2 tbsp fish sauce',
            '1 tbsp sugar',
            '1 onion, halved',
            '3 cloves garlic, crushed',
            '1 tbsp dried shrimp',
            'Bean sprouts',
            'Spring onions, chopped',
            'Cilantro, chopped',
            'Lime wedges',
            'Chili sauce'
        ],
        'instructions': [
            'Simmer pork bones in water for 30 minutes to make the broth.',
            'Add onion, garlic, dried shrimp, fish sauce, and sugar.',
            'Shape ground pork into small meatballs and add to the broth.',
            'Prepare rice noodles according to package instructions.',
            'Place noodles in bowls and ladle the hot broth over them.',
            'Top with bean sprouts, spring onions, and cilantro.',
            'Serve with lime wedges and chili sauce on the side.'
        ],
        'tips': 'For a clearer broth, blanch the bones first by bringing them to a boil, discarding the water, and then starting fresh.'
    },
    {
        'id': 7,
        'name': 'Cha Houy Teuk',
        'image': 'cha-houy-teuk.webp',
        'description': 'Cha Houy Teuk is a refreshing Cambodian jelly dessert made with agar agar and served with coconut cream. It\'s perfect for hot days.',
        'cooking_time': '20 minutes (plus cooling time)',
        'difficulty': 'Easy',
        'servings': 6,
        'ingredients': [
            '15g agar agar powder',
            '1 cup sugar',
            '4 cups water',
            'Food coloring (optional)',
            '1 cup coconut cream',
            '1/4 cup palm sugar',
            'Pandan leaves (optional)',
            'Ice cubes'
        ],
        'instructions': [
            'Dissolve agar agar in water and bring to a boil.',
            'Add sugar and stir until dissolved.',
            'Add food coloring if desired and stir well.',
            'Pour into molds or a flat tray and let cool until set.',
            'Cut the jelly into cubes.',
            'Heat coconut cream with palm sugar until sugar dissolves.',
            'Let the coconut syrup cool.',
            'Serve the jelly with coconut syrup and ice.'
        ],
        'tips': 'For added flavor, infuse the water with pandan leaves before adding the agar agar.'
    },
    {
        'id': 8,
        'name': 'Kralan',
        'image': 'kralan.jpg',
        'description': 'Kralan is a traditional Cambodian sticky rice cake cooked in bamboo tubes. It\'s filled with coconut milk, beans, and sometimes black rice.',
        'cooking_time': '60 minutes',
        'difficulty': 'Hard',
        'servings': 8,
        'ingredients': [
            '2 cups sticky rice, soaked for 4-5 hours',
            '1 cup black beans, soaked overnight',
            '2 cups coconut milk',
            '1/2 cup sugar',
            '1 tsp salt',
            'Bamboo tubes for cooking',
            'Banana leaves for wrapping'
        ],
        'instructions': [
            'Drain the soaked sticky rice and beans.',
            'Mix rice with coconut milk, sugar, and salt.',
            'Line bamboo tubes with banana leaves.',
            'Fill tubes with the rice mixture and black beans.',
            'Seal the ends of the tubes.',
            'Grill the bamboo tubes over charcoal, rotating occasionally, for about 45-60 minutes.',
            'Remove from heat and let cool slightly.',
            'Split open the bamboo to reveal the rice cake.'
        ],
        'tips': 'If bamboo tubes are not available, you can use aluminum foil formed into tubes, though the flavor won\'t be the same.'
    },
    {
        'id': 9,
        'name': 'Nom Kom',
        'image': 'nom-kom.jpg',
        'description': 'Nom Kom are Cambodian rice dumplings filled with palm sugar and coconut. They\'re wrapped in banana leaves and steamed until tender.',
        'cooking_time': '40 minutes',
        'difficulty': 'Medium',
        'servings': 12,
        'ingredients': [
            '2 cups glutinous rice flour',
            '1/2 cup warm water',
            '1/2 cup grated palm sugar',
            '1 cup grated coconut',
            '1/4 tsp salt',
            'Banana leaves, cut into squares',
            'String for tying'
        ],
        'instructions': [
            'Mix glutinous rice flour with water to form a dough.',
            'Mix palm sugar, grated coconut, and salt for the filling.',
            'Take a small piece of dough and flatten it.',
            'Place some filling in the center and wrap the dough around it.',
            'Place each dumpling on a banana leaf square.',
            'Fold the leaf around the dumpling and tie with string.',
            'Steam for about 15-20 minutes until cooked through.',
            'Serve warm or at room temperature.'
        ],
        'tips': 'Make sure the dough isn\'t too wet or it will be difficult to handle. If it\'s too dry, add a little more water.'
    },
    {
        'id': 10,
        'name': 'Prahok Ktiss',
        'image': 'prahok-ktiss.jpeg',
        'description': 'Prahok Ktiss is a savory dip made with fermented fish paste, pork, and coconut milk. It\'s typically served with fresh vegetables.',
        'cooking_time': '35 minutes',
        'difficulty': 'Medium',
        'servings': 6,
        'ingredients': [
            '200g ground pork',
            '2 tbsp prahok (fermented fish paste)',
            '1 cup coconut milk',
            '2 tbsp kroeung paste',
            '1 tbsp sugar',
            '1 tsp fish sauce',
            'Red chili slices',
            'Assorted fresh vegetables (cucumber, eggplant, cabbage)',
            'Kaffir lime leaves, finely sliced'
        ],
        'instructions': [
            'Cook ground pork in a pan until browned.',
            'Add kroeung paste and stir-fry until fragrant.',
            'Mix prahok with a little water to dissolve, then add to the pan.',
            'Add coconut milk, sugar, and fish sauce.',
            'Simmer until the sauce thickens, about 15-20 minutes.',
            'Garnish with red chili and kaffir lime leaves.',
            'Serve with fresh vegetables for dipping.'
        ],
        'tips': 'Prahok has a strong flavor, so adjust the amount according to your taste. The dip should be thick enough to cling to the vegetables.'
    },
    {
        'id': 11,
        'name': 'Num Anksom',
        'image': 'num-anksom.webp',
        'description': 'Num Anksom is a traditional Cambodian sticky rice cake wrapped in banana leaves. It\'s filled with beans, pork, and other savory ingredients.',
        'cooking_time': '60 minutes',
        'difficulty': 'Hard',
        'servings': 8,
        'ingredients': [
            '2 cups sticky rice, soaked for 4 hours',
            '200g mung beans, soaked for 2 hours',
            '200g pork belly, sliced',
            '2 cloves garlic, minced',
            '1 tbsp fish sauce',
            '1 tbsp sugar',
            'Black pepper to taste',
            'Banana leaves for wrapping',
            'String for tying'
        ],
        'instructions': [
            'Cook mung beans until soft, then mash them.',
            'Season pork with garlic, fish sauce, sugar, and black pepper.',
            'Lay out banana leaves and place a layer of soaked rice.',
            'Add mung beans and pork in the center.',
            'Cover with more rice and fold the banana leaves to form a package.',
            'Tie securely with string.',
            'Steam for 45-50 minutes until fully cooked.',
            'Remove from heat and let rest before unwrapping and slicing.'
        ],
        'tips': 'Make sure to wrap the packages tightly to prevent them from falling apart during steaming.'
    },
    {
        'id': 12,
        'name': 'Char Kroeung',
        'image': 'char-kroeung.jpg',
        'description': 'Char Kroeung is a flavorful Cambodian stir-fry made with a lemongrass paste called kroeung. It can be made with various proteins.',
        'cooking_time': '25 minutes',
        'difficulty': 'Easy',
        'servings': 4,
        'ingredients': [
            '500g protein (chicken, beef, or tofu)',
            '3 tbsp kroeung paste',
            '2 tbsp vegetable oil',
            '1 tbsp fish sauce',
            '1 tbsp soy sauce',
            '1 tbsp sugar',
            '1 red bell pepper, sliced',
            '1 cup string beans, cut into pieces',
            '2 kaffir lime leaves, finely sliced',
            'Red chilies to taste',
            'Fresh holy basil leaves'
        ],
        'instructions': [
            'Slice your chosen protein into thin strips.',
            'Heat oil in a wok or large frying pan over high heat.',
            'Add kroeung paste and stir-fry until fragrant.',
            'Add protein and cook until nearly done.',
            'Add vegetables and continue to stir-fry.',
            'Season with fish sauce, soy sauce, and sugar.',
            'Add kaffir lime leaves and chilies.',
            'Finish with fresh holy basil leaves.',
            'Serve hot with steamed rice.'
        ],
        'tips': 'Kroeung paste can be made ahead and stored in the refrigerator for up to a week, making this a quick weeknight meal.'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', recipes=recipes)

@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    if recipe:
        return render_template('recipe.html', recipe=recipe)
    else:
        return "Recipe not found", 404

if __name__ == '__main__':
    app.run(debug=True)
