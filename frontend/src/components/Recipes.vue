<template>
  <main class="container">
    <HeaderApp />

    <div class="search">
      <Button icon="add-recipe" size="large" class="button-new centered"
        :label="searchText ? undefined : $t('recipes.new')"
        :class="searchText ? undefined : 'grow'" />
      <router-link to="/recipes/search">
        <Button v-if="!searchText" icon="search" type="white" size="large" class="button-search" />
        <InputSearch v-if="searchText" name="search" v-bind:value="searchText" class="hide-clear-search"
          :placeholder="$t('search.placeholder')" />
      </router-link>
    </div>

    <div class="filter-meal">
      <ul>
        <li v-for="dish in dishes" :key="dish">
          <input type="radio" :id="dish" :value="dish" v-model="selectedDish" @change="refresh">
          <label :for="dish">
            <Icon :name="formatDishIcon(dish)" />
            <p>{{ $tc('recipes.' + dish, 2) }}</p>
          </label>
        </li>
      </ul>
    </div>

    <div class="results">
      <RecipeCard v-for="recipe in recipes" :key="recipe.id" :recipe="recipe" />
      <Message :message="$t('recipes.no_results')" class="centered" v-if="recipes.length == 0" />
    </div>

    <Navbar page="recipes" />
  </main>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import formatDishIcon from '@/utils/formatDishIcon'

export default {
  name: 'Recipes',
  data: function () {
    return {
      selectedDish: 'main_course',
      dishes: [
        'starter',
        'main_course',
        'dessert'
      ]
    }
  },
  computed: mapState({
    recipes: state => state.recipes.all,
    searchText: state => state.recipes.search.text
  }),
  methods: {
    refresh: function (event) {
      let search = this.$store.state.recipes.search
      search.dish = this.selectedDish
      this.$store.dispatch('recipes/getRecipesList', search)
    },
    formatDishIcon: function (dish) {
      return formatDishIcon({ dish })
    },
    ...mapActions('recipes', [
      'getRecipesList'
    ])
  },
  created () {
    this.selectedDish = this.$store.state.recipes.search.dish
    this.$store.commit('recipes/clearRecipe')
    this.refresh()
  }
}
</script>

<style lang="scss" scoped>
.search {
  display: flex;
  margin: 0 var(--spacing-05);
  padding-bottom: var(--spacing-04);
  border-bottom: 1px solid var(--background-40);

  .button-new {
    margin-right: var(--spacing-02);

    i { // TODO: ignored
      height: 2rem;
      width: 2rem;
      transform: translateY(-0.2rem);
    }

    &.grow {
      flex-grow: 1;
    }

    &:not(.grow) + a {
      flex-grow: 1;
    }
  }

  .button-search {
    i.icon { // TODO: ignored
      color: var(--background-70);
    }
  }
}

.filter-meal {
  margin: 0 var(--spacing-05);
  padding: var(--spacing-04) 0;
  border-bottom: 1px solid var(--background-40);

  ul {
    display: flex;
  }

  li {
    flex-basis: calc(100% / 3);
  }

  input[type="radio"] {
    display: none;

    &:checked + label {
      color: var(--primary-60);
      background-color: var(--primary-40);

      i {
        color: var(--primary-50);
      }
    }
  }

  label {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border-radius: 5px;
    color: var(--grey-70);
    height: 4.5rem;

    i {
      color: var(--background-50);
      height: 1.5em;
      width: 1.5em;
    }

    p {
      margin: 0;
      margin-top: var(--spacing-01);
      font-size: 0.875em;
      font-weight: bold;
    }

    + li {
      margin-left: var(--spacing-02);
    }
  }
}

.results {
  padding: var(--spacing-04) var(--spacing-02);

  .recipe {
    margin-bottom: 0.5em;
  }
}
</style>
