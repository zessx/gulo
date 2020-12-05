<template>
  <div class="container">
    <h1>{{ $t('navbar.recipes') }}</h1>

    <RecipeCard v-for="recipe in recipes" :key="recipe.id" :recipe="recipe" />

    <Navbar page="recipes" />
  </div>
</template>

<script>
export default {
  name: 'Recipes',
  data: function () {
    return {
      recipes: [
        {
          id: 1,
          title: 'Porc tonkatsu',
          image: 'https://www.placecage.com/200/200',
          duration: 15,
          portions: 2
        },
        {
          id: 2,
          title: 'Bouillon de volaille',
          image: 'https://www.placecage.com/201/201',
          duration: 90,
          portions: null
        },
        {
          id: 3,
          title: 'Ramen de poulet au petits oignons marinés',
          image: 'https://www.placecage.com/202/202',
          duration: 60,
          portions: 4
        },
        {
          id: 4,
          title: 'Crêpes',
          image: 'https://www.placecage.com/203/203',
          duration: null,
          portions: 12
        },
        {
          id: 5,
          title: 'Pancakes',
          image: 'https://www.placecage.com/204/204',
          duration: 15,
          portions: 2
        },
        {
          id: 6,
          title: 'Tartiflette',
          image: 'https://www.placecage.com/205/205',
          duration: 75,
          portions: 4
        },
        {
          id: 7,
          title: 'Wraps',
          image: 'https://www.placecage.com/206/206',
          duration: 65,
          portions: 4
        }
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
h1 {
  text-align: center;
}
.recipe {
  margin-bottom: 0.5em;
}
</style>
