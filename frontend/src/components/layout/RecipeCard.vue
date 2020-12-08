<template>
  <router-link tag="article" :to="'/recipes/' + recipe.pk" class="recipe">
    <img :src="recipe.picture" :alt="recipe.title">
    <div>
      <h3>{{ recipe.title }}</h3>
      <footer>
        <div class="duration" v-if="recipe.duration">
          <Icon name="timing" />
          <span>{{ formatDuration(recipe.duration) }}</span>
        </div>
        <div class="portions" v-if="recipe.portions">
          <Icon name="portion" />
          <span>{{ recipe.portions }}</span>
        </div>
        <Button size="small" icon="add" />
      </footer>
    </div>
  </router-link>
</template>

<script>
import formatDuration from '@/utils/formatDuration'

export default {
  name: 'RecipeCard',
  props: {
    recipe: {
      type: Object,
      required: true
    }
  },
  methods: {
    formatDuration: function (duration) {
      return formatDuration({ duration })
    }
  }
}
</script>

<style lang="scss" scoped>
.recipe {
  display: flex;
  height: 6.25em;
  padding: var(--spacing-01);
  border-radius: 5px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  background-color: var(--white);

  img {
    display: block;
    height: calc(6.25em - 2 * var(--spacing-01));
    width: calc(6.25em - 2 * var(--spacing-01));
    object-fit: cover;
    object-position: center center;
    margin-right: var(--spacing-03);
    border-radius: 3px;
    background-color: var(--grey-10);
  }

  > div {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    padding: var(--spacing-02);
  }

  h3 {
    margin: 0;
    font-size: 1.125em;
  }

  footer {
    display: flex;
    align-items: flex-end;
    margin-top: auto;

    .duration {

      + .portions {
        margin-left: var(--spacing-04);
      }
    }

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
}
</style>
