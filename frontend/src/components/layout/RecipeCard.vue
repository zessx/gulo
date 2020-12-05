<template>
  <article class="recipe">
    <img :src="recipe.image" :alt="recipe.title">
    <div>
      <h3>{{ recipe.title }}</h3>
      <footer>
        <div class="duration" v-if="recipe.duration">
          <BaseIcon name="timing" />
          <span>{{ recipe.duration }}</span>
        </div>
        <div class="portions" v-if="recipe.portions">
          <BaseIcon name="portion" />
          <span>{{ recipe.portions }}</span>
        </div>
        <BaseButton size="small" icon="add" />
      </footer>
    </div>
  </article>
</template>

<script>
export default {
  name: 'RecipeCard',
  props: {
    recipe: {
      type: Object,
      required: true
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
    height: 100%;
    margin-right: var(--spacing-03);
    border-radius: 3px;
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
