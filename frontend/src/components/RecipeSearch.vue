<template>
  <main class="container">
    <header>
      <router-link to="/recipes">
        <Button type="secondary" class="cancel" :label="$t('search.cancel')" />
      </router-link>
    </header>

    <div class="search">
      <h1>{{ $t('search.new') }}</h1>

      <InputSearch name="search" v-bind:value="search.text" :placeholder="$t('search.placeholder')" v-on:keyup.native="typeText" v-on:click.native="typeText" />

      <div class="sorting">
        <h2>{{ $t('search.sort_by') }}</h2>

        <div class="sorting-buttons">
          <Button icon="timing" type="white" size="large" class="vertical" data-sort="timing"
            :label="$t('search.sort.timing')"
            :class="{ selected: search.sort === 'timing' }"
            v-on:click.native="selectSorting" />
          <Button icon="popular" type="white" size="large" class="vertical" data-sort="popular"
            :label="$t('search.sort.popularity')"
            :class="{ selected: search.sort === 'popular' }"
            v-on:click.native="selectSorting" />
        </div>
      </div>
    </div>

    <footer>
      <Button type="success" icon="check" size="large" class="full centered validate" :label="$t('search.validate')" :disabled="! canValidate()" v-on:click.native="validate" />
    </footer>
  </main>
</template>

<script>
export default {
  name: 'RecipeSearch',
  data: function () {
    return {
      search: {}
    }
  },
  methods: {
    typeText: function (event) {
      this.search.text = document.querySelector('[name="search"]').value
    },
    selectSorting: function (event) {
      let target = event.target.tagName === 'BUTTON' ? event.target : event.target.closest('button')
      const value = target.getAttribute('data-sort')
      this.search.sort = this.search.sort !== value ? value : 'date'
      // document.querySelector('[data-sort="timing"]').classList.toggle('selected', this.search.sort === 'timing')
      // document.querySelector('[data-sort="popular"]').classList.toggle('selected', this.search.sort === 'popular')
    },
    canValidate: function () {
      return (this.search.text && this.search.text.trim() !== '') ||
        (this.search.tags && this.search.tags.length > 0) ||
        (this.search.sort && this.search.sort !== 'date')
    },
    validate: function (event) {
      let target = event.target.tagName === 'BUTTON' ? event.target : event.target.closest('button')
      if (!target.disabled) {
        this.$store.dispatch('recipes/getRecipesList', this.search)
        this.$router.push('/recipes')
      }
    }
  },
  created () {
    this.search = this.$store.state.recipes.search
  }
}
</script>

<style lang="scss" scoped>
header {
  display: flex;
  justify-content: flex-end;
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

  .edit {
    box-shadow: none;
  }
}

.search {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0 var(--spacing-06);
  height: calc(100vh - (1rem + 2 * var(--spacing-03) + 2 * var(--spacing-05)) - (1.5rem + 2 * var(--spacing-04)));

  h1 {
    margin: var(--spacing-06) 0;
  }

  .sorting {
    width: 100%;
    margin-top: auto;
    border-top: 1px solid var(--background-40);
    padding-bottom: var(--spacing-06);

    h2 {
      margin: var(--spacing-06) 0;
      font-size: 0.875rem;
      font-weight: bold;
      text-align: center;
      text-transform: uppercase;
      color: var(--background-60);
    }

    .sorting-buttons {
      display: flex;
      padding: 0 var(--spacing-02);

      button {
        width: 100%;
        margin: 0 var(--spacing-02);
        transition: background-color var(--speed-quick), color var(--speed-quick);

        &:hover,
        &:focus {
          background-color: var(--white);
        }

        &.selected {
          color: var(--primary-60);
          background-color: var(--primary-40);
        }
      }
    }
  }
}

footer {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;

  button {
    border-radius: 0;
  }
}
</style>
