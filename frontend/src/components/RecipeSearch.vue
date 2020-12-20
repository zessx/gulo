<template>
  <main class="container">
    <header>
      <Button type="secondary" class="cancel" :label="$t('search.cancel')"
        v-on:click.native="cancel" />
    </header>

    <div class="search">
      <h1>{{ $t('search.new') }}</h1>

      <InputSearch name="search"
        :placeholder="$t('search.placeholder')"
        v-bind:value="search.text"
        v-on:keyup.native="typeText"
        v-on:click.native="typeText" />

      <div class="tags">
        <Tag v-for="tag in this.$store.state.tags.selected" :key="tag.pk"
          :data-tag="tag.pk" :label="tag.name" :active="true"
          v-on:click.native="unselectTag" />
        <Tag v-for="tag in tagsResults" :key="tag.pk"
          :data-tag="tag.pk" :label="tag.name"
          v-on:click.native="selectTag"/>
      </div>

      <div class="sorting">
        <Separator />

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
      <Button type="success" icon="check" size="large" class="full centered validate"
        :label="$t('search.validate')"
        v-on:click.native="validate" />
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
  computed: {
    tagsResults: function () {
      let selectedIds = this.$store.state.tags.selected.map(e => e.pk)
      return this.$store.state.tags.results.filter(
        tag => !selectedIds.includes(tag.pk)
      ).slice(0, 5)
    }
  },
  methods: {
    typeText: function (event) {
      this.search.text = document.querySelector('[name="search"]').value
      this.$store.dispatch('tags/getTagsList', this.search.text)
    },
    selectSorting: function (event) {
      let target = event.target.tagName === 'BUTTON' ? event.target : event.target.closest('button')
      const value = target.getAttribute('data-sort')
      this.search.sort = this.search.sort !== value ? value : 'date'
    },
    selectTag: function (event) {
      let target = event.target.classList.contains('tag') ? event.target : event.target.closest('.tag')
      this.$store.dispatch('tags/selectTag', target.getAttribute('data-tag'))
    },
    unselectTag: function (event) {
      let target = event.target.classList.contains('tag') ? event.target : event.target.closest('.tag')
      this.$store.dispatch('tags/unselectTag', target.getAttribute('data-tag'))
    },
    validate: function (event) {
      let target = event.target.tagName === 'BUTTON' ? event.target : event.target.closest('button')
      if (!target.disabled) {
        this.search.tags = this.$store.state.tags.selected.map(e => e.name)
        this.$store.dispatch('recipes/getRecipesList', this.search).then(() => {
          this.$router.push('/recipes')
        })
      }
    },
    cancel: function () {
      this.search = { ...this.$store.state.recipes.search }
      this.$router.push('/recipes')
    }
  },
  created () {
    this.search = { ...this.$store.state.recipes.search }
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

  .tags {
    display: flex;
    justify-content: flex-start;
    flex-wrap: wrap;
    width: 100%;
    padding: var(--spacing-06) 0;

    .tag {
      margin-right: var(--spacing-03);
      margin-bottom: var(--spacing-03);
    }
  }

  .sorting {
    width: 100%;
    margin-top: auto;
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
