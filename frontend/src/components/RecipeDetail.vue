<template>
  <main class="container">
    <header>
      <router-link to="/recipes">
        <Icon name="arrow" class="back reversed" />
      </router-link>
      <router-link to="/recipes">
        <Button icon="edit" type="secondary" class="edit" :label="$t('recipes.edit')" />
      </router-link>
    </header>

    <Loader v-if="recipe === null" />

    <article class="recipe" v-if="recipe">
      <img :src="recipe.picture" :alt="recipe.title">
      <h1>{{ recipe.title }}</h1>

      <div class="meta">
        <div class="dish">
          <Icon :name="formatDishIcon(recipe.dish)" />
          <span>{{ $tc('recipes.' + recipe.dish, 1) }}</span>
        </div>
        <div class="duration" v-if="recipe.duration">
          <Icon name="timing" />
          <span>{{ formatDuration(recipe.duration) }}</span>
        </div>
        <div class="portions" v-if="recipe.portions">
          <Icon name="portion" />
          <span>{{ recipe.portions }}</span>
        </div>
      </div>

      <div class="ingredients" v-if="recipe.ingredients.length > 0">
        <ul>
          <li v-for="ingredient in recipe.ingredients" :key="ingredient.id">
            <span v-if="ingredient.quantity">{{ ingredient.quantity }} </span>
            <span v-if="ingredient.unit">{{ $tc('ingredients.units.' + ingredient.unit, ingredient.quantity) }} </span>
            <span>{{ ingredient.name }}</span>
          </li>
        </ul>
        <Button icon="list" type="secondary" size="large" />
      </div>

      <div class="steps" v-if="recipe.steps.length > 0">
        <h2>{{ $t('recipes.making') }}</h2>
        <ol>
          <li v-for="step in recipe.steps" :key="step.id">{{ step.text }}</li>
        </ol>
      </div>
    </article>

    <Navbar page="recipes" />
  </main>
</template>

<script>
import { mapState } from 'vuex'
import formatDuration from '@/utils/formatDuration'
import formatDishIcon from '@/utils/formatDishIcon'

export default {
  name: 'RecipeDetail',
  computed: mapState({
    recipe: state => state.recipes.recipe
  }),
  methods: {
    formatDuration: function (duration) {
      return formatDuration({ duration })
    },
    formatDishIcon: function (dish) {
      return formatDishIcon({ dish })
    }
  },
  created () {
    this.$store.dispatch('recipes/getRecipe', this.$route.params.id)
  }
}
</script>

<style lang="scss" scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  padding: var(--spacing-05) var(--spacing-06);

  .back {
    color: var(--background-50);
    font-size: 1.5rem;
    transition: color var(--speed-normal);

    &:hover,
    &:focus {
      color: var(--background-60);
    }
  }
}

.recipe {
  display: flex;
  flex-direction: column;
  align-items: center;

  img {
    display: block;
    width: 100%;
    height: 11rem;
    object-fit: cover;
    object-position: center center;
    border-radius: 8px;
    padding: var(--spacing-01);
  }

  h1 {
    margin: var(--spacing-06) 0;
    text-align: center;
  }

  .meta {
    display: inline-flex;
    align-items: flex-end;
    padding: var(--spacing-04);
    border-radius: 10px;
    background-color: var(--white);

    .dish {
      + .duration,
      + .portions {
        margin-left: var(--spacing-04);
        padding-left: var(--spacing-04);
        border-left: 1px solid var(--background-40);
      }
    }

    .duration {
      + .portions {
        margin-left: var(--spacing-04);
      }
    }

    .dish,
    .duration,
    .portions {
      i {
        float: left;
        height: 1.25em;
        margin-right: var(--spacing-02);
        color: var(--background-40);
      }

      span {
        line-height: 1.35em;
      }
    }

    button {
      margin-left: auto;
    }
  }

  .ingredients {
    position: relative;
    padding: var(--spacing-06);
    padding-bottom: 0;
    width: 100%;

    button {
      position: absolute;
      right: var(--spacing-06);
      top: var(--spacing-06);
    }

    ul {
      list-style: none;
      padding: 0;
      padding-bottom: var(--spacing-06);
      border-bottom: solid 1px var(--background-40);
    }

    li {
      position: relative;
      font-weight: bold;
      line-height: 1.67em;
      padding-left: var(--spacing-06);

      &::before {
        content: "•";
        display: inline-block;
        position: absolute;
        left: 0;
        width: 1em;
        font-size: 1.5rem;
        font-weight: bold;
        color: var(--primary-50);
        margin-right: var(--spacing-05);
      }
    }
  }

  .steps {
    padding: var(--spacing-06);
    width: 100%;

    h2 {
      font-size: 0.875rem;
      font-weight: bold;
      text-transform: uppercase;
      text-align: center;
      color: var(--primary-50);
    }

    ol {
      list-style: none;
      counter-reset: li;
      padding: 0;
    }

    li {
      position: relative;
      counter-increment: li;
      margin: var(--spacing-05) 0;
      line-height: 1.33em;
      padding-left: var(--spacing-06);

      &::before {
        content: counter(li);
        display: inline-block;
        position: absolute;
        left: 0;
        width: 1em;
        font-size: 0.875rem;
        font-weight: bold;
        color: var(--primary-50);
        margin-right: var(--spacing-05);
      }
    }
  }
}
</style>
